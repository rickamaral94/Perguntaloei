package br.com.perguntaloei

import android.app.Application
import android.os.Looper
import androidx.test.core.app.ApplicationProvider
import androidx.test.ext.junit.runners.AndroidJUnit4
import br.com.perguntaloei.audio.Sfx
import br.com.perguntaloei.game.GameAction
import br.com.perguntaloei.game.Phase
import br.com.perguntaloei.game.Speech
import br.com.perguntaloei.game.Transcript
import br.com.perguntaloei.model.GameConfig
import br.com.perguntaloei.model.Question
import br.com.perguntaloei.model.QuestionFormat
import br.com.perguntaloei.voice.Listener
import br.com.perguntaloei.voice.SoundPlayer
import br.com.perguntaloei.voice.SpeakResult
import br.com.perguntaloei.voice.Speaker
import br.com.perguntaloei.voice.SpeechEvent
import br.com.perguntaloei.voice.TtsStatus
import br.com.perguntaloei.voice.VoiceDeps
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test
import kotlinx.coroutines.launch
import org.junit.runner.RunWith
import org.robolectric.Shadows.shadowOf
import org.robolectric.annotation.Config
import java.time.Duration

/** Voz falsa: guarda cada leitura e só "termina" quando o teste mandar. */
class FakeSpeaker(onStatus: (TtsStatus) -> Unit) : Speaker {
    override val status = TtsStatus.READY
    override var isSpeaking = false
    override val engine: String? = null
    override var currentVoice: String? = null
    val voiceList = listOf(
        br.com.perguntaloei.voice.VoiceOption("pt-br-x-neural", "Voz neural", 500, needsNetwork = false, installed = true),
        br.com.perguntaloei.voice.VoiceOption("pt-br-x-online", "Voz online", 500, needsNetwork = true, installed = true),
        br.com.perguntaloei.voice.VoiceOption("pt-br-x-basica", "Voz básica", 300, needsNetwork = false, installed = true),
    )
    override fun voices() = voiceList
    override fun selectVoice(name: String?, allowNetwork: Boolean): String? {
        val usable = voiceList.filter { allowNetwork || !it.needsNetwork }
        currentVoice = (usable.firstOrNull { it.name == name } ?: usable.first()).name
        return currentVoice
    }
    val readings = mutableListOf<Pair<List<Speech>, (SpeakResult) -> Unit>>()
    var stops = 0

    init { onStatus(TtsStatus.READY) }

    override fun speak(parts: List<Speech>, rate: Float, onDone: (SpeakResult) -> Unit) {
        isSpeaking = true
        readings += parts to onDone
    }

    /** Termina a leitura mais recente que contém [marker] (ou a última). */
    fun finishLast(result: SpeakResult = SpeakResult.COMPLETED) {
        isSpeaking = false
        readings.last().second(result)
    }

    fun lastText(): String = readings.last().first.joinToString(" ") { it.text }

    // Como um TTS defeituoso: NÃO descarta o retorno das leituras interrompidas.
    override fun stop() { stops++; isSpeaking = false }
    override fun shutdown() = Unit
}

class FakeListener(var available: Boolean = true) : Listener {
    override var isListening = false
    var starts = 0
    var cancels = 0
    private var callback: ((SpeechEvent) -> Unit)? = null
    override fun isAvailable() = available
    override fun start(onEvent: (SpeechEvent) -> Unit) { starts++; isListening = true; callback = onEvent }
    override fun stop() = Unit
    override fun cancel() { cancels++; isListening = false }
    override fun destroy() = Unit
    fun say(text: String, confidence: Float? = 0.92f) {
        isListening = false
        callback!!(SpeechEvent.Results(listOf(Transcript(text, confidence))))
    }
    fun silence() {
        isListening = false
        callback!!(SpeechEvent.Failure("Não ouvi nenhuma resposta.", silence = true, serviceProblem = false))
    }
}

class SilentSounds : SoundPlayer {
    override var enabled = true
    val played = mutableListOf<Sfx>()
    override fun play(sfx: Sfx) { played += sfx }
    override fun release() = Unit
}

@RunWith(AndroidJUnit4::class)
@Config(sdk = [34])
class VoiceFlowTest {

