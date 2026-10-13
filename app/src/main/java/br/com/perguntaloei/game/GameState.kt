package br.com.perguntaloei.game

import br.com.perguntaloei.model.Difficulty
import br.com.perguntaloei.model.GameConfig
import br.com.perguntaloei.model.GameMode
import br.com.perguntaloei.model.Player
import br.com.perguntaloei.model.Theme
import kotlinx.serialization.Serializable

@Serializable
enum class Phase {
    /** Apresentação da rodada (tema e ordem). */
    ROUND_INTRO,

    /** Pergunta em andamento: aguardando resposta do jogador da vez. */
    ASKING,

    /** Resultado da pergunta exibido; aguardando "Continuar". */
    REVEAL,

    /** Fim de uma partida do Melhor de três. */
    MATCH_END,

    /** Fim do jogo (ou empate aguardando decisão). */
    GAME_OVER,
}

@Serializable
enum class Outcome(val label: String) {
    CORRECT("Certa"),
    WRONG("Errada"),
    SKIPPED("Pulada"),
    NO_ANSWER("Sem resposta"),
    ANNULLED("Anulada"),
    REPLACED_REPEATED("Trocada (repetida)"),
}

@Serializable
enum class AnswerMethod(val label: String) {
    VOICE("Voz"), TOUCH("Toque"), TYPED("Digitada"), GROUP("Decisão do grupo"), NONE("—");
}

@Serializable
enum class RoundKind { REGULAR, TIEBREAK }

@Serializable
enum class TiePurpose { MATCH, FINAL }

/** Uma vez: um jogador e a pergunta selecionada para ele. */
@Serializable
data class TurnSlot(
    val playerId: String,
    val questionId: String,
    val reusedFromHistory: Boolean = false,
    val difficultyAdjusted: Boolean = false,
    val replacements: Int = 0,
)

@Serializable
data class RoundState(
    val kind: RoundKind,
    /** Número da rodada na partida (regular) ou contador de desempates. */
    val number: Int,
    /** Tema único da rodada; nulo quando cada jogador recebe um tema (modo Número de perguntas). */
    val theme: Theme?,
    val slots: List<TurnSlot>,
    val turnIndex: Int = 0,
) {
    val currentSlot: TurnSlot? get() = slots.getOrNull(turnIndex)
}

@Serializable
data class TieState(
    val playerIds: List<String>,
    val purpose: TiePurpose,
    val tiebreakRounds: Int = 0,
)

/** Registro de cada pergunta feita: base do placar e do histórico da partida. */
@Serializable
data class TurnRecord(
    val seq: Int,
    val match: Int,
    val round: Int,
    val kind: RoundKind,
    val playerId: String,
    val playerName: String,
    val questionId: String,
    val questionText: String,
    val theme: Theme,
    val difficulty: Difficulty,
    val givenAnswer: String?,
    val correctAnswer: String,
    val outcome: Outcome,
    val method: AnswerMethod,
    val points: Int,
    val undone: Boolean = false,
    val timestamp: Long,
)

@Serializable
data class GameState(
    val id: String,
    val createdAt: Long,
    val config: GameConfig,
    /** Ordem oficial das vezes. */
    val players: List<Player>,
    val seed: Long,
    val rngCounter: Int = 0,
    val phase: Phase,
    /** Partida atual (sempre 1 fora do Melhor de três). */
    val match: Int = 1,
    /** Número da última rodada regular planejada na partida atual. */
    val regularRound: Int = 0,
    val round: RoundState? = null,
    val themeHistory: List<Theme> = emptyList(),
    /** Perguntas já atribuídas nesta partida (nunca repetem). */
    val usedQuestionIds: List<String> = emptyList(),
    val log: List<TurnRecord> = emptyList(),
    /** Registro exibido na tela de resultado da pergunta. */
    val revealSeq: Int? = null,
    /** Empate pendente de decisão ou desempate em andamento. */
    val tie: TieState? = null,
    val tiebreakCounter: Int = 0,
    /** Vencedores de cada partida do Melhor de três (lista vazia = empate aceito). */
    val matchWinners: List<List<String>> = emptyList(),
    val winners: List<String> = emptyList(),
    val finished: Boolean = false,
    /** Aviso para o grupo (ex.: tema trocado por falta de perguntas). */
    val notice: String? = null,
) {
    val roundsInMatch: Int get() = if (config.mode == GameMode.BEST_OF_THREE) config.roundsPerMatch else config.rounds

    fun player(id: String): Player? = players.firstOrNull { it.id == id }

    val currentPlayer: Player? get() = round?.currentSlot?.let { player(it.playerId) }

    /** Pontos do jogador na partida indicada: soma dos registros avaliados e não desfeitos. */
    fun score(playerId: String, inMatch: Int = match): Int =
        log.filter { it.playerId == playerId && it.match == inMatch && it.kind == RoundKind.REGULAR && !it.undone }
            .sumOf { it.points }

    fun totalScore(playerId: String): Int =
        log.filter { it.playerId == playerId && it.kind == RoundKind.REGULAR && !it.undone }.sumOf { it.points }

    fun matchWins(playerId: String): Int = matchWinners.count { playerId in it }

    val revealRecord: TurnRecord? get() = revealSeq?.let { s -> log.firstOrNull { it.seq == s } }

    /** Jogador que vem depois do atual (na rodada ou na próxima rodada). */
    val nextPlayer: Player?
        get() {
            val r = round ?: return null
            val next = r.slots.getOrNull(r.turnIndex + 1) ?: return if (r.kind == RoundKind.REGULAR && regularRound < roundsInMatch) players.firstOrNull() else null
            return player(next.playerId)
        }

    val isLastTurnOfRound: Boolean get() = round?.let { it.turnIndex >= it.slots.size - 1 } ?: true

    /** Ordem para a rodada atual (jogadores do desempate ou todos). */
    val turnOrder: List<Player> get() = round?.slots?.mapNotNull { player(it.playerId) } ?: players
}
