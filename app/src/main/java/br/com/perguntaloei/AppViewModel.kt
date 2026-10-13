package br.com.perguntaloei

import android.Manifest
import android.app.Application
import android.content.pm.PackageManager
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.core.content.ContextCompat
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import br.com.perguntaloei.audio.Sfx
import br.com.perguntaloei.audio.SoundFx
import br.com.perguntaloei.data.AppSettings
import br.com.perguntaloei.data.GameSummary
import br.com.perguntaloei.data.HistoryEntry
import br.com.perguntaloei.data.LocalStore
import br.com.perguntaloei.data.QuestionHistory
import br.com.perguntaloei.game.AnswerChoice
import br.com.perguntaloei.game.AnswerInterpreter
import br.com.perguntaloei.game.AnswerMethod
import br.com.perguntaloei.game.CommandKind
import br.com.perguntaloei.game.GameAction
import br.com.perguntaloei.game.GameEngine
import br.com.perguntaloei.game.GameState
import br.com.perguntaloei.game.Interpretation
import br.com.perguntaloei.game.NotEnoughQuestionsException
import br.com.perguntaloei.game.Outcome
import br.com.perguntaloei.game.Phase
import br.com.perguntaloei.game.PresenterScript
import br.com.perguntaloei.game.RoundKind
import br.com.perguntaloei.game.Speech
import br.com.perguntaloei.model.GameConfig
import br.com.perguntaloei.model.Player
import br.com.perguntaloei.model.Question
import br.com.perguntaloei.questions.QuestionBank
import br.com.perguntaloei.questions.TextNormalizer
import br.com.perguntaloei.voice.SpeakResult
import br.com.perguntaloei.voice.SpeechEvent
import br.com.perguntaloei.voice.SpeechInput
import br.com.perguntaloei.voice.TtsStatus
import br.com.perguntaloei.voice.VoiceHost
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.SharedFlow
import kotlinx.coroutines.launch
import java.io.File
import java.util.UUID

enum class Screen { HOME, PLAYERS, SETUP, GAME, LOG, RULES, SETTINGS }

/** O que o jogo espera do grupo antes de avaliar. */
sealed interface Pending {
    data class Confirm(val choice: AnswerChoice, val description: String, val reason: String, val heard: String, val method: AnswerMethod) : Pending
    data class Clarify(val reason: String, val heard: String, val allowGroupDecision: Boolean, val method: AnswerMethod) : Pending
    data class GroupDecision(val text: String) : Pending
    data class ConfirmSkip(val heard: String) : Pending
    data class ConfirmNoAnswer(val heard: String) : Pending
}

data class VoiceUi(
    val speaking: Boolean = false,
    val listening: Boolean = false,
    val listeningForConfirmation: Boolean = false,
    val micLevel: Float = 0f,
    val partial: String = "",
    val heard: String? = null,
    val pending: Pending? = null,
    val message: String? = null,
    /** Leitura da pergunta e das alternativas terminou: respostas liberadas. */
    val readingDone: Boolean = false,
    /** O grupo escolheu responder tocando (fala interrompida). */
    val touchMode: Boolean = false,
)

sealed interface AppDialog {
    data class Message(val title: String, val text: String) : AppDialog
    data object SpeechConsent : AppDialog
    data object MicRationale : AppDialog
    data object AnnulReasons : AppDialog
    data object ConfirmEndGame : AppDialog
}

sealed interface UiEvent {
    data object RequestMicPermission : UiEvent
}

class AppViewModel(app: Application) : AndroidViewModel(app) {

    private val store = LocalStore(File(app.filesDir, "dados"))
    private val ioWriter = Dispatchers.IO.limitedParallelism(1)

    val bank: QuestionBank = app.assets.open("questions.json").use { QuestionBank.fromJson(it.reader(Charsets.UTF_8).readText()) }
    private var questionHistory: QuestionHistory = store.loadHistory()
    val engine = GameEngine(bank, { questionHistory.toUsage() })