    private lateinit var app: Application
    private lateinit var speaker: FakeSpeaker
    private lateinit var listener: FakeListener
    private lateinit var vm: AppViewModel

    private fun newVm(micAvailable: Boolean = true, permission: Boolean = true): AppViewModel {
        listener = FakeListener(micAvailable)
        return AppViewModel(app, VoiceDeps({ _, s -> FakeSpeaker(s).also { speaker = it } }, listener, SilentSounds(), { permission }))
            .also { idle(50) }
    }

    private fun idle(ms: Long = 800) = shadowOf(Looper.getMainLooper()).idleFor(Duration.ofMillis(ms))

    private val q: Question get() = vm.engine.currentQuestion(vm.game!!)!!
    private fun scoreOfCurrent() = vm.game!!.score(vm.game!!.currentPlayer!!.id)
    private fun totalScore() = vm.game!!.players.sumOf { vm.game!!.score(it.id) }

    private fun spokenCorrect(q: Question) = q.answer
    private fun spokenWrong(q: Question) = when (q.format) {
        QuestionFormat.OPEN -> "banana com canela"
        else -> q.options[(q.correctIndex + 1) % q.options.size]
    }

    @Before
    fun setUp() {
        app = ApplicationProvider.getApplicationContext()
        vm = newVm()
        listOf("Paula" to 45, "Katharina" to 39, "Ricardo" to 32, "Vilma" to 63).forEach { (n, a) -> vm.addPlayer(n, a) }
        vm.updateSettings { it.copy(speechConsent = true, autoListen = true) }
    }

    /** Começa a partida e deixa a primeira pergunta sendo lida. */
    private fun startAsking(config: GameConfig = GameConfig(rounds = 2)) {
        vm.startNewGame(config)
        idle()
        vm.dispatch(GameAction.BeginRound)
        idle()
        assertEquals(Phase.ASKING, vm.game!!.phase)
    }

    private fun finishReadingAndListen() {
        speaker.finishLast()
        idle()
        assertTrue("microfone deveria estar aberto", vm.voice.listening)
    }

    @Test
    fun ifTheNeuralVoiceFailsTheGameGoesBackToTheDefaultVoiceAndRemembers() {
        val abis = android.os.Build.SUPPORTED_ABIS
        org.robolectric.util.ReflectionHelpers.setStaticField(android.os.Build::class.java, "SUPPORTED_ABIS", arrayOf("arm64-v8a"))
        try {
        val base = java.io.File(app.filesDir, "voz-teste-falha")
        val pack = br.com.perguntaloei.voice.NeuralVoicePack(base, files = listOf(br.com.perguntaloei.voice.VoiceFile("m", 1, "x")))
        pack.dir.mkdirs()
        java.io.File(pack.dir, "m").writeText("1")
        java.io.File(pack.dir, ".instalado").writeText("ok")
        val neural = br.com.perguntaloei.voice.NeuralSpeaker.ENGINE_ID
        val asked = mutableListOf<String?>()
        val vm = AppViewModel(app, VoiceDeps({ e, s ->
            asked += e
            if (e == neural) {
                object : Speaker by FakeSpeaker(s) {
                    override val engine = neural
                    override val status = TtsStatus.UNAVAILABLE
                    init { android.os.Handler(Looper.getMainLooper()).post { s(TtsStatus.UNAVAILABLE) } }
                }
            } else FakeSpeaker(s)
        }, FakeListener(true), SilentSounds(), { true }, pack))
        idle(50)
        assertTrue(vm.neuralInstalled)
        vm.chooseEngine(neural)
        idle(50)
        assertEquals(listOf(null, neural, SYSTEM_VOICE), asked)
        assertEquals(SYSTEM_VOICE, vm.settings.ttsEngine)
        assertEquals(TtsStatus.READY, vm.ttsStatus)
        assertTrue((vm.dialog as? AppDialog.Message)?.text.orEmpty().contains("voz padrão"))
        } finally {
            org.robolectric.util.ReflectionHelpers.setStaticField(android.os.Build::class.java, "SUPPORTED_ABIS", abis)
        }
    }

