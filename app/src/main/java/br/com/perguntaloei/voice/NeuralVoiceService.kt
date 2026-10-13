package br.com.perguntaloei.voice

import android.app.Service
import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.content.ServiceConnection
import android.os.Bundle
import android.os.Handler
import android.os.IBinder
import android.os.Looper
import android.os.Message
import android.os.Messenger
import androidx.annotation.VisibleForTesting
import br.com.perguntaloei.game.Speech
import java.io.File

/**
 * Roda a voz neural num processo separado (":voz", ver AndroidManifest).
 *
 * O modelo neural é pesado (memória e CPU) e usa código nativo. Isolado em outro processo, um
 * travamento, falta de memória ou falha nativa da voz nunca congela a tela do jogo: o app só
 * perde a conexão e volta para a voz padrão.
 */
class NeuralVoiceService : Service() {

    private var speaker: NeuralSpeaker? = null
    private var client: Messenger? = null
    private var status: TtsStatus = TtsStatus.INITIALIZING

    private val messenger = Messenger(Handler(Looper.getMainLooper()) { handle(it); true })

    override fun onBind(intent: Intent): IBinder {
        if (speaker == null) {
            val dir = File(intent.getStringExtra(EXTRA_DIR).orEmpty())
            val onStatus: (TtsStatus) -> Unit = { s ->
                status = s
                reply(Message.obtain(null, MSG_STATUS, s.ordinal, 0))
            }
            val synth = synthFactoryForTests
            speaker = if (synth != null) {
                NeuralSpeaker(this, dir, onStatus, { synth(dir) }, playerForTests ?: PcmPlayer { _, _, _ -> })
            } else {
                NeuralSpeaker(this, dir, onStatus)
            }
        }
        return messenger.binder
    }

    private fun handle(msg: Message) {
        val s = speaker ?: return
        when (msg.what) {
            MSG_REGISTER -> {
                client = msg.replyTo
                if (status != TtsStatus.INITIALIZING) reply(Message.obtain(null, MSG_STATUS, status.ordinal, 0))
            }
            MSG_SPEAK -> {
                val id = msg.arg1
                val data = msg.data
                val texts = data.getStringArray(KEY_TEXTS).orEmpty()
                val pauses = data.getLongArray(KEY_PAUSES) ?: LongArray(texts.size)
                val parts = texts.mapIndexed { i, t -> Speech(t, pauses.getOrElse(i) { 0L }) }
                s.speak(parts, data.getFloat(KEY_RATE, 1f)) { result ->
                    reply(Message.obtain(null, MSG_DONE, id, result.ordinal))
                }
            }
            MSG_STOP -> s.stop()
        }
    }

    private fun reply(msg: Message) {
        runCatching { client?.send(msg) }
    }

    override fun onUnbind(intent: Intent?): Boolean {
        release()
        stopSelf()
        return false
    }

    override fun onDestroy() {
        release()
        super.onDestroy()
    }

    private fun release() {
        speaker?.shutdown()
        speaker = null
        client = null
        status = TtsStatus.INITIALIZING
    }

    companion object {
        const val EXTRA_DIR = "dir"
        const val MSG_REGISTER = 1
        const val MSG_SPEAK = 2
        const val MSG_STOP = 3
        const val MSG_STATUS = 10
        const val MSG_DONE = 11
        const val KEY_TEXTS = "texts"
        const val KEY_PAUSES = "pauses"
        const val KEY_RATE = "rate"

        @VisibleForTesting var synthFactoryForTests: ((File) -> Synth)? = null
        @VisibleForTesting var playerForTests: PcmPlayer? = null
    }
}

/**
 * O apresentador com voz neural, visto pelo jogo. Só conversa por mensagens com
 * [NeuralVoiceService]; nada da voz neural roda no processo da tela.
 *
 * Se o processo da voz morrer, não carregar a tempo ou parar de responder no meio de uma fala,
 * a fala em andamento termina com erro e o status vira [TtsStatus.UNAVAILABLE], e o jogo volta
 * para a voz padrão.
 */