    var screen by mutableStateOf(Screen.HOME)
        private set
    var players by mutableStateOf(store.loadPlayers())
        private set
    var settings by mutableStateOf(store.loadSettings())
        private set
    var game by mutableStateOf<GameState?>(store.loadGame())
        private set
    var voice by mutableStateOf(VoiceUi())
        private set
    var ttsStatus by mutableStateOf(TtsStatus.INITIALIZING)
        private set
    var dialog by mutableStateOf<AppDialog?>(null)
    var summaries by mutableStateOf(store.loadSummaries())
        private set
    var historyCount by mutableStateOf(questionHistory.entries.size)
        private set

    private val _events = MutableSharedFlow<UiEvent>(extraBufferCapacity = 4)
    val events: SharedFlow<UiEvent> = _events

    private val sfx = SoundFx().also { it.enabled = settings.soundEffects }
    private val host = VoiceHost(app) { ttsStatus = it }
    private val speech = SpeechInput(app)
    val recognitionAvailable: Boolean = speech.isAvailable()

    /** Identifica a pergunta em exibição; eventos de voz de outra pergunta são descartados. */
    private var presentationKey: String? = null
    private var autoRetries = 0
    private var listenAfterPermission = false
    private var pendingListenJob: Job? = null

    init {
        // Pré-calcula a detecção de quase-duplicatas fora da thread principal.
        viewModelScope.launch(Dispatchers.Default) { bank.nearDuplicates.size }
    }

    // ================================================================== navegação

    fun go(to: Screen) {
        val from = screen
        if (from == Screen.GAME && to != Screen.GAME) onAppPaused()
        screen = to
        // Voltando do histórico da partida, não relê nada: o grupo decide se quer Repetir.
        if (to == Screen.GAME && from != Screen.LOG) resumeGame()
    }

    // ================================================================== jogadores

    fun addPlayer(name: String, age: Int?) {
        val clean = name.trim()
        if (clean.isEmpty()) return
        updatePlayers(players + Player(UUID.randomUUID().toString(), clean, age))
    }

    fun editPlayer(id: String, name: String, age: Int?) {
        val clean = name.trim()
        if (clean.isEmpty()) return
        updatePlayers(players.map { if (it.id == id) it.copy(name = clean, age = age) else it })
    }

    fun removePlayer(id: String) = updatePlayers(players.filterNot { it.id == id })

    fun movePlayer(id: String, delta: Int) {
        val i = players.indexOfFirst { it.id == id }
        val j = i + delta
        if (i < 0 || j !in players.indices) return
        val list = players.toMutableList()
        list[i] = list[j].also { list[j] = list[i] }
        updatePlayers(list)
    }

    fun shufflePlayers() = updatePlayers(players.shuffled())

    /** Participantes sugeridos (opcional): adiciona os que ainda não estão na lista. */
    fun addSuggestedPlayers() {
        val suggested = listOf("Paula" to 45, "Katharina" to 39, "Ricardo" to 32, "Vilma" to 63)
        val existing = players.map { it.name.lowercase() }.toSet()
        val toAdd = suggested.filter { it.first.lowercase() !in existing }
            .map { Player(UUID.randomUUID().toString(), it.first, it.second) }
        updatePlayers(players + toAdd)
    }

    private fun updatePlayers(list: List<Player>) {
        players = list
        viewModelScope.launch(ioWriter) { store.savePlayers(list) }
    }

    // ================================================================== configurações

    fun updateSettings(transform: (AppSettings) -> AppSettings) {
        val s = transform(settings)
        settings = s
        sfx.enabled = s.soundEffects
        viewModelScope.launch(ioWriter) { store.saveSettings(s) }
    }

    fun clearQuestionHistory() {
        questionHistory = QuestionHistory()
        historyCount = 0
        viewModelScope.launch(ioWriter) { store.saveHistory(QuestionHistory()) }
    }

    fun usedInHistory(q: Question): Boolean = engine.selector.usedInHistory(q, questionHistory.toUsage())

    // ================================================================== início da partida