    @Test
    fun theDefaultVoiceIsTheSystemOneAndTheNeuralVoiceNeedsToBeDownloaded() {
        val asked = mutableListOf<String?>()
        val pack = br.com.perguntaloei.voice.NeuralVoicePack(java.io.File(app.filesDir, "voz-teste-padrao"))
        val vm = AppViewModel(app, VoiceDeps({ e, s -> asked += e; FakeSpeaker(s) }, FakeListener(true), SilentSounds(), { true }, pack))
        idle(50)
        assertEquals(listOf<String?>(null), asked)
        assertFalse(vm.usingNeuralVoice)
        assertFalse(vm.neuralInstalled)
        assertTrue(vm.engineOptions.none { it.packageName == br.com.perguntaloei.voice.NeuralSpeaker.ENGINE_ID })
        vm.chooseEngine(br.com.perguntaloei.voice.NeuralSpeaker.ENGINE_ID)
        assertEquals("sem baixar, a voz neural não é usada", 1, asked.size)
        assertTrue(vm.dialog is AppDialog.Message)
        vm.dialog = null
        vm.askNeuralDownload()
        assertEquals("o download só começa depois da confirmação", AppDialog.ConfirmVoiceDownload, vm.dialog)
        assertEquals(null, vm.neuralProgress)
    }

    @Test
    fun microphoneOpensOnlyAfterTheQuestionAndOptionsAreRead() {
        startAsking()
        val reading = speaker.lastText()
        assertTrue("anuncia a vez", reading.contains("Paula"))
        assertTrue(reading.contains(q.text))
        q.options.forEach { assertTrue("alternativa lida: $it", reading.contains(it)) }
        assertFalse("a leitura não pode revelar a resposta", q.format == QuestionFormat.OPEN && reading.contains(q.explanation))
        // Durante a leitura: microfone fechado e alternativas bloqueadas.
        assertEquals(0, listener.starts)
        assertFalse(vm.voice.readingDone)
        vm.touchOption(0)
        assertEquals(Phase.ASKING, vm.game!!.phase)
        vm.listenForAnswer()
        idle()
        assertEquals("Ouvir resposta é recusado durante a leitura", 0, listener.starts)
        // Terminada a leitura, o microfone abre (escuta automática ligada).
        speaker.finishLast()
        idle()
        assertEquals(1, listener.starts)
        assertTrue(vm.voice.listening)
    }

    @Test
    fun lateCallbackFromAnInterruptedReadingNeverOpensTheMicrophone() {
        startAsking()
        val first = speaker.readings.last().second
        vm.repeatQuestion()
        idle()
        first(SpeakResult.COMPLETED) // retorno atrasado da leitura antiga
        idle()
        assertEquals(0, listener.starts)
        assertFalse(vm.voice.readingDone)
        finishReadingAndListen()
    }

    @Test
    fun clearSpokenAnswerIsEvaluatedOnceAndOnlyForThePlayerOfTheTurn() {
        startAsking()
        finishReadingAndListen()
        val player = vm.game!!.currentPlayer!!.id
        listener.say(spokenCorrect(q))
        idle()
        assertEquals(Phase.REVEAL, vm.game!!.phase)
        assertEquals(1, vm.game!!.score(player))
        assertEquals(1, totalScore())
        assertTrue("anuncia o próximo jogador", speaker.lastText().contains("Próxima vez: Katharina"))
    }

    @Test
    fun uncertainTranscriptIsConfirmedBeforeEvaluation() {
        startAsking()
        finishReadingAndListen()
        listener.say("acho que é ${spokenCorrect(q)}")
        idle()
        assertEquals(Phase.ASKING, vm.game!!.phase)
        assertTrue(vm.voice.pending is Pending.Confirm)
        assertEquals(0, totalScore())
        vm.resolvePending(false)
        idle()
        assertEquals(0, totalScore())
        assertEquals(Phase.ASKING, vm.game!!.phase)
        // Fala de novo com clareza e confirma tocando em "Sim".
        speaker.finishLast(); idle()
        listener.say("acho que é ${spokenCorrect(q)}")
        idle()
        vm.resolvePending(true)
        idle()
        assertEquals(1, totalScore())
    }

    @Test
    fun confirmationCanAlsoBeSpoken() {
        startAsking()
        finishReadingAndListen()
        listener.say("talvez ${spokenWrong(q)}")
        idle()
        assertTrue(vm.voice.pending is Pending.Confirm)
        speaker.finishLast() // "Entendi: ... Confirma?"
        idle()
        assertTrue(vm.voice.listeningForConfirmation)
        listener.say("sim")
        idle()
        assertEquals(Phase.REVEAL, vm.game!!.phase)
        assertEquals(0, totalScore())
    }

