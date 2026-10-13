package br.com.perguntaloei.game

import br.com.perguntaloei.model.GameConfig
import br.com.perguntaloei.model.GameMode
import br.com.perguntaloei.model.Player
import br.com.perguntaloei.model.Question
import br.com.perguntaloei.model.QuestionFormat
import br.com.perguntaloei.model.Theme
import br.com.perguntaloei.questions.QuestionBank
import br.com.perguntaloei.questions.QuestionSelector
import br.com.perguntaloei.questions.UsageHistory
import kotlin.random.Random

/** Ações que o grupo pode tomar. Ações fora de hora são ignoradas (o estado não muda). */
sealed interface GameAction {
    /** Começa a rodada exibida na introdução. */
    data object BeginRound : GameAction

    /** Repetir a leitura: não é resposta e não altera nada. */
    data object Repeat : GameAction

    data class SubmitAnswer(val choice: AnswerChoice, val method: AnswerMethod) : GameAction

    /** Pular: sem ponto, mostra a resposta e passa a vez. */
    data object Skip : GameAction

    /** Ninguém respondeu: encerra a vez sem ponto. */
    data object NoAnswer : GameAction

    /** Anula a pergunta (problema de áudio, interrupção, jogador errado ou repetida) e troca por outra. */
    data class Annul(val repeated: Boolean = false) : GameAction

    /** Desfaz o último resultado exibido e volta para a mesma pergunta. */
    data object Undo : GameAction

    /** Continuar para o próximo jogador / rodada. */
    data object Next : GameAction

    data object StartTiebreak : GameAction
    data object AcceptTie : GameAction
    data object NextMatch : GameAction

    /** Encerra o jogo antes do fim; a pergunta em aberto é descartada sem ponto. */
    data object EndEarly : GameAction
}

class NotEnoughQuestionsException(message: String) : IllegalStateException(message)

/**
 * Regras do jogo. Funções puras: recebem um estado e devolvem o próximo.
 * O placar é sempre derivado do registro de perguntas avaliadas, então não existe
 * caminho para alterar pontos sem uma resposta avaliada.
 */