    fun startNewGame(config: GameConfig) {
        if (players.isEmpty()) {
            dialog = AppDialog.Message("Sem jogadores", "Cadastre pelo menos um jogador antes de começar.")
            return
        }
        updateSettings { it.copy(lastConfig = config) }
        val state = try {
            engine.newGame(config, players)
        } catch (e: NotEnoughQuestionsException) {
            dialog = AppDialog.Message("Faltam perguntas", e.message ?: "Não há perguntas suficientes.")
            return
        } catch (e: IllegalArgumentException) {
            dialog = AppDialog.Message("Não foi possível começar", e.message ?: "Configuração inválida.")
            return
        }
        silenceIO()
        voice = VoiceUi()
        game = state
        persist(state)
        screen = Screen.GAME
        react(null, state)
    }

    /** Volta para uma partida salva (ex.: depois de o app ter sido fechado). */
    private fun resumeGame() {
        val g = game ?: return
        presentationKey = null
        voice = VoiceUi()
        react(null, g, resumed = true)
    }

    fun leaveFinishedGame() {
        silenceIO()
        game = null
        viewModelScope.launch(ioWriter) { store.clearGame() }
        screen = Screen.HOME
    }

    // ================================================================== ações do jogo

    fun dispatch(action: GameAction) {
        val old = game ?: return
        val new = engine.reduce(old, action)
        if (new == old) return // ação fora de hora: nada muda
        game = new
        persist(new)
        react(old, new)
    }

    private fun persist(state: GameState) {
        viewModelScope.launch(ioWriter) { store.saveGame(state) }
    }

    private fun keyOf(state: GameState): String? {
        val r = state.round ?: return null
        val slot = r.currentSlot ?: return null
        return "${state.match}-${r.kind}-${r.number}-${r.turnIndex}-${slot.questionId}"
    }

    /** Reage à mudança de estado: fala, efeitos sonoros e microfone. */
    private fun react(old: GameState?, new: GameState, resumed: Boolean = false) {
        val newKey = keyOf(new)
        val phaseChanged = old?.phase != new.phase
        if (phaseChanged || keyOf(old ?: new) != newKey || old == null) silenceIO()

        when (new.phase) {
            Phase.ROUND_INTRO -> {
                voice = VoiceUi()
                presentationKey = null
                if (!resumed) sfx.play(Sfx.ROUND)
                speakHost(PresenterScript.roundIntro(new) + listOfNotNull(new.notice?.let { Speech(it, 0) }))
            }
            Phase.ASKING -> {
                val q = engine.currentQuestion(new) ?: return
                val player = new.currentPlayer ?: return
                val sameQuestionAfterUndo = old?.phase == Phase.REVEAL && keyOf(old) == newKey
                if (sameQuestionAfterUndo && !resumed) {
                    presentationKey = newKey
                    voice = VoiceUi(readingDone = true, message = new.notice)
                    speakHost(listOf(Speech(new.notice ?: "Resultado desfeito.", 0)))
                    return
                }
                if (!resumed) markQuestionUsed(q)
                presentationKey = newKey
                autoRetries = 0
                val intro = listOfNotNull(new.notice?.takeIf { old?.phase == Phase.ASKING }?.let { Speech(it, 300) })
                presentQuestion(new, q, player.name, intro, resumed)
            }
            Phase.REVEAL -> {
                presentationKey = null
                voice = VoiceUi(readingDone = true)
                val record = new.revealRecord ?: return
                val q = engine.question(record.questionId)
                when (record.outcome) {
                    Outcome.CORRECT -> if (!resumed) sfx.play(Sfx.CORRECT)
                    Outcome.WRONG -> if (!resumed) sfx.play(Sfx.WRONG)
                    else -> Unit
                }
                if (!resumed) {
                    val lines = PresenterScript.result(new, record, q) + listOfNotNull(new.notice?.let { Speech(it, 0) })
                    speakHost(lines, delayMs = 450)
                }
            }
            Phase.MATCH_END, Phase.GAME_OVER -> {
                presentationKey = null
                voice = VoiceUi()
                if (!resumed) {
                    if (new.finished) sfx.play(Sfx.VICTORY)
                    speakHost(endSpeech(new), delayMs = 400)
                }
                if (new.finished) saveSummary(new)
            }
        }
    }

