package br.com.perguntaloei

import android.app.Application
import android.os.Looper
import androidx.test.core.app.ApplicationProvider
import androidx.test.ext.junit.runners.AndroidJUnit4
import br.com.perguntaloei.game.Speech
import br.com.perguntaloei.voice.NeuralSpeaker
import br.com.perguntaloei.voice.PcmPlayer
import br.com.perguntaloei.voice.SpeakResult
import br.com.perguntaloei.voice.Synth
import br.com.perguntaloei.voice.TtsStatus
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.Shadows.shadowOf
import org.robolectric.annotation.Config
import java.io.File
import java.util.Collections

/** Lógica da voz neural (fila, ordem, interrupção, aviso de fim) com síntese e som falsos. */
@RunWith(AndroidJUnit4::class)
@Config(sdk = [34])
class NeuralSpeakerTest {

    private val app: Application = ApplicationProvider.getApplicationContext()

    /** Síntese falsa: devolve um "áudio" cujo primeiro valor identifica o texto. */
    private class FakeSynth : Synth {
        val generated: MutableList<String> = Collections.synchronizedList(mutableListOf())
        override val sampleRate = 22050
        override fun generate(text: String, speed: Float): FloatArray {
            generated += text
            Thread.sleep(15)
            return FloatArray(100) { text.hashCode().toFloat() }
        }
        override fun release() = Unit
    }

    /** Som falso: registra o que tocou, demorando um pouco, e respeita a interrupção. */
    private class FakePlayer(private val millis: Long = 40) : PcmPlayer {
        val played: MutableList<Float> = Collections.synchronizedList(mutableListOf())
        override fun play(samples: FloatArray, sampleRate: Int, stillValid: () -> Boolean) {
            val end = System.currentTimeMillis() + millis
            while (System.currentTimeMillis() < end) {
                if (!stillValid()) return
                Thread.sleep(5)
            }
            played += samples[0]
        }
    }

    private fun waitUntil(timeoutMs: Long = 5000, cond: () -> Boolean) {
        val end = System.currentTimeMillis() + timeoutMs
        while (!cond() && System.currentTimeMillis() < end) {
            shadowOf(Looper.getMainLooper()).idle()
            Thread.sleep(10)
        }
        shadowOf(Looper.getMainLooper()).idle()
    }

    private fun ready(synth: Synth, player: PcmPlayer): NeuralSpeaker {
        var status: TtsStatus? = null
        val speaker = NeuralSpeaker(app, File(app.filesDir, "voz-teste"), { status = it }, { synth }, player)
        waitUntil { status != null }
        assertEquals(TtsStatus.READY, status)
        return speaker
    }

    @Test
    fun speaksAllPartsInOrderAndSignalsTheEndOnce() {
        val synth = FakeSynth()
        val player = FakePlayer()
        val speaker = ready(synth, player)
        val parts = listOf(Speech("Vez de Paula!", 10), Speech("Qual é a capital do Brasil?", 10), Speech("A, Brasília.", 0))
        val results = mutableListOf<SpeakResult>()
        speaker.speak(parts, 1f) { results += it }
        assertTrue(speaker.isSpeaking)
        waitUntil { results.isNotEmpty() }
        Thread.sleep(100)
        shadowOf(Looper.getMainLooper()).idle()
        assertEquals(listOf(SpeakResult.COMPLETED), results)
        assertEquals(parts.map { it.text.hashCode().toFloat() }, player.played.toList())
        assertTrue(!speaker.isSpeaking)
    }

    @Test
    fun theEndIsSignalledOnlyAfterTheLastSoundFinishes() {
        val player = FakePlayer(millis = 300)
        val speaker = ready(FakeSynth(), player)
        var done = false
        speaker.speak(listOf(Speech("Pergunta longa.", 0)), 1f) { done = true }
        Thread.sleep(150)
        shadowOf(Looper.getMainLooper()).idle()
        assertTrue("não pode avisar fim com som tocando", !done)
        waitUntil { done }
        assertTrue(done)
        assertEquals(1, player.played.size)
    }

    @Test
    fun stoppingInterruptsAndNeverSignalsTheEnd() {
        val player = FakePlayer(millis = 200)
        val speaker = ready(FakeSynth(), player)
        val results = mutableListOf<SpeakResult>()
        speaker.speak(listOf(Speech("Um.", 0), Speech("Dois.", 0), Speech("Três.", 0)), 1f) { results += it }
        Thread.sleep(80)
        speaker.stop()
        waitUntil(800) { false }
        assertTrue("fala interrompida não avisa fim", results.isEmpty())
        assertTrue("parou antes do fim", player.played.size < 3)
        assertTrue(!speaker.isSpeaking)
    }

    @Test
    fun aNewReadingReplacesTheOldOne() {
        val player = FakePlayer(millis = 100)
        val speaker = ready(FakeSynth(), player)
        val first = mutableListOf<SpeakResult>()
        val second = mutableListOf<SpeakResult>()
        speaker.speak(listOf(Speech("Antiga um.", 0), Speech("Antiga dois.", 0)), 1f) { first += it }
        Thread.sleep(30)
        speaker.speak(listOf(Speech("Nova.", 0)), 1f) { second += it }
        waitUntil { second.isNotEmpty() }
        assertTrue(first.isEmpty())
        assertEquals(listOf(SpeakResult.COMPLETED), second)
        assertEquals("Nova.".hashCode().toFloat(), player.played.last())
    }

    @Test
    fun aBrokenModelReportsUnavailableInsteadOfCrashing() {
        var status: TtsStatus? = null
        val speaker = NeuralSpeaker(app, File(app.filesDir, "voz-teste"), { status = it }, { error("sem biblioteca nativa") }, FakePlayer())
        waitUntil { status != null }
        assertEquals(TtsStatus.UNAVAILABLE, status)
        var result: SpeakResult? = null
        speaker.speak(listOf(Speech("Oi.", 0)), 1f) { result = it }
        assertEquals(SpeakResult.UNAVAILABLE, result)
    }
}