class GameEngine(
    private val bank: QuestionBank,
    private val history: () -> UsageHistory = { UsageHistory.EMPTY },
    private val clock: () -> Long = System::currentTimeMillis,
) {
    val selector = QuestionSelector(bank)

    fun question(id: String): Question = bank.byId.getValue(id)

    fun currentQuestion(state: GameState): Question? = state.round?.currentSlot?.let { bank.byId[it.questionId] }

    /** Temas efetivos: os escolhidos que têm perguntas no modo atual. */
    fun effectiveThemes(config: GameConfig): List<Theme> {
        val available = bank.themesWithQuestions(brazilOnly = config.mode == GameMode.BRAZIL)
        return config.themes.filter { it in available }.distinct()
    }

    fun newGame(config: GameConfig, players: List<Player>, seed: Long = Random.nextLong(), id: String = "jogo-$seed"): GameState {
        require(players.isNotEmpty()) { "Cadastre pelo menos um jogador." }
        require(players.map { it.id }.toSet().size == players.size) { "Jogadores repetidos." }
        val themes = effectiveThemes(config)
        if (themes.isEmpty()) throw NotEnoughQuestionsException("Nenhum dos temas escolhidos tem perguntas neste modo.")
        val cfg = config.copy(
            themes = themes,
            rounds = config.rounds.coerceIn(1, 50),
            roundsPerMatch = config.roundsPerMatch.coerceIn(1, 10),
        )
        val initial = GameState(id = id, createdAt = clock(), config = cfg, players = players, seed = seed, phase = Phase.ROUND_INTRO)
        return planRegularRound(initial)
            ?: throw NotEnoughQuestionsException("Não há perguntas suficientes para estes jogadores e temas.")
    }

    fun reduce(state: GameState, action: GameAction): GameState = when (action) {
        GameAction.BeginRound -> if (state.phase == Phase.ROUND_INTRO && state.round != null) {
            state.copy(phase = Phase.ASKING, notice = null)
        } else state
        GameAction.Repeat -> state
        is GameAction.SubmitAnswer -> submit(state, action)
        GameAction.Skip -> closeWithoutAnswer(state, Outcome.SKIPPED)
        GameAction.NoAnswer -> closeWithoutAnswer(state, Outcome.NO_ANSWER)
        is GameAction.Annul -> annul(state, action.repeated)
        GameAction.Undo -> undo(state)
        GameAction.Next -> next(state)
        GameAction.StartTiebreak -> startTiebreak(state)
        GameAction.AcceptTie -> acceptTie(state)
        GameAction.NextMatch -> nextMatch(state)
        GameAction.EndEarly -> endEarly(state)
    }

    private fun endEarly(state: GameState): GameState {
        if (state.finished) return state
        val total = state.players.associate { it.id to state.totalScore(it.id) }
        val ranked = if (state.config.mode == GameMode.BEST_OF_THREE) {
            state.players.sortedWith(compareByDescending<Player> { state.matchWins(it.id) }.thenByDescending { total[it.id] })
        } else {
            state.players.sortedByDescending { total[it.id] }
        }
        val best = ranked.first()
        val winners = ranked.filter {
            total[it.id] == total[best.id] &&
                (state.config.mode != GameMode.BEST_OF_THREE || state.matchWins(it.id) == state.matchWins(best.id))
        }.map { it.id }
        return state.copy(
            phase = Phase.GAME_OVER, round = null, tie = null, revealSeq = null, finished = true,
            winners = winners, notice = "Partida encerrada antes do fim.",
        )
    }

    // ------------------------------------------------------------------ respostas

    private fun submit(state: GameState, action: GameAction.SubmitAnswer): GameState {
        if (state.phase != Phase.ASKING) return state
        val round = state.round ?: return state
        val slot = round.currentSlot ?: return state
        val q = question(slot.questionId)
        val (given, correct) = when (val c = action.choice) {
            is AnswerChoice.Option -> {
                if (q.format == QuestionFormat.OPEN || c.index !in q.options.indices) return state
                val label = if (q.format == QuestionFormat.MULTIPLE_CHOICE) "${'A' + c.index}) ${q.options[c.index]}" else q.options[c.index]
                label to (c.index == q.correctIndex)
            }
            is AnswerChoice.Text -> {
                if (q.format != QuestionFormat.OPEN || c.text.isBlank()) return state
                c.text.trim() to AnswerMatcher.isCorrectOpen(c.text, q)
            }
            is AnswerChoice.Judged -> {
                if (q.format != QuestionFormat.OPEN) return state
                c.text.trim() to c.correct
            }
        }
        val points = if (correct && round.kind == RoundKind.REGULAR) 1 else 0
        val record = newRecord(state, slot, q, given, if (correct) Outcome.CORRECT else Outcome.WRONG, action.method, points)
        return state.copy(log = state.log + record, phase = Phase.REVEAL, revealSeq = record.seq, notice = null)
    }

    private fun closeWithoutAnswer(state: GameState, outcome: Outcome): GameState {
        if (state.phase != Phase.ASKING) return state
        val slot = state.round?.currentSlot ?: return state
        val q = question(slot.questionId)
        val record = newRecord(state, slot, q, null, outcome, AnswerMethod.NONE, 0)
        return state.copy(log = state.log + record, phase = Phase.REVEAL, revealSeq = record.seq, notice = null)
    }

    private fun newRecord(
        state: GameState, slot: TurnSlot, q: Question, given: String?, outcome: Outcome, method: AnswerMethod, points: Int,
    ): TurnRecord {
        val round = state.round!!
        return TurnRecord(
            seq = (state.log.maxOfOrNull { it.seq } ?: 0) + 1,
            match = state.match,
            round = round.number,
            kind = round.kind,
            playerId = slot.playerId,
            playerName = state.player(slot.playerId)?.name ?: "?",
            questionId = q.id,
            questionText = q.text,
            theme = q.theme,
            difficulty = q.difficulty,
            givenAnswer = given,
            correctAnswer = q.answer,
            outcome = outcome,
            method = method,
            points = points,
            timestamp = clock(),
        )
    }

    // ------------------------------------------------------------------ anular / desfazer

    private fun annul(state: GameState, repeated: Boolean): GameState {
        if (state.phase != Phase.ASKING && state.phase != Phase.REVEAL) return state
        val round = state.round ?: return state
        val slot = round.currentSlot ?: return state
        val q = question(slot.questionId)
        // Se o resultado já tinha sido exibido, ele deixa de valer (sem tocar nos pontos de ninguém mais).
        var log = state.log
        if (state.phase == Phase.REVEAL) {
            val shown = state.revealRecord ?: return state
            if (shown.outcome == Outcome.ANNULLED || shown.outcome == Outcome.REPLACED_REPEATED) return state
            log = log.map { if (it.seq == shown.seq) it.copy(undone = true) else it }
        }
        val base = state.copy(log = log)
        val record = newRecord(
            base, slot, q, null, if (repeated) Outcome.REPLACED_REPEATED else Outcome.ANNULLED, AnswerMethod.NONE, 0,
        )
        val player = state.player(slot.playerId) ?: return state
        val rng = rngFor(state)
        val used = state.usedQuestionIds.toSet()
        val theme = round.theme ?: q.theme
        val pick = selector.pick(player, theme, state.config, used, history(), rng)
            ?: state.config.themes.filter { it != theme }.firstNotNullOfOrNull {
                if (round.theme != null) null else selector.pick(player, it, state.config, used, history(), rng)
            }
        val withRecord = base.copy(log = base.log + record, rngCounter = state.rngCounter + 1)
        if (pick == null) {
            // Sem substituta: a vez termina sem ponto.
            return withRecord.copy(
                phase = Phase.REVEAL,
                revealSeq = record.seq,
                notice = "Não há outra pergunta de ${theme.label} disponível para ${player.name}. A vez foi encerrada sem ponto.",
            )
        }
        val newSlot = slot.copy(
            questionId = pick.question.id,
            reusedFromHistory = pick.reusedFromHistory,
            difficultyAdjusted = pick.difficultyAdjusted,
            replacements = slot.replacements + 1,
        )
        val slots = round.slots.toMutableList().also { it[round.turnIndex] = newSlot }
        return withRecord.copy(
            round = round.copy(slots = slots),
            usedQuestionIds = state.usedQuestionIds + pick.question.id,
            phase = Phase.ASKING,
            revealSeq = null,
            notice = if (repeated) "Pergunta trocada sem penalidade." else "Pergunta anulada. O placar não mudou.",
        )
    }

    private fun undo(state: GameState): GameState {
        if (state.phase != Phase.REVEAL) return state
        val shown = state.revealRecord ?: return state
        if (shown.undone || shown.outcome == Outcome.ANNULLED || shown.outcome == Outcome.REPLACED_REPEATED) return state
        if (shown.seq != state.log.maxOf { it.seq }) return state
        return state.copy(
            log = state.log.map { if (it.seq == shown.seq) it.copy(undone = true) else it },
            phase = Phase.ASKING,
            revealSeq = null,
            notice = "Resultado desfeito. ${shown.playerName} pode responder de novo.",
        )
    }

    // ------------------------------------------------------------------ avanço

    private fun next(state: GameState): GameState {
        if (state.phase != Phase.REVEAL) return state
        val round = state.round ?: return state
        if (round.turnIndex + 1 < round.slots.size) {
            return state.copy(round = round.copy(turnIndex = round.turnIndex + 1), phase = Phase.ASKING, revealSeq = null, notice = null)
        }
        val cleared = state.copy(revealSeq = null, notice = null)
        return if (round.kind == RoundKind.REGULAR) endOfRegularRound(cleared) else endOfTiebreakRound(cleared)
    }

    private fun endOfRegularRound(state: GameState): GameState {
        if (state.regularRound < state.roundsInMatch) {
            planRegularRound(state)?.let { return it }
            return finishMatch(state.copy(notice = "As perguntas disponíveis acabaram. A partida foi encerrada antes do previsto."))
        }
        return finishMatch(state)
    }

    private fun finishMatch(state: GameState): GameState {
        val scores = state.players.associate { it.id to state.score(it.id) }
        val max = scores.values.max()
        val leaders = state.players.filter { scores[it.id] == max }.map { it.id }
        val ended = state.copy(round = null)
        if (leaders.size == 1 || state.players.size == 1) return matchWonBy(ended, leaders.first())
        val purpose = if (state.config.mode == GameMode.BEST_OF_THREE) TiePurpose.MATCH else TiePurpose.FINAL
        val phase = if (purpose == TiePurpose.MATCH) Phase.MATCH_END else Phase.GAME_OVER
        return ended.copy(phase = phase, tie = TieState(leaders, purpose))
    }

    private fun matchWonBy(state: GameState, winnerId: String): GameState {
        if (state.config.mode != GameMode.BEST_OF_THREE) {
            return state.copy(phase = Phase.GAME_OVER, winners = listOf(winnerId), finished = true, tie = null, round = null)
        }
        val s = state.copy(matchWinners = state.matchWinners + listOf(listOf(winnerId)), tie = null, round = null)
        return afterMatchResult(s)
    }

    private fun afterMatchResult(s: GameState): GameState {
        val champion = s.players.firstOrNull { s.matchWins(it.id) >= 2 }
        if (champion != null) return s.copy(phase = Phase.GAME_OVER, winners = listOf(champion.id), finished = true)
        if (s.match >= 3) {
            val wins = s.players.associate { it.id to s.matchWins(it.id) }
            val max = wins.values.max()
            val leaders = s.players.filter { wins[it.id] == max }.map { it.id }
            return if (leaders.size == 1) {
                s.copy(phase = Phase.GAME_OVER, winners = leaders, finished = true)
            } else {
                s.copy(phase = Phase.GAME_OVER, tie = TieState(leaders, TiePurpose.FINAL))
            }
        }
        return s.copy(phase = Phase.MATCH_END)
    }

    private fun nextMatch(state: GameState): GameState {
        if (state.phase != Phase.MATCH_END || state.tie != null || state.finished) return state
        val s = state.copy(match = state.match + 1, regularRound = 0, round = null)
        return planRegularRound(s) ?: s.copy(
            phase = Phase.GAME_OVER,
            tie = null,
            notice = "As perguntas disponíveis acabaram antes da próxima partida.",
        ).let { decideByWins(it) }
    }

    private fun decideByWins(s: GameState): GameState {
        val wins = s.players.associate { it.id to s.matchWins(it.id) }
        val max = wins.values.max()
        val leaders = s.players.filter { wins[it.id] == max }.map { it.id }
        return if (leaders.size == 1) s.copy(winners = leaders, finished = true) else s.copy(tie = TieState(leaders, TiePurpose.FINAL))
    }

    // ------------------------------------------------------------------ empate

    private fun startTiebreak(state: GameState): GameState {
        val tie = state.tie ?: return state
        val canStart = (state.phase == Phase.MATCH_END || state.phase == Phase.GAME_OVER) && state.round == null && !state.finished
        if (!canStart) return state
        return planTiebreakRound(state, tie) ?: state.copy(
            notice = "Não há perguntas inéditas suficientes para o desempate. Vocês podem aceitar o empate.",
        )
    }

    private fun acceptTie(state: GameState): GameState {
        val tie = state.tie ?: return state
        val inTiebreakIntro = state.phase == Phase.ROUND_INTRO && state.round?.kind == RoundKind.TIEBREAK
        val pending = (state.phase == Phase.MATCH_END || state.phase == Phase.GAME_OVER) && state.round == null
        if (!inTiebreakIntro && !pending) return state
        val s = state.copy(tie = null, round = null, notice = null)
        return when (tie.purpose) {
            TiePurpose.FINAL -> s.copy(phase = Phase.GAME_OVER, winners = tie.playerIds, finished = true)
            TiePurpose.MATCH -> afterMatchResult(s.copy(matchWinners = s.matchWinners + listOf(emptyList())))
        }
    }

    private fun endOfTiebreakRound(state: GameState): GameState {
        val round = state.round ?: return state
        val tie = state.tie ?: return state
        val correct = state.log.filter {
            it.kind == RoundKind.TIEBREAK && it.round == round.number && !it.undone && it.outcome == Outcome.CORRECT
        }.map { it.playerId }.distinct()
        if (correct.size == 1) {
            val winner = correct.first()
            val s = state.copy(round = null, tie = null)
            return when (tie.purpose) {
                TiePurpose.FINAL -> s.copy(phase = Phase.GAME_OVER, winners = listOf(winner), finished = true)
                TiePurpose.MATCH -> matchWonBy(s, winner)
            }
        }
        val survivors = if (correct.isEmpty()) tie.playerIds else tie.playerIds.filter { it in correct }
        val newTie = tie.copy(playerIds = survivors, tiebreakRounds = tie.tiebreakRounds + 1)
        val base = state.copy(round = null, tie = newTie, phase = if (tie.purpose == TiePurpose.MATCH) Phase.MATCH_END else Phase.GAME_OVER)
        val note = if (correct.isEmpty()) "Ninguém acertou. Mais uma pergunta de desempate!" else "Ainda empatados. Mais uma pergunta de desempate!"
        return planTiebreakRound(base, newTie)?.copy(notice = note)
            ?: base.copy(notice = "Não há mais perguntas inéditas para desempatar. Vocês podem aceitar o empate.")
    }

    // ------------------------------------------------------------------ planejamento

    private fun rngFor(state: GameState): Random = Random(state.seed xor (state.rngCounter.toLong() * 0x2545F4914F6CDD1DL))

    /** Ordem de tentativa dos temas: os menos usados primeiro, sorteando entre empatados. */
    private fun themeOrder(state: GameState, rng: Random): List<Theme> {
        val counts = state.themeHistory.groupingBy { it }.eachCount()
        val last = state.themeHistory.lastOrNull()
        return state.config.themes.shuffled(rng).sortedWith(
            compareBy<Theme>({ counts[it] ?: 0 }, { if (it == last) 1 else 0 }),
        )
    }

    /** Seleciona, antes da rodada começar, uma pergunta não usada para cada jogador. */
    private fun planRegularRound(state: GameState): GameState? {
        val rng = rngFor(state)
        val number = state.regularRound + 1
        val history = history()
        val round: RoundState
        val chosenThemes: List<Theme>
        var notice: String? = null

        if (state.config.mode == GameMode.QUESTION_COUNT) {
            val themes = state.config.themes
            val reserved = state.usedQuestionIds.toMutableSet()
            val slots = mutableListOf<TurnSlot>()
            val themesUsed = mutableListOf<Theme>()
            val offset = state.themeHistory.size
            for (p in state.players) {
                val rotated = themes.indices.map { themes[(offset + themesUsed.size + it) % themes.size] }
                var picked: Pair<Theme, br.com.perguntaloei.questions.Pick>? = null
                for (allowReuse in listOf(false, true)) {
                    for (t in rotated) {
                        val pick = selector.pick(p, t, state.config, reserved, history, rng, allowReuse) ?: continue
                        picked = t to pick
                        break
                    }
                    if (picked != null) break
                }
                val (t, pick) = picked ?: return null
                reserved += pick.question.id
                themesUsed += t
                slots += TurnSlot(p.id, pick.question.id, pick.reusedFromHistory, pick.difficultyAdjusted)
            }
            round = RoundState(RoundKind.REGULAR, number, null, slots)
            chosenThemes = themesUsed
        } else {
            val order = themeOrder(state, rng)
            var planned: Pair<Theme, List<TurnSlot>>? = null
            for (allowReuse in listOf(false, true)) {
                for (t in order) {
                    val slots = planThemeForPlayers(state.players, t, state, history, rng, allowReuse) ?: continue
                    planned = t to slots
                    break
                }
                if (planned != null) break
            }
            val (theme, slots) = planned ?: return null
            if (theme != order.first()) {
                notice = "O tema ${order.first().label} não tem perguntas suficientes para todos agora. Tema desta rodada: ${theme.label}."
            }
            if (slots.any { it.reusedFromHistory }) {
                notice = listOfNotNull(notice, "Algumas perguntas já apareceram em partidas anteriores (as inéditas deste tema acabaram).").joinToString(" ")
            }
            round = RoundState(RoundKind.REGULAR, number, theme, slots)
            chosenThemes = listOf(theme)
        }
        return state.copy(
            phase = Phase.ROUND_INTRO,
            round = round,
            regularRound = number,
            themeHistory = state.themeHistory + chosenThemes,
            usedQuestionIds = state.usedQuestionIds + round.slots.map { it.questionId },
            rngCounter = state.rngCounter + 1,
            revealSeq = null,
            notice = notice ?: state.notice,
        )
    }

    private fun planThemeForPlayers(
        players: List<Player>, theme: Theme, state: GameState, history: UsageHistory, rng: Random, allowReuse: Boolean,
    ): List<TurnSlot>? {
        val reserved = state.usedQuestionIds.toMutableSet()
        val slots = mutableListOf<TurnSlot>()
        for (p in players) {
            val pick = selector.pick(p, theme, state.config, reserved, history, rng, allowReuse) ?: return null
            reserved += pick.question.id
            slots += TurnSlot(p.id, pick.question.id, pick.reusedFromHistory, pick.difficultyAdjusted)
        }
        return slots
    }

    private fun planTiebreakRound(state: GameState, tie: TieState): GameState? {
        val rng = rngFor(state)
        val players = state.players.filter { it.id in tie.playerIds }
        // Desempate só com perguntas inéditas: nada do histórico.
        for (t in themeOrder(state, rng)) {
            val slots = planThemeForPlayers(players, t, state, history(), rng, allowReuse = false) ?: continue
            val number = state.tiebreakCounter + 1
            return state.copy(
                phase = Phase.ROUND_INTRO,
                round = RoundState(RoundKind.TIEBREAK, number, t, slots),
                tiebreakCounter = number,
                tie = tie,
                usedQuestionIds = state.usedQuestionIds + slots.map { it.questionId },
                rngCounter = state.rngCounter + 1,
                notice = null,
            )
        }
        return null
    }
}