    private fun endSpeech(state: GameState): List<Speech> {
        fun names(ids: List<String>) = ids.mapNotNull { state.player(it)?.name }.joinToString(" e ")
        val tie = state.tie
        return when {
            state.finished && state.winners.size == 1 -> listOf(Speech("Fim de jogo! Vitória de ${names(state.winners)}! Parabéns!", 0))
            state.finished -> listOf(Speech("Fim de jogo! Empate entre ${names(state.winners)}!", 0))
            tie != null -> listOf(Speech("Empate entre ${names(tie.playerIds)}! Vocês podem jogar uma pergunta de desempate.", 0))
            state.phase == Phase.MATCH_END -> {
                val last = state.matchWinners.lastOrNull().orEmpty()
                listOf(Speech(if (last.isEmpty()) "Partida empatada." else "Partida ${state.match} para ${names(last)}!", 0))
            }
            else -> emptyList()
        }
    }

    private fun saveSummary(state: GameState) {
        val summary = GameSummary(
            id = state.id,
            finishedAt = System.currentTimeMillis(),
            mode = state.config.mode.label,
            players = state.players.map { it.name },
            scores = state.players.map { state.totalScore(it.id) },
            winners = state.winners.mapNotNull { state.player(it)?.name },
        )
        viewModelScope.launch(ioWriter) {
            store.addSummary(summary)
            summaries = store.loadSummaries()
        }
    }

    private fun markQuestionUsed(q: Question) {
        val prev = questionHistory.entries[q.id]
        val entry = HistoryEntry(TextNormalizer.fingerprint(q.text), (prev?.timesUsed ?: 0) + 1, System.currentTimeMillis())
        questionHistory = questionHistory.copy(entries = questionHistory.entries + (q.id to entry))
        historyCount = questionHistory.entries.size
        val snapshot = questionHistory
        viewModelScope.launch(ioWriter) { store.saveHistory(snapshot) }
    }

    // ================================================================== leitura da pergunta

    private fun presentQuestion(state: GameState, q: Question, playerName: String, intro: List<Speech> = emptyList(), resumed: Boolean = false) {
        val key = keyOf(state)
        val voiceOn = state.config.voiceHost && ttsStatus == TtsStatus.READY
        if (!voiceOn) {
            val msg = when {
                !state.config.voiceHost -> null
                ttsStatus == TtsStatus.INITIALIZING -> "A voz ainda está carregando. Toque em Repetir para ouvir."
                else -> "Voz indisponível neste aparelho: leia a pergunta na tela e responda tocando."
            }
            voice = VoiceUi(readingDone = true, message = msg ?: if (resumed) "Partida retomada." else null)
            return
        }
        voice = VoiceUi(speaking = true, readingDone = false, message = if (resumed) "Partida retomada: lendo a pergunta de novo." else null)
        val parts = intro + PresenterScript.questionReading(playerName, q)
        host.speak(parts, settings.speechRate) { result ->
            if (presentationKey != key || game?.phase != Phase.ASKING) return@speak
            when (result) {
                SpeakResult.COMPLETED -> {
                    voice = voice.copy(speaking = false, readingDone = true)
                    if (shouldAutoListen()) scheduleListen()
                }
                SpeakResult.TIMEOUT, SpeakResult.ERROR -> voice = voice.copy(
                    speaking = false,
                    readingDone = true,
                    message = "Falha no áudio da pergunta. Use Repetir, ou Anular pergunta se ela foi interrompida.",
                )
                SpeakResult.UNAVAILABLE -> voice = voice.copy(speaking = false, readingDone = true)
            }
        }
    }

    private fun speakHost(parts: List<Speech>, delayMs: Long = 0, then: (() -> Unit)? = null) {
        val g = game ?: return
        if (!g.config.voiceHost || ttsStatus != TtsStatus.READY || parts.isEmpty()) {
            then?.invoke()
            return
        }
        val key = presentationKey
        val start = {
            voice = voice.copy(speaking = true)
            host.speak(parts, settings.speechRate) { result ->
                if (presentationKey != key) return@speak
                voice = voice.copy(speaking = false)
                if (result == SpeakResult.COMPLETED) then?.invoke()
            }
        }
        if (delayMs > 0) viewModelScope.launch { delay(delayMs); if (presentationKey == key) start() } else start()
    }