class RemoteNeuralSpeaker(
    context: Context,
    modelDir: File,
    private val onStatus: (TtsStatus) -> Unit,
    private val loadTimeoutMs: Long = 45_000,
    bind: ((ServiceConnection) -> Boolean)? = null,
    private val unbind: ((ServiceConnection) -> Unit)? = null,
) : Speaker {

    private val app = context.applicationContext
    private val main = Handler(Looper.getMainLooper())
    private val replies = Messenger(Handler(Looper.getMainLooper()) { onReply(it); true })
    private var service: Messenger? = null
    private var bound = false
    private var ended = false

    override var status: TtsStatus = TtsStatus.INITIALIZING
        private set
    override var isSpeaking: Boolean = false
        private set
    override val engine: String = NeuralSpeaker.ENGINE_ID
    override val currentVoice: String = NeuralSpeaker.VOICE_NAME

    private var nextId = 0
    private var currentId = -1
    private var currentDone: ((SpeakResult) -> Unit)? = null

    private val connection = object : ServiceConnection {
        override fun onServiceConnected(name: ComponentName?, binder: IBinder?) {
            if (ended || binder == null) return
            service = Messenger(binder)
            send(Message.obtain(null, NeuralVoiceService.MSG_REGISTER).apply { replyTo = replies })
        }

        // O processo da voz morreu (falta de memória, falha nativa...).
        override fun onServiceDisconnected(name: ComponentName?) = fail()
        override fun onBindingDied(name: ComponentName?) = fail()
        override fun onNullBinding(name: ComponentName?) = fail()
    }

    private val loadTimeout = Runnable { if (status == TtsStatus.INITIALIZING) fail() }
    private val speechTimeout = Runnable { if (isSpeaking) fail() }

    init {
        val doBind = bind ?: { c ->
            app.bindService(
                Intent(app, NeuralVoiceService::class.java).putExtra(NeuralVoiceService.EXTRA_DIR, modelDir.absolutePath),
                c, Context.BIND_AUTO_CREATE,
            )
        }
        bound = runCatching { doBind(connection) }.getOrDefault(false)
        if (bound) main.postDelayed(loadTimeout, loadTimeoutMs) else main.post { fail() }
    }

    private fun onReply(msg: Message) {
        if (ended) return
        when (msg.what) {
            NeuralVoiceService.MSG_STATUS -> {
                val s = TtsStatus.entries.getOrElse(msg.arg1) { TtsStatus.UNAVAILABLE }
                if (s == TtsStatus.UNAVAILABLE) return fail()
                main.removeCallbacks(loadTimeout)
                status = s
                onStatus(s)
            }
            NeuralVoiceService.MSG_DONE -> {
                if (msg.arg1 != currentId) return
                main.removeCallbacks(speechTimeout)
                val done = currentDone
                currentDone = null
                isSpeaking = false
                done?.invoke(SpeakResult.entries.getOrElse(msg.arg2) { SpeakResult.ERROR })
            }
        }
    }

    override fun engines(): List<EngineOption> = NeuralSpeaker.systemEngines(app)

    override fun voices(): List<VoiceOption> =
        listOf(VoiceOption(NeuralSpeaker.VOICE_NAME, "Voz neural (faber, Brasil) · offline", 500, needsNetwork = false, installed = true))

    override fun selectVoice(name: String?, allowNetwork: Boolean): String = NeuralSpeaker.VOICE_NAME

    override fun speak(parts: List<Speech>, rate: Float, onDone: (SpeakResult) -> Unit) {
        stop()
        if (parts.isEmpty()) return onDone(SpeakResult.COMPLETED)
        if (ended || status != TtsStatus.READY) return onDone(SpeakResult.UNAVAILABLE)
        val id = ++nextId
        currentId = id
        currentDone = onDone
        isSpeaking = true
        val msg = Message.obtain(null, NeuralVoiceService.MSG_SPEAK, id, 0).apply {
            data = Bundle().apply {
                putStringArray(NeuralVoiceService.KEY_TEXTS, parts.map { it.text }.toTypedArray())
                putLongArray(NeuralVoiceService.KEY_PAUSES, parts.map { it.pauseAfterMs }.toLongArray())
                putFloat(NeuralVoiceService.KEY_RATE, rate)
            }
        }
        // Se a voz não responder em bem mais tempo do que a fala levaria, desiste dela.
        val chars = parts.sumOf { it.text.length }
        val pauses = parts.sumOf { it.pauseAfterMs }
        main.postDelayed(speechTimeout, 20_000 + pauses + (chars * 150 / rate.coerceAtLeast(0.5f)).toLong())
        send(msg)
    }

    override fun stop() {
        main.removeCallbacks(speechTimeout)
        val wasSpeaking = isSpeaking
        currentId = -1
        currentDone = null
        isSpeaking = false
        if (wasSpeaking && !ended) send(Message.obtain(null, NeuralVoiceService.MSG_STOP))
    }

    override fun shutdown() {
        stop()
        ended = true
        main.removeCallbacks(loadTimeout)
        release()
    }

    private fun send(msg: Message) {
        val s = service
        if (s == null) {
            // Ainda conectando: só a fala precisa de serviço pronto, e ela exige status READY.
            if (msg.what == NeuralVoiceService.MSG_SPEAK) fail()
            return
        }
        if (runCatching { s.send(msg) }.isFailure) fail()
    }

    private fun fail() {
        if (ended) return
        ended = true
        main.removeCallbacks(loadTimeout)
        main.removeCallbacks(speechTimeout)
        val done = currentDone
        currentDone = null
        isSpeaking = false
        status = TtsStatus.UNAVAILABLE
        release()
        done?.invoke(SpeakResult.ERROR)
        onStatus(TtsStatus.UNAVAILABLE)
    }

    private fun release() {
        service = null
        if (bound) {
            bound = false
            runCatching { (unbind ?: { c -> app.unbindService(c) })(connection) }
        }
    }
}
