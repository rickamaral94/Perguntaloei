package br.com.perguntaloei.voice

import br.com.perguntaloei.audio.Sfx
import br.com.perguntaloei.game.Speech

/** Quem fala pelo apresentador (no app: TextToSpeech do Android). */
interface Speaker {
    val status: TtsStatus
    val isSpeaking: Boolean

    /** Fala tudo e chama [onDone] uma única vez, só quando a fala terminar (ou falhar). */
    fun speak(parts: List<Speech>, rate: Float, onDone: (SpeakResult) -> Unit)

    /** Interrompe sem chamar o retorno da fala interrompida. */
    fun stop()
    fun shutdown()
}

/** Quem escuta as respostas (no app: SpeechRecognizer do Android). Nunca grava áudio. */
interface Listener {
    val isListening: Boolean
    fun isAvailable(): Boolean
    fun start(onEvent: (SpeechEvent) -> Unit)
    fun stop()
    fun cancel()
    fun destroy()
}

interface SoundPlayer {
    var enabled: Boolean
    fun play(sfx: Sfx)
    fun release()
}

/** Dependências de áudio do app; os testes trocam por versões falsas. */
class VoiceDeps(
    val speaker: ((TtsStatus) -> Unit) -> Speaker,
    val listener: Listener,
    val sounds: SoundPlayer,
    val micPermission: () -> Boolean,
)