    /** Repetir: lê de novo a mesma pergunta. Não é resposta e não muda o placar. */
    fun repeatQuestion() {
        val g = game ?: return
        if (g.phase != Phase.ASKING) return
        dispatch(GameAction.Repeat)
        silenceIO()
        val q = engine.currentQuestion(g) ?: return
        presentationKey = keyOf(g)
        if (!g.config.voiceHost || ttsStatus != TtsStatus.READY) {
            voice = voice.copy(pending = null, message = "Voz desligada ou indisponível: leia a pergunta na tela.")
            return
        }
        presentQuestion(g, q, g.currentPlayer?.name ?: "")
    }

    // ================================================================== microfone

    private fun shouldAutoListen(): Boolean {
        val g = game ?: return false
        return g.config.voiceAnswers && settings.autoListen && settings.speechConsent == true && recognitionAvailable && hasMicPermission()
    }

    private fun hasMicPermission(): Boolean =
        ContextCompat.checkSelfPermission(getApplication(), Manifest.permission.RECORD_AUDIO) == PackageManager.PERMISSION_GRANTED

    private fun scheduleListen(confirmation: Boolean = false) {
        pendingListenJob?.cancel()
        pendingListenJob = viewModelScope.launch {
            delay(200)
            startListening(confirmation)
        }
    }

    /** Botão "Ouvir resposta". */
    fun listenForAnswer() {
        val g = game ?: return
        if (g.phase != Phase.ASKING) return
        if (!recognitionAvailable) {
            dialog = AppDialog.Message(
                "Sem reconhecimento de fala",
                "Este aparelho não tem um serviço de reconhecimento de fala. Respondam tocando nas alternativas.",
            )
            voice = voice.copy(touchMode = true, readingDone = true)
            return
        }
        when {
            settings.speechConsent != true -> { listenAfterPermission = true; dialog = AppDialog.SpeechConsent }
            !hasMicPermission() -> { listenAfterPermission = true; dialog = AppDialog.MicRationale }
            else -> {
                if (host.isSpeaking) host.stop()
                voice = voice.copy(speaking = false, readingDone = true)
                startListening(confirmation = voice.pending is Pending.Confirm || voice.pending is Pending.ConfirmSkip || voice.pending is Pending.ConfirmNoAnswer)
            }
        }
    }

    fun onSpeechConsent(accepted: Boolean) {
        dialog = null
        updateSettings { it.copy(speechConsent = accepted) }
        if (!accepted) {
            listenAfterPermission = false
            voice = voice.copy(touchMode = true, readingDone = true, message = "Respostas por toque. Você pode mudar isso em Configurações.")
            return
        }
        if (!hasMicPermission()) dialog = AppDialog.MicRationale else if (listenAfterPermission) listenForAnswer()
    }

    fun onMicRationaleAccepted() {
        dialog = null
        viewModelScope.launch { _events.emit(UiEvent.RequestMicPermission) }
    }

    fun onMicPermissionResult(granted: Boolean) {
        if (granted) {
            if (listenAfterPermission) {
                listenAfterPermission = false
                listenForAnswer()
            }
        } else {
            listenAfterPermission = false
            voice = voice.copy(touchMode = true, readingDone = true, message = "Sem permissão de microfone: respondam tocando na tela.")
        }
    }

    private fun startListening(confirmation: Boolean) {
        val g = game ?: return
        val key = keyOf(g)
        // O microfone só abre quando o jogo espera uma resposta e a leitura terminou.
        if (g.phase != Phase.ASKING || key == null || key != presentationKey || host.isSpeaking) return
        if (!voice.readingDone) return
        sfx.play(Sfx.MIC_ON)
        voice = voice.copy(listening = true, listeningForConfirmation = confirmation, partial = "", micLevel = 0f, message = null)
        viewModelScope.launch {
            delay(250) // deixa o "bip" terminar antes de ouvir
            if (presentationKey != key || game?.phase != Phase.ASKING) return@launch
            speech.start { event -> onSpeechEvent(event, key, confirmation) }
        }
    }

