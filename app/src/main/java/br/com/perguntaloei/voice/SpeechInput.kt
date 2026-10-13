package br.com.perguntaloei.voice

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.speech.RecognitionListener
import android.speech.RecognizerIntent
import android.speech.SpeechRecognizer
import br.com.perguntaloei.game.Transcript

sealed interface SpeechEvent {
    data object Ready : SpeechEvent
    data class Level(val value: Float) : SpeechEvent
    data class Partial(val text: String) : SpeechEvent
    data class Results(val alternatives: List<Transcript>) : SpeechEvent

    /** [silence] = ninguém falou (resposta inaudível). */
    data class Failure(val message: String, val silence: Boolean, val serviceProblem: Boolean) : SpeechEvent
}

/**
 * Reconhecimento de fala do Android. Escuta uma única vez por chamada de [start] e
 * não grava nem guarda áudio: só recebe o texto reconhecido.
 */
class SpeechInput(private val context: Context) {

    private var recognizer: SpeechRecognizer? = null
    private var token = 0
    var isListening = false
        private set

    fun isAvailable(): Boolean = SpeechRecognizer.isRecognitionAvailable(context)

    fun start(onEvent: (SpeechEvent) -> Unit) {
        destroyRecognizer()
        token++
        val t = token
        val r = try {
            SpeechRecognizer.createSpeechRecognizer(context)
        } catch (e: Exception) {
            onEvent(SpeechEvent.Failure("Reconhecimento de fala indisponível neste aparelho.", false, true))
            return
        }
        recognizer = r
        isListening = true
        r.setRecognitionListener(object : RecognitionListener {
            private fun live() = t == token
            override fun onReadyForSpeech(params: Bundle?) { if (live()) onEvent(SpeechEvent.Ready) }
            override fun onBeginningOfSpeech() = Unit
            override fun onRmsChanged(rmsdB: Float) { if (live()) onEvent(SpeechEvent.Level(((rmsdB + 2f) / 12f).coerceIn(0f, 1f))) }
            override fun onBufferReceived(buffer: ByteArray?) = Unit // áudio não é usado nem guardado
            override fun onEndOfSpeech() = Unit
            override fun onError(error: Int) {
                if (!live()) return
                isListening = false
                onEvent(describe(error))
            }

            override fun onResults(results: Bundle?) {
                if (!live()) return
                isListening = false
                onEvent(SpeechEvent.Results(extract(results)))
            }

            override fun onPartialResults(partialResults: Bundle?) {
                if (!live()) return
                extract(partialResults).firstOrNull()?.let { onEvent(SpeechEvent.Partial(it.text)) }
            }

            override fun onEvent(eventType: Int, params: Bundle?) = Unit
        })
        val intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH).apply {
            putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            putExtra(RecognizerIntent.EXTRA_LANGUAGE, "pt-BR")
            putExtra(RecognizerIntent.EXTRA_LANGUAGE_PREFERENCE, "pt-BR")
            putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 5)
            putExtra(RecognizerIntent.EXTRA_PARTIAL_RESULTS, true)
            putExtra(RecognizerIntent.EXTRA_PREFER_OFFLINE, true)
            putExtra(RecognizerIntent.EXTRA_CALLING_PACKAGE, context.packageName)
            putExtra(RecognizerIntent.EXTRA_SPEECH_INPUT_COMPLETE_SILENCE_LENGTH_MILLIS, 1500L)
        }
        try {
            r.startListening(intent)
        } catch (e: Exception) {
            isListening = false
            onEvent(SpeechEvent.Failure("Não foi possível abrir o microfone.", false, true))
        }
    }

    private fun extract(bundle: Bundle?): List<Transcript> {
        val texts = bundle?.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION).orEmpty()
        val scores = bundle?.getFloatArray(SpeechRecognizer.CONFIDENCE_SCORES)
        return texts.mapIndexed { i, s ->
            val c = scores?.getOrNull(i)
            // Alguns serviços enviam 0 ou -1 quando não calculam confiança.
            Transcript(s, if (c == null || c <= 0f) null else c)
        }
    }

    private fun describe(error: Int): SpeechEvent.Failure = when (error) {
        SpeechRecognizer.ERROR_NO_MATCH, SpeechRecognizer.ERROR_SPEECH_TIMEOUT ->
            SpeechEvent.Failure("Não ouvi nenhuma resposta.", silence = true, serviceProblem = false)
        SpeechRecognizer.ERROR_NETWORK, SpeechRecognizer.ERROR_NETWORK_TIMEOUT, SpeechRecognizer.ERROR_SERVER ->
            SpeechEvent.Failure("O reconhecimento de fala precisa de internet ou o serviço falhou. Responda tocando na tela.", false, true)
        SpeechRecognizer.ERROR_INSUFFICIENT_PERMISSIONS ->
            SpeechEvent.Failure("Sem permissão de microfone. Responda tocando na tela.", false, true)
        SpeechRecognizer.ERROR_AUDIO ->
            SpeechEvent.Failure("Problema no microfone. Tente de novo ou responda tocando.", false, false)
        SpeechRecognizer.ERROR_RECOGNIZER_BUSY ->
            SpeechEvent.Failure("O reconhecimento de fala está ocupado. Tente de novo.", false, false)
        12, 13 -> // ERROR_LANGUAGE_NOT_SUPPORTED / ERROR_LANGUAGE_UNAVAILABLE (Android 12+)
            SpeechEvent.Failure("Português não está disponível no reconhecimento de fala deste aparelho. Responda tocando.", false, true)
        else -> SpeechEvent.Failure("O reconhecimento de fala falhou (código $error). Tente de novo ou responda tocando.", false, false)
    }

    /** Para de ouvir e processa o que já foi dito. */
    fun stop() {
        if (isListening) recognizer?.stopListening()
    }

    /** Cancela sem processar nada. */
    fun cancel() {
        token++
        isListening = false
        recognizer?.cancel()
    }

    private fun destroyRecognizer() {
        recognizer?.let {
            runCatching { it.cancel() }
            runCatching { it.destroy() }
        }
        recognizer = null
    }

    fun destroy() {
        token++
        isListening = false
        destroyRecognizer()
    }
}
