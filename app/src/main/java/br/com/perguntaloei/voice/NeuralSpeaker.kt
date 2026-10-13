package br.com.perguntaloei.voice

import android.content.Context
import android.content.Intent
import android.media.AudioAttributes
import android.media.AudioFormat
import android.media.AudioTrack
import android.os.Handler
import android.os.Looper
import android.speech.tts.TextToSpeech
import br.com.perguntaloei.game.Speech
import com.k2fsa.sherpa.onnx.OfflineTts
import com.k2fsa.sherpa.onnx.OfflineTtsConfig
import com.k2fsa.sherpa.onnx.OfflineTtsModelConfig
import com.k2fsa.sherpa.onnx.OfflineTtsVitsModelConfig
import java.io.File
import java.util.concurrent.ExecutorService
import java.util.concurrent.Executors
import java.util.concurrent.Future
import java.util.concurrent.atomic.AtomicInteger

/**
 * Voz neural embutida no app (modelo Piper "faber", pt-BR, via sherpa-onnx). Roda 100% no
 * aparelho, sem internet. Cada trecho é sintetizado em segundo plano — o próximo já é
 * preparado enquanto o atual toca — e o aviso de fim só vem quando o último som termina de
 * tocar, para o microfone nunca abrir durante a leitura.
 */
/** Gera áudio a partir de texto (no app: modelo Piper via sherpa-onnx). */
interface Synth {
    val sampleRate: Int
    fun generate(text: String, speed: Float): FloatArray
    fun release()
}

/** Toca amostras e só retorna quando terminaram de tocar (ou [stillValid] virou falso). */
fun interface PcmPlayer {
    fun play(samples: FloatArray, sampleRate: Int, stillValid: () -> Boolean)
}

class NeuralSpeaker(
    context: Context,
    private val onStatus: (TtsStatus) -> Unit,
    private val synthFactory: (Context) -> Synth = ::sherpaSynth,
    private val player: PcmPlayer = AudioTrackPlayer,
) : Speaker {

    private val app = context.applicationContext
    private val main = Handler(Looper.getMainLooper())
    private val synthThread: ExecutorService = Executors.newSingleThreadExecutor { Thread(it, "voz-neural-sintese") }
    private val playThread: ExecutorService = Executors.newSingleThreadExecutor { Thread(it, "voz-neural-som") }
    private val token = AtomicInteger(0)

    @Volatile private var tts: Synth? = null
    private var pending: List<Future<FloatArray?>> = emptyList()

    @Volatile override var status: TtsStatus = TtsStatus.INITIALIZING
        private set
    @Volatile override var isSpeaking: Boolean = false
        private set
    override val engine: String = ENGINE_ID
    override val currentVoice: String = VOICE_NAME

    init {
        synthThread.execute {
            val result = runCatching {
                tts = synthFactory(app)
                // Aquece o modelo para a primeira pergunta sair sem atraso.
                tts?.generate("Olá.", 1.0f)
            }
            val s = if (result.isSuccess && tts != null) TtsStatus.READY else TtsStatus.UNAVAILABLE
            main.post {
                status = s
                onStatus(s)
            }
        }
    }

    override fun engines(): List<EngineOption> = systemEngines(app)


    override fun voices(): List<VoiceOption> =
        listOf(VoiceOption(VOICE_NAME, "Voz neural embutida (faber, Brasil) · offline", 500, needsNetwork = false, installed = true))

    override fun selectVoice(name: String?, allowNetwork: Boolean): String = VOICE_NAME

    override fun speak(parts: List<Speech>, rate: Float, onDone: (SpeakResult) -> Unit) {
        stopPlayback()
        val engine = tts
        if (status != TtsStatus.READY || engine == null || parts.isEmpty()) {
            onDone(if (parts.isEmpty()) SpeakResult.COMPLETED else SpeakResult.UNAVAILABLE)
            return
        }
        val t = token.incrementAndGet()
        isSpeaking = true
        val speed = rate.coerceIn(0.6f, 1.6f)
        // Todos os trechos entram na fila de síntese; o som toca na ordem, assim que cada um fica pronto.
        val futures = parts.map { part ->
            synthThread.submit<FloatArray?> {
                if (token.get() != t || part.text.isBlank()) null else engine.generate(part.text, speed)
            }
        }
        pending = futures
        val sampleRate = engine.sampleRate
        playThread.execute {
            val result = runCatching {
                for ((i, part) in parts.withIndex()) {
                    if (token.get() != t) return@runCatching SpeakResult.ERROR
                    val samples = futures[i].get()
                    if (token.get() != t) return@runCatching SpeakResult.ERROR
                    if (samples != null && samples.isNotEmpty()) player.play(samples, sampleRate) { token.get() == t }
                    if (part.pauseAfterMs > 0 && token.get() == t) Thread.sleep(part.pauseAfterMs)
                }
                SpeakResult.COMPLETED
            }.getOrElse { SpeakResult.ERROR }
            main.post {
                // Leitura interrompida (stop ou nova fala): não avisa nada.
                if (token.get() != t) return@post
                isSpeaking = false
                onDone(result)
            }
        }
    }

    private fun stopPlayback() {
        token.incrementAndGet()
        pending.forEach { it.cancel(false) }
        pending = emptyList()
        isSpeaking = false
    }

    override fun stop() = stopPlayback()

    override fun shutdown() {
        stopPlayback()
        synthThread.execute { tts?.release(); tts = null }
        synthThread.shutdown()
        playThread.shutdownNow()
    }

    companion object {
        const val ENGINE_ID = "perguntaloei.voz-neural"
        const val VOICE_NAME = "neural-pt-br-faber"
        const val ASSET_DIR = "tts"
        const val MODEL_FILE = "pt_BR-faber-medium.onnx"
        private const val DATA_VERSION = 1

        /** O espeak-ng precisa dos dados de fonética como pasta de verdade: copia dos assets uma vez. */
        fun copyPhonemeData(app: Context): File {
            val target = File(app.filesDir, "voz-neural/espeak-ng-data-$DATA_VERSION")
            val marker = File(target, ".ok")
            if (marker.exists()) return target
            target.deleteRecursively()
            fun copy(assetPath: String, dest: File) {
                val children = app.assets.list(assetPath).orEmpty()
                if (children.isEmpty()) {
                    dest.parentFile?.mkdirs()
                    app.assets.open(assetPath).use { input -> dest.outputStream().use { input.copyTo(it) } }
                } else {
                    dest.mkdirs()
                    children.forEach { copy("$assetPath/$it", File(dest, it)) }
                }
            }
            copy("$ASSET_DIR/espeak-ng-data", target)
            marker.writeText("ok")
            return target
        }

        /** Mecanismos de voz do sistema instalados (Google, Samsung...). */
        fun systemEngines(context: Context): List<EngineOption> = runCatching {
            val pm = context.packageManager
            pm.queryIntentServices(Intent(TextToSpeech.Engine.INTENT_ACTION_TTS_SERVICE), 0).map {
                EngineOption(it.serviceInfo.packageName, it.loadLabel(pm).toString())
            }.distinctBy { it.packageName }
        }.getOrDefault(emptyList())

        /** O app tem o modelo e a biblioteca nativa para este aparelho? */
        fun isSupported(): Boolean =
            android.os.Build.SUPPORTED_ABIS.any { it == "arm64-v8a" || it == "armeabi-v7a" }
    }
}

