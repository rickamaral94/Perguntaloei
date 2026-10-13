package br.com.perguntaloei.audio

import android.media.AudioAttributes
import android.media.AudioFormat
import android.media.AudioTrack
import java.util.concurrent.Executors
import kotlin.math.PI
import kotlin.math.sin

enum class Sfx { SELECT, ROUND, CORRECT, WRONG, MIC_ON, MIC_OFF, VICTORY }

/**
 * Efeitos sonoros originais estilo 8 bits, sintetizados no próprio app
 * (ondas quadradas com envelope curto). Volume baixo para não atrapalhar a conversa.
 */
class SoundFx {

    private val rate = 22050
    private val executor = Executors.newSingleThreadExecutor()
    private val cache = HashMap<Sfx, ShortArray>()
    @Volatile var enabled = true

    private data class Note(val freq: Double, val ms: Int, val duty: Double = 0.5)

    private fun melody(sfx: Sfx): List<Note> = when (sfx) {
        Sfx.SELECT -> listOf(Note(880.0, 40), Note(1320.0, 40))
        Sfx.ROUND -> listOf(Note(392.0, 90), Note(523.3, 90), Note(659.3, 90), Note(784.0, 180, 0.25))
        Sfx.CORRECT -> listOf(Note(523.3, 70), Note(659.3, 70), Note(784.0, 70), Note(1046.5, 160, 0.25))
        Sfx.WRONG -> listOf(Note(311.1, 140, 0.25), Note(233.1, 260, 0.25))
        Sfx.MIC_ON -> listOf(Note(660.0, 50), Note(990.0, 70))
        Sfx.MIC_OFF -> listOf(Note(990.0, 50), Note(660.0, 70))
        Sfx.VICTORY -> listOf(
            Note(523.3, 100), Note(523.3, 100), Note(523.3, 100), Note(659.3, 220),
            Note(587.3, 100), Note(659.3, 100), Note(784.0, 360, 0.25),
        )
    }

    private fun render(notes: List<Note>): ShortArray {
        val total = notes.sumOf { it.ms } * rate / 1000
        val out = ShortArray(total)
        var pos = 0
        for (n in notes) {
            val len = n.ms * rate / 1000
            val period = rate / n.freq
            for (i in 0 until len) {
                val phase = (i % period) / period
                val square = if (phase < n.duty) 1.0 else -1.0
                // Envelope: ataque rápido e queda suave, evitando estalos.
                val attack = (i / (rate * 0.004)).coerceAtMost(1.0)
                val release = ((len - i) / (rate * 0.02)).coerceAtMost(1.0)
                val sample = square * 0.18 * attack * release + 0.02 * sin(2 * PI * n.freq * i / rate)
                if (pos + i < out.size) out[pos + i] = (sample * Short.MAX_VALUE).toInt().toShort()
            }
            pos += len
        }
        return out
    }

    fun play(sfx: Sfx) {
        if (!enabled) return
        executor.execute {
            runCatching {
                val pcm = cache.getOrPut(sfx) { render(melody(sfx)) }
                val track = AudioTrack.Builder()
                    .setAudioAttributes(
                        AudioAttributes.Builder()
                            .setUsage(AudioAttributes.USAGE_GAME)
                            .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
                            .build(),
                    )
                    .setAudioFormat(
                        AudioFormat.Builder()
                            .setEncoding(AudioFormat.ENCODING_PCM_16BIT)
                            .setSampleRate(rate)
                            .setChannelMask(AudioFormat.CHANNEL_OUT_MONO)
                            .build(),
                    )
                    .setTransferMode(AudioTrack.MODE_STATIC)
                    .setBufferSizeInBytes(pcm.size * 2)
                    .build()
                track.write(pcm, 0, pcm.size)
                track.play()
                Thread.sleep(pcm.size * 1000L / rate + 60)
                track.release()
            }
        }
    }

    fun release() {
        executor.shutdownNow()
    }
}
