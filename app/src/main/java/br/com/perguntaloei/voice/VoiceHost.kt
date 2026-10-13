package br.com.perguntaloei.voice

import android.content.Context
import android.media.AudioAttributes
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import android.speech.tts.Voice
import br.com.perguntaloei.game.Speech
import java.util.Locale

enum class TtsStatus { INITIALIZING, READY, MISSING_LANGUAGE, UNAVAILABLE }

enum class SpeakResult {
    /** Toda a fala terminou: só agora o microfone pode abrir. */
    COMPLETED,

    /** O mecanismo de voz relatou erro. */
    ERROR,

    /** Voz indisponível neste aparelho. */
    UNAVAILABLE,

    /** O mecanismo não avisou o fim dentro do tempo esperado. */
    TIMEOUT,
}

/**
 * Apresentador: fala usando o TextToSpeech do Android (pt-BR). Cada leitura recebe um
 * identificador; avisos de leituras antigas (interrompidas ou repetidas) são ignorados,
 * para que o fim de uma leitura velha nunca abra o microfone por engano.
 */
class VoiceHost(context: Context, private val onStatus: (TtsStatus) -> Unit) {

    private val main = Handler(Looper.getMainLooper())
    private var tts: TextToSpeech? = null
    var status: TtsStatus = TtsStatus.INITIALIZING
        private set

    private var token = 0
    private var callback: ((SpeakResult) -> Unit)? = null
    private var timeout: Runnable? = null
    var isSpeaking: Boolean = false
        private set

    init {
        tts = TextToSpeech(context.applicationContext) { code ->
            main.post { onInit(code) }
        }
    }

    private fun onInit(code: Int) {
        val engine = tts
        if (code != TextToSpeech.SUCCESS || engine == null) {
            setStatus(TtsStatus.UNAVAILABLE)
            return
        }
        val ptBr = Locale("pt", "BR")
        var result = engine.setLanguage(ptBr)
        if (result == TextToSpeech.LANG_MISSING_DATA || result == TextToSpeech.LANG_NOT_SUPPORTED) {
            result = engine.setLanguage(Locale("pt"))
        }
        if (result == TextToSpeech.LANG_MISSING_DATA || result == TextToSpeech.LANG_NOT_SUPPORTED) {
            setStatus(TtsStatus.MISSING_LANGUAGE)
            return
        }
        // Prefere uma voz instalada no aparelho, que não dependa de internet.
        runCatching {
            val offline = engine.voices?.filter { v: Voice ->
                v.locale.language == "pt" && !v.isNetworkConnectionRequired &&
                    !v.features.contains(TextToSpeech.Engine.KEY_FEATURE_NOT_INSTALLED)
            }?.sortedWith(compareByDescending<Voice> { it.locale.country == "BR" }.thenByDescending { it.quality })
            offline?.firstOrNull()?.let { engine.voice = it }
        }
        engine.setAudioAttributes(
            AudioAttributes.Builder()
                .setUsage(AudioAttributes.USAGE_MEDIA)
                .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
                .build(),
        )
        engine.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
            override fun onStart(utteranceId: String?) = Unit
            override fun onDone(utteranceId: String?) {
                main.post { if (utteranceId == endId(token)) finish(SpeakResult.COMPLETED) }
            }

            @Deprecated("Deprecated in Java")
            override fun onError(utteranceId: String?) {
                main.post { if (utteranceId?.startsWith("t$token-") == true) finish(SpeakResult.ERROR) }
            }

            override fun onError(utteranceId: String?, errorCode: Int) {
                main.post { if (utteranceId?.startsWith("t$token-") == true) finish(SpeakResult.ERROR) }
            }
        })
        setStatus(TtsStatus.READY)
    }

    private fun setStatus(s: TtsStatus) {
        status = s
        onStatus(s)
    }

    private fun endId(t: Int) = "t$t-fim"

    /** Fala os trechos em sequência e chama [onDone] uma única vez quando tudo terminar. */
    fun speak(parts: List<Speech>, rate: Float, onDone: (SpeakResult) -> Unit) {
        cancelCurrent()
        val engine = tts
        if (status != TtsStatus.READY || engine == null || parts.isEmpty()) {
            onDone(if (parts.isEmpty()) SpeakResult.COMPLETED else SpeakResult.UNAVAILABLE)
            return
        }
        token++
        val t = token
        callback = onDone
        isSpeaking = true
        engine.setSpeechRate(rate.coerceIn(0.5f, 2.0f))
        val params = Bundle()
        var totalChars = 0
        var totalPause = 0L
        parts.forEachIndexed { i, part ->
            totalChars += part.text.length
            engine.speak(part.text, TextToSpeech.QUEUE_ADD, params, "t$t-$i")
            if (part.pauseAfterMs > 0) {
                totalPause += part.pauseAfterMs
                engine.playSilentUtterance(part.pauseAfterMs, TextToSpeech.QUEUE_ADD, "t$t-$i-pausa")
            }
        }
        // Marcador final: o fim dele significa que tudo já foi falado.
        engine.playSilentUtterance(1, TextToSpeech.QUEUE_ADD, endId(t))
        val limit = 6000L + totalPause + (totalChars * 140L / rate.coerceIn(0.5f, 2f)).toLong()
        timeout = Runnable { if (t == token) finish(SpeakResult.TIMEOUT) }.also { main.postDelayed(it, limit) }
    }

    private fun finish(result: SpeakResult) {
        val cb = callback ?: return
        callback = null
        isSpeaking = false
        timeout?.let { main.removeCallbacks(it) }
        timeout = null
        cb(result)
    }

    private fun cancelCurrent() {
        token++
        callback = null
        isSpeaking = false
        timeout?.let { main.removeCallbacks(it) }
        timeout = null
        tts?.stop()
    }

    /** Interrompe a fala sem chamar o retorno da leitura interrompida. */
    fun stop() = cancelCurrent()

    fun shutdown() {
        cancelCurrent()
        tts?.shutdown()
        tts = null
    }
}