/** Síntese real: modelo Piper pt-BR "faber" lido dos assets pelo sherpa-onnx. */
private fun sherpaSynth(app: Context): Synth {
    val dataDir = NeuralSpeaker.copyPhonemeData(app)
    val config = OfflineTtsConfig(
        model = OfflineTtsModelConfig(
            vits = OfflineTtsVitsModelConfig(
                model = "${NeuralSpeaker.ASSET_DIR}/${NeuralSpeaker.MODEL_FILE}",
                tokens = "${NeuralSpeaker.ASSET_DIR}/tokens.txt",
                dataDir = dataDir.absolutePath,
                noiseScale = 0.667f,
                noiseScaleW = 0.8f,
                lengthScale = 1.0f,
            ),
            numThreads = (Runtime.getRuntime().availableProcessors() / 2).coerceIn(1, 4),
            debug = false,
            provider = "cpu",
        ),
    )
    val tts = OfflineTts(app.assets, config)
    return object : Synth {
        override val sampleRate: Int = tts.sampleRate()
        override fun generate(text: String, speed: Float): FloatArray = tts.generate(text, 0, speed).samples
        override fun release() = tts.release()
    }
}

/** Saída de som pelo AudioTrack; espera o último som sair do alto-falante. */
private object AudioTrackPlayer : PcmPlayer {
    override fun play(samples: FloatArray, sampleRate: Int, stillValid: () -> Boolean) {
        val minBuf = AudioTrack.getMinBufferSize(sampleRate, AudioFormat.CHANNEL_OUT_MONO, AudioFormat.ENCODING_PCM_FLOAT)
        val audio = AudioTrack.Builder()
            .setAudioAttributes(
                AudioAttributes.Builder()
                    .setUsage(AudioAttributes.USAGE_MEDIA)
                    .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
                    .build(),
            )
            .setAudioFormat(
                AudioFormat.Builder()
                    .setEncoding(AudioFormat.ENCODING_PCM_FLOAT)
                    .setSampleRate(sampleRate)
                    .setChannelMask(AudioFormat.CHANNEL_OUT_MONO)
                    .build(),
            )
            .setTransferMode(AudioTrack.MODE_STREAM)
            .setBufferSizeInBytes(maxOf(minBuf, sampleRate))
            .build()
        try {
            audio.play()
            var offset = 0
            val chunk = sampleRate / 10
            while (offset < samples.size && stillValid()) {
                val n = minOf(chunk, samples.size - offset)
                audio.write(samples, offset, n, AudioTrack.WRITE_BLOCKING)
                offset += n
            }
            // Espera o som que ainda está no buffer terminar de tocar (ou a fala ser interrompida).
            val deadline = System.currentTimeMillis() + 3000 + samples.size * 1000L / sampleRate
            while (stillValid() && audio.playbackHeadPosition < samples.size && System.currentTimeMillis() < deadline) {
                Thread.sleep(20)
            }
            if (!stillValid()) runCatching { audio.pause(); audio.flush() }
        } finally {
            runCatching { audio.stop() }
            audio.release()
        }
    }
}
