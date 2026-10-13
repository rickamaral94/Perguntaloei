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
 *
 * A naturalidade depende das vozes instaladas: o app escolhe a de maior qualidade
 * (vozes "neurais"/alta qualidade do Google TTS, quando instaladas) e permite trocar.
 */
class VoiceHost(
    context: Context,
    enginePackage: String?,
    private val onStatus: (TtsStatus) -> Unit,
) : Speaker {

    private val main = Handler(Looper.getMainLooper())
    private var tts: TextToSpeech? = null
    override var status: TtsStatus = TtsStatus.INITIALIZING
        private set

    private var token = 0
    private var callback: ((SpeakResult) -> Unit)? = null
    private var timeout: Runnable? = null
    override var isSpeaking: Boolean = false
        private set
    override var engine: String? = enginePackage
        private set
    override val currentVoice: String? get() = runCatching { tts?.voice?.name }.getOrNull()
    private var pitch = 1.0f

    init {
        val listener = TextToSpeech.OnInitListener { code -> main.post { onInit(code) } }
        tts = if (enginePackage.isNullOrBlank()) {
            TextToSpeech(context.applicationContext, listener)
        } else {
            TextToSpeech(context.applicationContext, listener, enginePackage)
        }
    }

    private fun onInit(code: Int) {
        val e = tts
        if (code != TextToSpeech.SUCCESS || e == null) {
            setStatus(TtsStatus.UNAVAILABLE)
            return
        }
        engine = runCatching { e.defaultEngine }.getOrNull().takeIf { engine == null } ?: engine
        var result = e.setLanguage(Locale("pt", "BR"))
        if (result == TextToSpeech.LANG_MISSING_DATA || result == TextToSpeech.LANG_NOT_SUPPORTED) {
            result = e.setLanguage(Locale("pt"))
        }
        if (result == TextToSpeech.LANG_MISSING_DATA || result == TextToSpeech.LANG_NOT_SUPPORTED) {
            setStatus(TtsStatus.MISSING_LANGUAGE)
            return
        }
        selectVoice(null, allowNetwork = false)
        e.setAudioAttributes(
            AudioAttributes.Builder()
                .setUsage(AudioAttributes.USAGE_MEDIA)
                .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
                .build(),
        )
        e.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
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

    override fun engines(): List<EngineOption> =
        runCatching { tts?.engines.orEmpty().map { EngineOption(it.name, it.label) } }.getOrDefault(emptyList())

    override fun voices(): List<VoiceOption> = runCatching {
        tts?.voices.orEmpty()
            .filter { it.locale.language == "pt" }
            .sortedWith(voiceRanking())
            .map { v ->
                VoiceOption(
                    name = v.name,
                    label = describe(v),
                    quality = v.quality,
                    needsNetwork = v.isNetworkConnectionRequired,
                    installed = !v.features.contains(TextToSpeech.Engine.KEY_FEATURE_NOT_INSTALLED),
                )
            }
    }.getOrDefault(emptyList())

    /** Mais natural primeiro: português do Brasil, maior qualidade, menor latência. */
    private fun voiceRanking(): Comparator<Voice> =
        compareByDescending<Voice> { it.locale.country == "BR" }
            .thenByDescending { it.quality }
            .thenBy { it.latency }
            .thenBy { it.name }

    private fun describe(v: Voice): String {
        val country = if (v.locale.country == "BR") "Brasil" else v.locale.displayCountry.ifBlank { "Portugal" }
        val q = when {
            v.quality >= Voice.QUALITY_VERY_HIGH -> "qualidade muito alta"
            v.quality >= Voice.QUALITY_HIGH -> "alta qualidade"
            v.quality >= Voice.QUALITY_NORMAL -> "qualidade normal"
            else -> "qualidade baixa"
        }
        // Nomes como "pt-br-x-afs-local" ficam mais legíveis só com o identificador curto.
        val id = v.name.removePrefix("pt-br-x-").removePrefix("pt-BR-").removeSuffix("-local").removeSuffix("-network")
        return "Voz $id · $country · $q"
    }

    override fun selectVoice(name: String?, allowNetwork: Boolean): String? {
        val e = tts ?: return null
        return runCatching {
            val all = e.voices.orEmpty().filter {
                it.locale.language == "pt" && !it.features.contains(TextToSpeech.Engine.KEY_FEATURE_NOT_INSTALLED)
            }
            val usable = all.filter { allowNetwork || !it.isNetworkConnectionRequired }
            val chosen = usable.firstOrNull { it.name == name } ?: usable.sortedWith(voiceRanking()).firstOrNull()
            chosen?.let { e.voice = it }
            chosen?.name
        }.getOrNull()
    }

    override fun setPitch(pitch: Float) {
        this.pitch = pitch.coerceIn(0.7f, 1.4f)
    }

    private fun endId(t: Int) = "t$t-fim"

    /** Fala os trechos em sequência e chama [onDone] uma única vez quando tudo terminar. */
    override fun speak(parts: List<Speech>, rate: Float, onDone: (SpeakResult) -> Unit) {
        cancelCurrent()
        val e = tts
        if (status != TtsStatus.READY || e == null || parts.isEmpty()) {
            onDone(if (parts.isEmpty()) SpeakResult.COMPLETED else SpeakResult.UNAVAILABLE)
            return
        }
        token++
        val t = token
        callback = onDone
        isSpeaking = true
        e.setSpeechRate(rate.coerceIn(0.5f, 2.0f))
        e.setPitch(pitch)
        val params = Bundle()
        var totalChars = 0
        var totalPause = 0L
        parts.forEachIndexed { i, part ->
            totalChars += part.text.length
            e.speak(part.text, TextToSpeech.QUEUE_ADD, params, "t$t-$i")
            if (part.pauseAfterMs > 0) {
                totalPause += part.pauseAfterMs
                e.playSilentUtterance(part.pauseAfterMs, TextToSpeech.QUEUE_ADD, "t$t-$i-pausa")
            }
        }
        // Marcador final: o fim dele significa que tudo já foi falado.
        e.playSilentUtterance(1, TextToSpeech.QUEUE_ADD, endId(t))
        val limit = 8000L + totalPause + (totalChars * 140L / rate.coerceIn(0.5f, 2f)).toLong()
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
    override fun stop() = cancelCurrent()

    override fun shutdown() {
        cancelCurrent()
        tts?.shutdown()
        tts = null
    }
}