    /** Parar: encerra a escuta e avalia o que já foi dito. */
    fun stopListening() = speech.stop()

    /** Cancelar: descarta o que foi ouvido. */
    fun cancelListening() {
        speech.cancel()
        pendingListenJob?.cancel()
        voice = voice.copy(listening = false, partial = "", micLevel = 0f, message = "Escuta cancelada. Nada foi avaliado.")
    }

    private fun onSpeechEvent(event: SpeechEvent, key: String, confirmation: Boolean) {
        if (presentationKey != key || game?.phase != Phase.ASKING) {
            speech.cancel()
            return
        }
        when (event) {
            SpeechEvent.Ready -> Unit
            is SpeechEvent.Level -> voice = voice.copy(micLevel = event.value)
            is SpeechEvent.Partial -> voice = voice.copy(partial = event.text)
            is SpeechEvent.Results -> {
                sfx.play(Sfx.MIC_OFF)
                val heard = event.alternatives.firstOrNull()?.text.orEmpty()
                voice = voice.copy(listening = false, micLevel = 0f, partial = "", heard = heard)
                if (confirmation) handleYesNo(heard) else {
                    val q = engine.currentQuestion(game!!) ?: return
                    handleInterpretation(AnswerInterpreter.interpret(q, event.alternatives, settings.alwaysConfirmVoice), AnswerMethod.VOICE)
                }
            }
            is SpeechEvent.Failure -> {
                voice = voice.copy(
                    listening = false, micLevel = 0f, partial = "",
                    touchMode = voice.touchMode || event.serviceProblem,
                    message = if (event.silence) "Não ouvi nenhuma resposta. Nenhum ponto foi dado. Toque em Ouvir resposta, Repetir, Pular ou Encerrar a vez." else event.message,
                )
                if (event.silence) speakShort("Não ouvi resposta.")
            }
        }
    }

    private fun speakShort(text: String, then: (() -> Unit)? = null) = speakHost(listOf(Speech(text, 0)), then = then)

    private fun handleInterpretation(interp: Interpretation, method: AnswerMethod) {
        when (interp) {
            is Interpretation.Clear -> submit(interp.choice, method)
            is Interpretation.NeedsConfirmation -> {
                voice = voice.copy(pending = Pending.Confirm(interp.choice, interp.description, interp.reason, interp.heard, method), message = null)
                if (method == AnswerMethod.VOICE) {
                    speakHost(PresenterScript.confirmation(interp.description)) { if (shouldAutoListen()) scheduleListen(confirmation = true) }
                }
            }
            is Interpretation.Ambiguous -> {
                voice = voice.copy(pending = Pending.Clarify(interp.reason, interp.heard, interp.allowGroupDecision, method), message = null)
                if (method == AnswerMethod.VOICE) speakHost(PresenterScript.clarification(interp.reason))
            }
            is Interpretation.Unclear -> {
                voice = voice.copy(
                    message = if (interp.heard.isBlank()) "Não identifiquei uma resposta." else "Não identifiquei uma resposta em “${interp.heard}”. Fale de novo ou toque na alternativa.",
                )
                if (method == AnswerMethod.VOICE) {
                    val retry = autoRetries < 1 && shouldAutoListen()
                    autoRetries++
                    speakShort("Não entendi a resposta. Pode falar de novo?") { if (retry) scheduleListen() }
                }
            }
            is Interpretation.Command -> when (interp.kind) {
                CommandKind.REPEAT -> repeatQuestion()
                CommandKind.SKIP -> {
                    voice = voice.copy(pending = Pending.ConfirmSkip(interp.heard))
                    speakHost(listOf(Speech("Quer pular esta pergunta?", 0))) { if (shouldAutoListen()) scheduleListen(confirmation = true) }
                }
                CommandKind.DONT_KNOW -> {
                    voice = voice.copy(pending = Pending.ConfirmNoAnswer(interp.heard))
                    speakHost(listOf(Speech("Encerrar a vez sem ponto?", 0))) { if (shouldAutoListen()) scheduleListen(confirmation = true) }
                }
            }
        }
    }

