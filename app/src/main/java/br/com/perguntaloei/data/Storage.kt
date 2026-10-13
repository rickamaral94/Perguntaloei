package br.com.perguntaloei.data

import br.com.perguntaloei.game.GameState
import br.com.perguntaloei.model.GameConfig
import br.com.perguntaloei.model.Player
import br.com.perguntaloei.questions.UsageHistory
import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.builtins.ListSerializer
import kotlinx.serialization.json.Json
import java.io.File
import java.io.FileOutputStream

/**
 * Arquivo JSON com escrita atômica: grava em um temporário, sincroniza com o disco e
 * renomeia por cima do original. Uma interrupção no meio da gravação mantém a versão anterior.
 */
class AtomicJsonFile<T>(private val file: File, private val serializer: KSerializer<T>) {

    fun read(): T? {
        if (!file.exists()) return null
        return try {
            json.decodeFromString(serializer, file.readText(Charsets.UTF_8))
        } catch (e: Exception) {
            // Arquivo corrompido: preserva uma cópia para diagnóstico e segue sem ele.
            file.copyTo(File(file.parentFile, file.name + ".corrompido"), overwrite = true)
            null
        }
    }

    @Synchronized
    fun write(value: T) {
        file.parentFile?.mkdirs()
        val tmp = File(file.parentFile, file.name + ".tmp")
        FileOutputStream(tmp).use { out ->
            out.write(json.encodeToString(serializer, value).toByteArray(Charsets.UTF_8))
            out.flush()
            out.fd.sync()
        }
        if (!tmp.renameTo(file)) {
            file.delete()
            check(tmp.renameTo(file)) { "Falha ao salvar ${file.name}" }
        }
    }

    fun delete() {
        file.delete()
    }

    companion object {
        val json = Json { ignoreUnknownKeys = true; encodeDefaults = true }
    }
}

@Serializable
data class AppSettings(
    val speechRate: Float = 1.0f,
    val soundEffects: Boolean = true,
    /** Sempre pedir confirmação antes de avaliar respostas faladas. */
    val alwaysConfirmVoice: Boolean = false,
    /** Abrir o microfone automaticamente quando a leitura terminar. */
    val autoListen: Boolean = true,
    /** null = ainda não perguntado; true/false = resposta do usuário ao aviso do reconhecimento de fala. */
    val speechConsent: Boolean? = null,
    val lastConfig: GameConfig = GameConfig(),
    /** Já mostramos o pedido de permissões da primeira abertura. */
    val permissionsAsked: Boolean = false,
    /** Mecanismo de voz escolhido (null = padrão do aparelho). */
    val ttsEngine: String? = null,
    /** Voz escolhida (null = a mais natural disponível). */
    val ttsVoice: String? = null,
    /** Permite vozes que precisam de internet (enviam o texto falado ao provedor). */
    val allowNetworkVoices: Boolean = false,
    val voicePitch: Float = 1.0f,
)

@Serializable
data class HistoryEntry(val fingerprint: String, val timesUsed: Int, val lastUsed: Long)

@Serializable
data class QuestionHistory(val entries: Map<String, HistoryEntry> = emptyMap()) {
    fun toUsage(): UsageHistory = UsageHistory(entries.keys, entries.values.map { it.fingerprint }.toSet())
}

@Serializable
data class GameSummary(
    val id: String,
    val finishedAt: Long,
    val mode: String,
    val players: List<String>,
    val scores: List<Int>,
    val winners: List<String>,
)

/** Todo o armazenamento local do app. Nada é enviado para servidores. */
class LocalStore(dir: File) {
    private val playersFile = AtomicJsonFile(File(dir, "jogadores.json"), ListSerializer(Player.serializer()))
    private val settingsFile = AtomicJsonFile(File(dir, "configuracoes.json"), AppSettings.serializer())
    private val historyFile = AtomicJsonFile(File(dir, "historico_perguntas.json"), QuestionHistory.serializer())
    private val gameFile = AtomicJsonFile(File(dir, "partida_atual.json"), GameState.serializer())
    private val summariesFile = AtomicJsonFile(File(dir, "partidas_anteriores.json"), ListSerializer(GameSummary.serializer()))

    fun loadPlayers(): List<Player> = playersFile.read() ?: emptyList()
    fun savePlayers(players: List<Player>) = playersFile.write(players)

    fun loadSettings(): AppSettings = settingsFile.read() ?: AppSettings()
    fun saveSettings(settings: AppSettings) = settingsFile.write(settings)

    fun loadHistory(): QuestionHistory = historyFile.read() ?: QuestionHistory()
    fun saveHistory(history: QuestionHistory) = historyFile.write(history)

    fun loadGame(): GameState? = gameFile.read()
    fun saveGame(state: GameState) = gameFile.write(state)
    fun clearGame() = gameFile.delete()

    fun loadSummaries(): List<GameSummary> = summariesFile.read() ?: emptyList()
    fun addSummary(summary: GameSummary) {
        val list = loadSummaries().filter { it.id != summary.id }
        summariesFile.write((listOf(summary) + list).take(30))
    }
}