    @Test
    fun inaudibleAnswerGivesNoPointAndKeepsTheTurn() {
        startAsking()
        finishReadingAndListen()
        val player = vm.game!!.currentPlayer
        listener.silence()
        idle()
        assertEquals(Phase.ASKING, vm.game!!.phase)
        assertEquals(player, vm.game!!.currentPlayer)
        assertEquals(0, totalScore())
        assertTrue(vm.voice.message!!.contains("Não ouvi"))
        // O grupo pode encerrar a vez sem ponto.
        vm.dispatch(GameAction.NoAnswer)
        assertEquals(0, totalScore())
        assertEquals(Phase.REVEAL, vm.game!!.phase)
    }

    @Test
    fun askingToRepeatIsNotAnAnswer() {
        startAsking()
        finishReadingAndListen()
        val readings = speaker.readings.size
        val stateBefore = vm.game
        listener.say("repete por favor")
        idle()
        assertEquals(stateBefore, vm.game)
        assertTrue("leu de novo", speaker.readings.size > readings)
        assertTrue(speaker.lastText().contains(q.text))
        assertFalse("microfone fechado enquanto relê", vm.voice.listening)
        assertEquals(0, totalScore())
    }

    @Test
    fun mentioningTwoOptionsAsksForClarification() {
        startAsking(GameConfig(rounds = 2, themes = listOf(br.com.perguntaloei.model.Theme.GEOGRAFIA)))
        if (q.format != QuestionFormat.MULTIPLE_CHOICE) return
        finishReadingAndListen()
        listener.say("${q.options[0]} ou ${q.options[1]}")
        idle()
        assertTrue(vm.voice.pending is Pending.Clarify)
        assertEquals(0, totalScore())
        assertEquals(Phase.ASKING, vm.game!!.phase)
    }

    @Test
    fun microphoneNeverOpensOutsideAQuestion() {
        startAsking()
        vm.answerByTouch()
        if (q.format == QuestionFormat.OPEN) vm.typedAnswer(q.answer) else vm.touchOption(q.correctIndex)
        idle()
        assertEquals(Phase.REVEAL, vm.game!!.phase)
        val starts = listener.starts
        vm.listenForAnswer()
        idle(2000)
        assertEquals(starts, listener.starts)
    }

    @Test
    fun speechNeedsConsentAndPermissionFirst() {
        vm.updateSettings { it.copy(speechConsent = null) }
        startAsking()
        speaker.finishLast()
        idle()
        assertEquals("sem consentimento não abre sozinho", 0, listener.starts)
        vm.listenForAnswer()
        assertEquals(AppDialog.SpeechConsent, vm.dialog)
        vm.onSpeechConsent(false)
        assertEquals(0, listener.starts)
        assertTrue(vm.voice.touchMode)
    }

    @Test
    fun touchOnlyGameWorksWithoutAnySpeechRecognizer() {
        Thread.sleep(300) // jogadores salvos em disco pelo setUp
        vm = newVm(micAvailable = false)
        assertEquals(4, vm.players.size)
        assertFalse(vm.recognitionAvailable)
        vm.startNewGame(GameConfig(rounds = 2, voiceHost = false, voiceAnswers = false))
        var guard = 0
        while (!vm.game!!.finished && guard++ < 200) {
            val g = vm.game!!
            when (g.phase) {
                Phase.ROUND_INTRO -> vm.dispatch(GameAction.BeginRound)
                Phase.ASKING -> {
                    assertTrue("modo sem voz libera as respostas na hora", vm.voice.readingDone)
                    vm.listenForAnswer() // sem reconhecedor: avisa e segue no toque
                    vm.dialog = null
                    val question = q
                    if (question.format == QuestionFormat.OPEN) vm.typedAnswer(question.answer) else vm.touchOption(question.correctIndex)
                    assertEquals(Phase.REVEAL, vm.game!!.phase)
                }
                Phase.REVEAL -> vm.dispatch(GameAction.Next)
                else -> vm.dispatch(GameAction.AcceptTie)
            }
            idle(50)
        }
        assertTrue(vm.game!!.finished)
        assertEquals(0, listener.starts)
        assertEquals("todos acertaram tudo", vm.game!!.players.size * 2, vm.game!!.players.sumOf { vm.game!!.score(it.id) })
    }

