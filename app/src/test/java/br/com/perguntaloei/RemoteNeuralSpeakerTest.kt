package br.com.perguntaloei

import android.app.Application
import android.content.ComponentName
import android.content.Intent
import android.content.ServiceConnection
import android.os.Looper
import androidx.test.core.app.ApplicationProvider
import androidx.test.ext.junit.runners.AndroidJUnit4
import br.com.perguntaloei.game.Speech
import br.com.perguntaloei.voice.NeuralVoiceService
import br.com.perguntaloei.voice.PcmPlayer
import br.com.perguntaloei.voice.RemoteNeuralSpeaker
import br.com.perguntaloei.voice.SpeakResult
import br.com.perguntaloei.voice.Synth
import br.com.perguntaloei.voice.TtsStatus
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.Robolectric
import org.robolectric.Shadows.shadowOf
import org.robolectric.annotation.Config
import java.io.File
import java.time.Duration
import java.util.Collections

/** Voz neural em processo separado: protocolo de mensagens, fim da fala, falhas e prazos. */
@RunWith(AndroidJUnit4::class)
@Config(sdk = [34])
class RemoteNeuralSpeakerTest {

    private val app: Application = ApplicationProvider.getApplicationContext()
    private val played: MutableList<String> = Collections.synchronizedList(mutableListOf())
    private val texts = HashMap<Float, String>()

    private inner class FakeSynth : Synth {
        override val sampleRate = 22050
        override fun generate(text: String, speed: Float): FloatArray {
            val key = text.hashCode().toFloat()
            synchronized(texts) { texts[key] = text }
            return FloatArray(10) { key }
        }
        override fun release() = Unit
    }

    private fun player(millis: Long) = PcmPlayer { samples, _, stillValid ->
        val end = System.currentTimeMillis() + millis
        while (System.currentTimeMillis() < end) {
            if (!stillValid()) return@PcmPlayer
            Thread.sleep(5)
        }
        synchronized(texts) { played += texts[samples[0]] ?: "?" }
    }

    @After
    fun reset() {
        NeuralVoiceService.synthFactoryForTests = null
        NeuralVoiceService.playerForTests = null
    }

    private fun idle() = shadowOf(Looper.getMainLooper()).idle()

    private fun waitUntil(timeoutMs: Long = 5000, cond: () -> Boolean) {
        val end = System.currentTimeMillis() + timeoutMs
        while (!cond() && System.currentTimeMillis() < end) {
            idle()
            Thread.sleep(10)
        }
        idle()
    }

    private val intent = Intent().putExtra(NeuralVoiceService.EXTRA_DIR, "/nao/importa")
    private var connection: ServiceConnection? = null
    private var unbinds = 0

    /** Liga o cliente ao serviço no mesmo processo (no app, é outro processo via bindService). */
    private fun connect(
        synth: () -> Synth = { FakeSynth() },
        playMillis: Long = 30,
        loadTimeoutMs: Long = 45_000,
        connects: Boolean = true,
        statuses: MutableList<TtsStatus> = mutableListOf(),
    ): RemoteNeuralSpeaker {
        NeuralVoiceService.synthFactoryForTests = { synth() }
        NeuralVoiceService.playerForTests = player(playMillis)
        val service = Robolectric.buildService(NeuralVoiceService::class.java, intent).create().get()
        return RemoteNeuralSpeaker(
            app, File("/nao/importa"), { statuses += it }, loadTimeoutMs,
            bind = { c ->
                connection = c
                if (connects) c.onServiceConnected(ComponentName(app, NeuralVoiceService::class.java), service.onBind(intent))
                true
            },
            unbind = { unbinds++; service.onUnbind(intent) },
        )
    }

