package br.com.perguntaloei.voice

import br.com.perguntaloei.audio.Sfx
import br.com.perguntaloei.game.Speech

/** Uma voz disponível no aparelho. */
data class VoiceOption(
    val name: String,
    val label: String,
    /** Qualidade informada pelo mecanismo (quanto maior, mais natural). */
    val quality: Int,
    val needsNetwork: Boolean,
    val installed: Boolean,
)

/** Um mecanismo de voz instalado (ex.: Google, Samsung). */
data class EngineOption(val packageName: String, val label: String)

/** Quem fala pelo apresentador (no app: TextToSpeech do Android). */
interface Speaker {
    val status: TtsStatus
    val isSpeaking: Boolean

    /** Mecanismo em uso e os instalados. */
    val engine: String?
    fun engines(): List<EngineOption> = emptyList()

    /** Vozes em português do mecanismo atual, da mais natural para a menos natural. */
    fun voices(): List<VoiceOption> = emptyList()

    /** Voz em uso. */
    val currentVoice: String?

    /** Escolhe a voz pelo nome (null = a mais natural disponível). Devolve a voz aplicada. */
    fun selectVoice(name: String?, allowNetwork: Boolean): String? = null

    fun setPitch(pitch: Float) = Unit

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
    /** Cria o apresentador com o mecanismo indicado (null = padrão do aparelho). */
    val speaker: (engine: String?, onStatus: (TtsStatus) -> Unit) -> Speaker,
    val listener: Listener,
    val sounds: SoundPlayer,
    val micPermission: () -> Boolean,
)