    @Test
    fun interruptionStopsTheMicrophoneAndTheGameResumesFromDisk() {
        startAsking()
        finishReadingAndListen()
        vm.onAppPaused()
        assertFalse(vm.voice.listening)
        assertTrue(listener.cancels > 0)
        val saved = vm.game
        Thread.sleep(400) // gravação em disco (thread de E/S)
        idle()
        // Processo recriado: um novo ViewModel lê a partida salva.
        val vm2 = newVm()
        assertEquals(saved, vm2.game)
        vm2.go(Screen.GAME)
        idle()
        assertTrue("relê a pergunta ao retomar", speaker.lastText().contains(vm2.engine.currentQuestion(saved!!)!!.text))
    }

    @Test
    fun undoAfterAMisheardAnswerRestoresTheScore() {
        startAsking()
        finishReadingAndListen()
        listener.say(spokenCorrect(q))
        idle()
        assertEquals(1, totalScore())
        vm.dispatch(GameAction.Undo)
        idle()
        assertEquals(0, totalScore())
        assertEquals(Phase.ASKING, vm.game!!.phase)
        assertTrue(vm.voice.readingDone)
        assertNotNull(vm.game!!.notice)
    }

    @Test
    fun permissionsAreRequestedOnceAtFirstLaunch() {
        vm = newVm(permission = false)
        vm.updateSettings { it.copy(permissionsAsked = false, speechConsent = null) }
        vm.onAppStart()
        assertEquals(AppDialog.Permissions, vm.dialog)
        val events = mutableListOf<UiEvent>()
        val job = kotlinx.coroutines.CoroutineScope(kotlinx.coroutines.Dispatchers.Main.immediate).launch { vm.events.collect { events += it } }
        idle()
        vm.onPermissionsChoice(true)
        idle()
        assertEquals(listOf<UiEvent>(UiEvent.RequestMicPermission), events)
        assertEquals(true, vm.settings.speechConsent)
        assertTrue(vm.settings.permissionsAsked)
        vm.onAppStart()
        assertEquals("não pergunta de novo", null, vm.dialog)
        job.cancel()
    }

    @Test
    fun decliningAtLaunchKeepsTheGameTouchOnly() {
        vm.updateSettings { it.copy(permissionsAsked = false, speechConsent = null) }
        vm.onAppStart()
        vm.onPermissionsChoice(false)
        assertEquals(false, vm.settings.speechConsent)
        startAsking()
        speaker.finishLast()
        idle()
        assertEquals("sem consentimento o microfone não abre", 0, listener.starts)
        assertTrue(vm.voice.readingDone)
    }

    @Test
    fun inactivePlayersStaySavedButDoNotPlay() {
        val ricardo = vm.players.first { it.name == "Ricardo" }
        vm.setPlayerActive(ricardo.id, false)
        assertEquals(4, vm.players.size)
        vm.startNewGame(GameConfig(rounds = 1))
        assertEquals(listOf("Paula", "Katharina", "Vilma"), vm.game!!.players.map { it.name })
        // Todos desligados: não começa.
        vm.leaveFinishedGame()
        vm.players.forEach { vm.setPlayerActive(it.id, false) }
        vm.startNewGame(GameConfig(rounds = 1))
        assertTrue(vm.dialog is AppDialog.Message)
        assertEquals(null, vm.game)
    }

    @Test
    fun theMostNaturalOfflineVoiceIsChosenAndCanBeChanged() {
        idle()
        assertEquals("pt-br-x-neural", vm.currentVoice)
        assertTrue("vozes online ficam ocultas sem permissão", vm.voiceOptions.none { it.needsNetwork })
        vm.chooseVoice("pt-br-x-basica")
        assertEquals("pt-br-x-basica", vm.currentVoice)
        assertEquals("pt-br-x-basica", vm.settings.ttsVoice)
        vm.setAllowNetworkVoices(true)
        assertTrue(vm.voiceOptions.any { it.needsNetwork })
    }
}