    @Test
    fun loadsInTheVoiceProcessAndSpeaksEverythingBeforeSignallingTheEnd() {
        val statuses = mutableListOf<TtsStatus>()
        val speaker = connect(statuses = statuses)
        waitUntil { statuses.isNotEmpty() }
        assertEquals(listOf(TtsStatus.READY), statuses)
        assertEquals(TtsStatus.READY, speaker.status)

        val results = mutableListOf<SpeakResult>()
        speaker.speak(listOf(Speech("Vez de Paula!", 0), Speech("Qual é a capital?", 0), Speech("A, Brasília.", 0)), 1f) { results += it }
        assertTrue(speaker.isSpeaking)
        waitUntil { results.isNotEmpty() }
        assertEquals(listOf(SpeakResult.COMPLETED), results)
        assertEquals(listOf("Vez de Paula!", "Qual é a capital?", "A, Brasília."), played.toList())
        assertTrue(!speaker.isSpeaking)
    }

    @Test
    fun stopNeverSignalsTheEnd() {
        val statuses = mutableListOf<TtsStatus>()
        val speaker = connect(playMillis = 200, statuses = statuses)
        waitUntil { statuses.isNotEmpty() }
        val results = mutableListOf<SpeakResult>()
        speaker.speak(listOf(Speech("Um.", 0), Speech("Dois.", 0)), 1f) { results += it }
        Thread.sleep(50)
        speaker.stop()
        waitUntil(700) { false }
        assertTrue(results.isEmpty())
        assertTrue(played.size < 2)
    }

    @Test
    fun ifTheVoiceProcessDiesTheReadingEndsWithErrorAndTheVoiceBecomesUnavailable() {
        val statuses = mutableListOf<TtsStatus>()
        val speaker = connect(playMillis = 2000, statuses = statuses)
        waitUntil { statuses.isNotEmpty() }
        val results = mutableListOf<SpeakResult>()
        speaker.speak(listOf(Speech("Pergunta.", 0)), 1f) { results += it }
        connection!!.onServiceDisconnected(ComponentName(app, NeuralVoiceService::class.java))
        idle()
        assertEquals(listOf(SpeakResult.ERROR), results)
        assertEquals(listOf(TtsStatus.READY, TtsStatus.UNAVAILABLE), statuses)
        assertEquals(1, unbinds)
        var after: SpeakResult? = null
        speaker.speak(listOf(Speech("Oi.", 0)), 1f) { after = it }
        assertEquals(SpeakResult.UNAVAILABLE, after)
    }

    @Test
    fun aVoiceThatNeverLoadsGivesUpAfterTheTimeLimit() {
        val statuses = mutableListOf<TtsStatus>()
        connect(connects = false, loadTimeoutMs = 10_000, statuses = statuses)
        shadowOf(Looper.getMainLooper()).idleFor(Duration.ofSeconds(9))
        assertTrue(statuses.isEmpty())
        shadowOf(Looper.getMainLooper()).idleFor(Duration.ofSeconds(2))
        assertEquals(listOf(TtsStatus.UNAVAILABLE), statuses)
    }

    @Test
    fun aBrokenModelIsReportedAsUnavailable() {
        val statuses = mutableListOf<TtsStatus>()
        connect(synth = { error("sem biblioteca nativa") }, statuses = statuses)
        waitUntil { statuses.isNotEmpty() }
        assertEquals(listOf(TtsStatus.UNAVAILABLE), statuses)
    }

    @Test
    fun aReadingThatHangsEndsWithErrorInsteadOfBlockingTheGame() {
        val statuses = mutableListOf<TtsStatus>()
        val speaker = connect(playMillis = 600_000, statuses = statuses)
        waitUntil { statuses.isNotEmpty() }
        val results = mutableListOf<SpeakResult>()
        speaker.speak(listOf(Speech("Pergunta curta.", 0)), 1f) { results += it }
        shadowOf(Looper.getMainLooper()).idleFor(Duration.ofSeconds(10))
        assertTrue(results.isEmpty())
        shadowOf(Looper.getMainLooper()).idleFor(Duration.ofSeconds(30))
        assertEquals(listOf(SpeakResult.ERROR), results)
        assertEquals(TtsStatus.UNAVAILABLE, statuses.last())
    }
}