    private fun handleYesNo(heard: String) {
        val words = TextNormalizer.tokens(heard).toSet()
        val yes = words.any { it in setOf("sim", "confirmo", "confirma", "isso", "correto", "exato", "claro", "pode", "certo") }
        val no = words.any { it in setOf("nao", "errado", "negativo", "cancela") }
        when {
            yes && !no -> resolvePending(true)
            no && !yes -> resolvePending(false)
            else -> voice = voice.copy(message = "Não entendi a confirmação (“$heard”). Toque em Sim ou Não.")
        }
    }

    /** Resposta do grupo a uma confirmação pendente. */
    fun resolvePending(yes: Boolean) {
        when (val p = voice.pending ?: return) {
            is Pending.Confirm -> if (yes) submit(p.choice, p.method) else {
                voice = voice.copy(pending = null, message = "Tudo bem: responda de novo, falando ou tocando.")
                if (p.method == AnswerMethod.VOICE) speakShort("Tudo bem, pode responder de novo.") { if (shouldAutoListen()) scheduleListen() }
            }
            is Pending.ConfirmSkip -> if (yes) dispatch(GameAction.Skip) else voice = voice.copy(pending = null)
            is Pending.ConfirmNoAnswer -> if (yes) dispatch(GameAction.NoAnswer) else voice = voice.copy(pending = null)
            is Pending.Clarify -> if (yes && p.allowGroupDecision) {
                voice = voice.copy(pending = Pending.GroupDecision(p.heard))
            } else {
                voice = voice.copy(pending = null)
            }
            is Pending.GroupDecision -> Unit
        }
    }

    fun groupDecision(correct: Boolean) {
        val p = voice.pending as? Pending.GroupDecision ?: return
        submit(AnswerChoice.Judged(p.text, correct), AnswerMethod.GROUP)
    }

    fun dismissPending() {
        voice = voice.copy(pending = null)
    }

    private fun submit(choice: AnswerChoice, method: AnswerMethod) {
        voice = voice.copy(pending = null)
        dispatch(GameAction.SubmitAnswer(choice, method))
    }

    // ================================================================== toque

    /** "Responder tocando": interrompe a fala e libera as alternativas. */
    fun answerByTouch() {
        if (game?.phase != Phase.ASKING) return
        silenceIO()
        voice = voice.copy(touchMode = true, readingDone = true, speaking = false, listening = false)
    }

    fun touchOption(index: Int) {
        val g = game ?: return
        if (g.phase != Phase.ASKING || voice.listening || voice.pending != null) return
        if (!voice.readingDone && !voice.touchMode) return
        sfx.play(Sfx.SELECT)
        silenceIO()
        submit(AnswerChoice.Option(index), AnswerMethod.TOUCH)
    }

    fun typedAnswer(text: String) {
        val g = game ?: return
        if (g.phase != Phase.ASKING || text.isBlank()) return
        val q = engine.currentQuestion(g) ?: return
        silenceIO()
        handleInterpretation(AnswerInterpreter.interpretTyped(q, text), AnswerMethod.TYPED)
    }

    // ================================================================== ciclo de vida

    /** Para fala e microfone imediatamente (sem disparar retornos pendentes). */
    private fun silenceIO() {
        pendingListenJob?.cancel()
        host.stop()
        speech.cancel()
        if (voice.listening || voice.speaking) voice = voice.copy(listening = false, speaking = false, micLevel = 0f, partial = "")
    }

    /** App foi para segundo plano: nada de microfone aberto; o estado já está salvo. */
    fun onAppPaused() {
        val wasReading = voice.speaking && !voice.readingDone
        silenceIO()
        if (game?.phase == Phase.ASKING && wasReading) {
            voice = voice.copy(message = "Leitura interrompida. Toque em Repetir para ouvir de novo.")
        }
    }

    override fun onCleared() {
        host.shutdown()
        speech.destroy()
        sfx.release()
    }

    fun tiebreakHits(state: GameState, playerId: String): Int =
        state.log.count { it.kind == RoundKind.TIEBREAK && it.playerId == playerId && !it.undone && it.outcome == Outcome.CORRECT }
}
