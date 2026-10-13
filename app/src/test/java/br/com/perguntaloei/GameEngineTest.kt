package br.com.perguntaloei

import br.com.perguntaloei.TestSupport.answer
import br.com.perguntaloei.data.LocalStore
import br.com.perguntaloei.game.AnswerChoice
import br.com.perguntaloei.game.AnswerMethod
import br.com.perguntaloei.game.GameAction
import br.com.perguntaloei.game.GameEngine
import br.com.perguntaloei.game.GameState
import br.com.perguntaloei.game.NotEnoughQuestionsException
import br.com.perguntaloei.game.Outcome
import br.com.perguntaloei.game.Phase
import br.com.perguntaloei.game.RoundKind
import br.com.perguntaloei.game.TiePurpose
import br.com.perguntaloei.model.Difficulty
import br.com.perguntaloei.model.GameConfig
import br.com.perguntaloei.model.GameMode
import br.com.perguntaloei.model.Player
import br.com.perguntaloei.model.Theme
import br.com.perguntaloei.questions.AgePolicy
import br.com.perguntaloei.questions.TextNormalizer
import br.com.perguntaloei.questions.UsageHistory
import kotlinx.serialization.json.Json
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNotEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertSame
import org.junit.Assert.assertTrue
import org.junit.Test
import java.nio.file.Files
import kotlin.random.Random

class GameEngineTest {

    private val bank = TestSupport.bank
    private var history = UsageHistory.EMPTY
    private val engine = GameEngine(bank, { history }, clock = { 1_000L })

    private fun scores(s: GameState) = s.players.associate { it.id to s.score(it.id) }

    private fun start(config: GameConfig = GameConfig(rounds = 3), players: List<Player> = TestSupport.family, seed: Long = 7) =
        engine.reduce(engine.newGame(config, players, seed), GameAction.BeginRound)

    // ------------------------------------------------------------ ordem das vezes

    @Test
    fun sevenPlayersKeepStrictTurnOrderThroughRandomActions() {
        for (seed in 1L..25L) {
            val rnd = Random(seed)
            var s = engine.newGame(GameConfig(mode = GameMode.THEMED_ROUNDS, rounds = 8), TestSupport.seven, seed)
            val expectedOrder = TestSupport.seven.map { it.id }
            var guard = 0
            while (!s.finished && guard++ < 5000) {
                val before = s
                when (s.phase) {
                    Phase.ROUND_INTRO -> {
                        val r = s.round!!
                        // Rodada normal: todos na ordem oficial. Desempate: só os empatados, também na ordem oficial.
                        val expected = if (r.kind == RoundKind.REGULAR) expectedOrder else expectedOrder.filter { it in s.tie!!.playerIds }
                        assertEquals(expected, r.slots.map { it.playerId })
                        s = engine.reduce(s, GameAction.BeginRound)
                    }
                    Phase.ASKING -> {
                        // A vez é sempre do jogador da posição indicada, na ordem oficial.
                        assertEquals(s.round!!.slots[s.round!!.turnIndex].playerId, s.currentPlayer!!.id)
                        if (s.round!!.kind == RoundKind.REGULAR) assertEquals(expectedOrder[s.round!!.turnIndex], s.currentPlayer!!.id)
                        s = when (rnd.nextInt(10)) {
                            0 -> engine.reduce(s, GameAction.Repeat).also { assertSame(before, it) }
                            1 -> engine.reduce(s, GameAction.Annul(repeated = rnd.nextBoolean()))
                            2 -> engine.reduce(s, GameAction.Skip)
                            3 -> engine.reduce(s, GameAction.NoAnswer)
                            4 -> engine.reduce(s, GameAction.Next).also { assertSame("Next fora de hora", before, it) }
                            else -> engine.answer(s, rnd.nextBoolean())
                        }
                        if (s.phase == Phase.ASKING) assertEquals(before.currentPlayer, s.currentPlayer)
                    }
                    Phase.REVEAL -> {
                        assertEquals(before.currentPlayer, s.currentPlayer)
                        s = if (rnd.nextInt(6) == 0) engine.reduce(s, GameAction.Undo) else engine.reduce(s, GameAction.Next)
                    }
                    Phase.MATCH_END, Phase.GAME_OVER -> {
                        s = if (s.tie != null) engine.reduce(s, if (rnd.nextBoolean()) GameAction.StartTiebreak else GameAction.AcceptTie)
                        else engine.reduce(s, GameAction.NextMatch)
                    }
                }
                assertScoreIsDerivedFromEvaluatedAnswers(s)
            }
            assertTrue("partida terminou (seed $seed)", s.finished)
            // Em cada rodada, os registros seguem a ordem oficial e cada jogador termina com exatamente
            // um resultado válido (resposta, pulo, sem resposta, ou anulação sem substituta).
            val rounds = s.log.filter { it.kind == RoundKind.REGULAR }.map { it.round }.distinct()
            assertEquals("todas as rodadas jogadas (seed $seed)", (1..8).toList(), rounds)
            for (round in rounds) {
                val records = s.log.filter { it.kind == RoundKind.REGULAR && it.round == round }
                assertEquals("rodada $round seed $seed: ${records.map { "${it.playerId}:${it.outcome}:${it.undone}:m${it.match}" }} fim=${s.notice}", expectedOrder, records.map { it.playerId }.distinct())
                for (p in expectedOrder) {
                    val mine = records.filter { it.playerId == p && !it.undone }
                    val finals = mine.filter { it.outcome != Outcome.ANNULLED && it.outcome != Outcome.REPLACED_REPEATED }
                    assertTrue("rodada $round, $p: $mine", finals.size == 1 || (finals.isEmpty() && mine.isNotEmpty()))
                }
            }
            assertNoRepeatedQuestions(s)
            assertAgeAppropriate(s)
        }
    }

    private fun assertScoreIsDerivedFromEvaluatedAnswers(s: GameState) {
        for (p in s.players) {
            val expected = s.log.count {
                it.playerId == p.id && it.match == s.match && it.kind == RoundKind.REGULAR && !it.undone && it.outcome == Outcome.CORRECT
            }
            assertEquals(expected, s.score(p.id))
        }
        assertTrue(s.log.all { it.points == 0 || (it.outcome == Outcome.CORRECT && it.kind == RoundKind.REGULAR && it.points == 1) })
    }

    private fun assertNoRepeatedQuestions(s: GameState) {
        val ids = s.usedQuestionIds
        assertEquals("perguntas repetidas na partida", ids.size, ids.toSet().size)
        val qs = ids.map { bank.byId.getValue(it) }
        for (i in qs.indices) for (j in i + 1 until qs.size) {
            assertFalse(
                "quase-duplicatas ${qs[i].id} ${qs[j].id}",
                TextNormalizer.isNearDuplicate(qs[i].text, qs[i].answer, qs[j].text, qs[j].answer),
            )
        }
    }

    private fun assertAgeAppropriate(s: GameState) {
        for (r in s.log) {
            val p = s.player(r.playerId)!!
            val q = bank.byId.getValue(r.questionId)
            assertTrue("${q.id} (${q.minAge}+) para ${p.name} (${p.age})", AgePolicy.ageAllows(q, p.age))
            val age = p.age
            if (age != null && age < 10) assertTrue("${q.id} ${q.difficulty} para criança de $age", q.difficulty.level <= Difficulty.MEDIA.level)
        }
    }

    @Test
    fun themedRoundGivesEveryoneTheSameThemeBeforeChanging() {
        var s = engine.newGame(GameConfig(mode = GameMode.THEMED_ROUNDS, rounds = 6), TestSupport.seven, 3)
        val themes = mutableListOf<Theme>()
        while (!s.finished) {
            when (s.phase) {
                Phase.ROUND_INTRO -> {
                    val r = s.round!!
                    assertNotNull(r.theme)
                    assertTrue(r.slots.all { bank.byId.getValue(it.questionId).theme == r.theme })
                    themes += r.theme!!
                    s = engine.reduce(s, GameAction.BeginRound)
                }
                Phase.ASKING -> s = engine.answer(s, true)
                Phase.REVEAL -> s = engine.reduce(s, GameAction.Next)
                else -> s = engine.reduce(s, GameAction.AcceptTie)
            }
        }
        assertEquals("um tema por rodada, sem repetir", themes.size, themes.toSet().size)
    }

    // ------------------------------------------------------------ placar

    @Test
    fun scoreChangesOnlyAfterAnEvaluatedAnswer() {
        var s = start()
        val base = scores(s)
        val unchangedBy = listOf(GameAction.Repeat, GameAction.Next, GameAction.Undo, GameAction.BeginRound, GameAction.NextMatch, GameAction.AcceptTie)
        for (a in unchangedBy) assertEquals(a.toString(), base, scores(engine.reduce(s, a)))
        assertEquals(base, scores(engine.reduce(s, GameAction.Annul())))
        assertEquals(base, scores(engine.reduce(s, GameAction.Skip)))
        assertEquals(base, scores(engine.reduce(s, GameAction.NoAnswer)))
        assertEquals(base, scores(engine.answer(s, correct = false)))

        val current = s.currentPlayer!!.id
        s = engine.answer(s, correct = true)
        val after = scores(s)
        assertEquals(1, after.getValue(current))
        s.players.filter { it.id != current }.forEach { assertEquals(0, after.getValue(it.id)) }
    }

    @Test
    fun repeatIsNotAnAnswerAndChangesNothing() {
        val s = start()
        assertSame(s, engine.reduce(s, GameAction.Repeat))
        val revealed = engine.answer(s, true)
        assertSame(revealed, engine.reduce(revealed, GameAction.Repeat))
    }

    @Test
    fun cannotAdvanceBeforeTheAnswerIsEvaluated() {
        val s = start()
        assertEquals(Phase.ASKING, s.phase)
        assertSame(s, engine.reduce(s, GameAction.Next))
        val revealed = engine.answer(s, true)
        // Depois de avaliada, não aceita outra resposta para a mesma pergunta.
        assertSame(revealed, engine.answer(revealed, true))
        val next = engine.reduce(revealed, GameAction.Next)
        assertNotEquals(s.currentPlayer, next.currentPlayer)
        assertEquals(TestSupport.family[1].id, next.currentPlayer!!.id)
    }

    @Test
    fun undoFixesTheLastResultOnlyForThatPlayer() {
        var s = start(players = TestSupport.family)
        s = engine.answer(s, true) // Paula +1
        s = engine.reduce(s, GameAction.Next)
        s = engine.answer(s, true) // Katharina +1
        assertEquals(1, s.score("p2"))
        val undone = engine.reduce(s, GameAction.Undo)
        assertEquals(Phase.ASKING, undone.phase)
        assertEquals("p2", undone.currentPlayer!!.id)
        assertEquals(0, undone.score("p2"))
        assertEquals("pontos de outro jogador não mudam", 1, undone.score("p1"))
        assertTrue(undone.log.last().undone)
        // Pode responder de novo a mesma pergunta.
        assertEquals(s.round!!.currentSlot!!.questionId, undone.round!!.currentSlot!!.questionId)
        val again = engine.answer(undone, false)
        assertEquals(0, again.score("p2"))
        // Só o último resultado pode ser desfeito, e só na tela de resultado.
        assertSame(undone, engine.reduce(undone, GameAction.Undo))
    }

    @Test
    fun annulReplacesTheQuestionWithoutTouchingTheScore() {
        var s = start()
        s = engine.answer(s, true)
        s = engine.reduce(s, GameAction.Next)
        val before = s
        val oldQ = s.round!!.currentSlot!!.questionId
        s = engine.reduce(s, GameAction.Annul())
        assertEquals(Phase.ASKING, s.phase)
        assertEquals(before.currentPlayer, s.currentPlayer)
        val newQ = s.round!!.currentSlot!!.questionId
        assertNotEquals(oldQ, newQ)
        assertEquals(before.round!!.theme, bank.byId.getValue(newQ).theme)
        assertEquals(scores(before), scores(s))
        assertEquals(Outcome.ANNULLED, s.log.last().outcome)
        assertTrue(oldQ in s.usedQuestionIds && newQ in s.usedQuestionIds)

        // Anular depois de um acerto exibido invalida aquele ponto (jogador errado / pergunta interrompida).
        val scored = engine.answer(s, true)
        assertEquals(scores(before)[s.currentPlayer!!.id]!! + 1, scored.score(s.currentPlayer!!.id))
        val voided = engine.reduce(scored, GameAction.Annul(repeated = true))
        assertEquals(scores(before), scores(voided))
        assertEquals(Outcome.REPLACED_REPEATED, voided.log.last().outcome)
    }

    @Test
    fun invalidActionsAreIgnored() {
        val intro = engine.newGame(GameConfig(rounds = 2), TestSupport.family, 11)
        assertEquals(Phase.ROUND_INTRO, intro.phase)
        assertSame(intro, engine.answer(intro, true))
        assertSame(intro, engine.reduce(intro, GameAction.Skip))
        assertSame(intro, engine.reduce(intro, GameAction.Undo))
        val s = engine.reduce(intro, GameAction.BeginRound)
        val q = engine.currentQuestion(s)!!
        if (q.format != br.com.perguntaloei.model.QuestionFormat.OPEN) {
            assertSame(s, engine.reduce(s, GameAction.SubmitAnswer(AnswerChoice.Option(99), AnswerMethod.TOUCH)))
        }
    }

    // ------------------------------------------------------------ perguntas e histórico

    @Test
    fun usedQuestionsDoNotReturnInLaterGames() {
        val used = mutableSetOf<String>()
        repeat(3) { game ->
            history = UsageHistory(used.toSet(), used.map { TextNormalizer.fingerprint(bank.byId.getValue(it).text) }.toSet())
            var s = engine.newGame(GameConfig(rounds = 5), TestSupport.family, 100L + game)
            while (!s.finished) {
                s = when (s.phase) {
                    Phase.ROUND_INTRO -> engine.reduce(s, GameAction.BeginRound)
                    Phase.ASKING -> engine.answer(s, false)
                    Phase.REVEAL -> engine.reduce(s, GameAction.Next)
                    else -> engine.reduce(s, GameAction.AcceptTie)
                }
            }
            val ids = s.usedQuestionIds
            assertTrue("pergunta de partida anterior voltou: ${ids.intersect(used)}", ids.none { it in used })
            used += ids
        }
    }

    @Test
    fun reportedQuestionsAreNeverPickedEvenWhenReusingHistory() {
        // Metade do banco reportada e o resto já usado: só pode sair pergunta não reportada.
        val blocked = bank.questions.filterIndexed { i, _ -> i % 2 == 0 }.map { it.id }.toSet()
        history = UsageHistory(bank.questions.map { it.id }.toSet(), emptySet(), blocked)
        repeat(5) { seed ->
            var s = engine.newGame(GameConfig(rounds = 3), TestSupport.family, 900L + seed)
            while (!s.finished) {
                s = when (s.phase) {
                    Phase.ROUND_INTRO -> engine.reduce(s, GameAction.BeginRound)
                    Phase.ASKING -> engine.answer(s, true)
                    Phase.REVEAL -> engine.reduce(s, GameAction.Next)
                    else -> engine.reduce(s, GameAction.AcceptTie)
                }
            }
            assertTrue("reportada saiu: ${s.usedQuestionIds.intersect(blocked)}", s.usedQuestionIds.none { it in blocked })
        }
    }

    @Test
    fun whenFreshQuestionsRunOutTheReuseIsFlagged() {
        // Histórico com TODAS as perguntas: o jogo continua, mas marca como já usada (nunca como inédita).
        history = UsageHistory(bank.questions.map { it.id }.toSet(), emptySet())
        val s = engine.newGame(GameConfig(rounds = 1), TestSupport.family, 5)
        assertTrue(s.round!!.slots.all { it.reusedFromHistory })
        assertNotNull(s.notice)
    }

    @Test
    fun rewordedQuestionIsDetectedThroughHistoryFingerprint() {
        val q = bank.questions.first { it.id == "geo-001" }
        // Histórico de uma versão antiga do banco, com outro id e texto levemente diferente.
        val reworded = "Qual a capital do Brasil?"
        history = UsageHistory(setOf("id-antigo"), setOf(TextNormalizer.fingerprint(reworded)))
        assertTrue(engine.selector.usedInHistory(q, history))
    }

    @Test
    fun childrenReceiveAgeAppropriateQuestions() {
        val kid = Player("k", "Lia", 6)
        val config = GameConfig(difficulties = setOf(Difficulty.MUITO_DIFICIL))
        for (t in Theme.entries) {
            repeat(5) { i ->
                val pick = engine.selector.pick(kid, t, config, emptySet(), UsageHistory.EMPTY, Random(i))
                assertNotNull("sem pergunta infantil em $t", pick)
                assertTrue(pick!!.question.minAge <= 6)
                assertEquals(Difficulty.FACIL, pick.question.difficulty)
            }
        }
        val adult = Player("a", "Vilma", 63)
        val adultPick = engine.selector.pick(adult, Theme.HISTORIA, config, emptySet(), UsageHistory.EMPTY, Random(1))!!
        assertEquals(Difficulty.MUITO_DIFICIL, adultPick.question.difficulty)
    }

    @Test
    fun preferredDifficultiesByAge() {
        val all = Difficulty.entries.toSet()
        assertEquals(listOf(Difficulty.FACIL), AgePolicy.preferredDifficulties(7, all))
        assertEquals(listOf(Difficulty.FACIL, Difficulty.MEDIA), AgePolicy.preferredDifficulties(11, all))
        assertFalse(Difficulty.MUITO_DIFICIL in AgePolicy.preferredDifficulties(14, all))
        assertEquals(Difficulty.entries, AgePolicy.preferredDifficulties(null, all))
    }

    // ------------------------------------------------------------ modos

    private fun playToEnd(start: GameState, tie: GameAction = GameAction.AcceptTie, correctFor: (GameState) -> Boolean): GameState {
        var s = start
        var guard = 0
        while (!s.finished && guard++ < 2000) {
            s = when (s.phase) {
                Phase.ROUND_INTRO -> engine.reduce(s, GameAction.BeginRound)
                Phase.ASKING -> engine.answer(s, correctFor(s))
                Phase.REVEAL -> engine.reduce(s, GameAction.Next)
                Phase.MATCH_END -> if (s.tie != null) engine.reduce(s, tie) else engine.reduce(s, GameAction.NextMatch)
                Phase.GAME_OVER -> engine.reduce(s, tie)
            }
        }
        return s
    }

    @Test
    fun questionCountModeGivesEachPlayerTheChosenNumberOfQuestions() {
        val s = playToEnd(engine.newGame(GameConfig(mode = GameMode.QUESTION_COUNT, rounds = 4), TestSupport.family, 9)) { it.currentPlayer!!.id == "p1" }
        for (p in TestSupport.family) assertEquals(4, s.log.count { it.playerId == p.id && it.kind == RoundKind.REGULAR })
        assertEquals(listOf("p1"), s.winners)
        assertEquals(4, s.score("p1"))
    }

    @Test
    fun brazilModeOnlyAsksAboutBrazil() {
        val s = playToEnd(engine.newGame(GameConfig(mode = GameMode.BRAZIL, rounds = 6), TestSupport.seven, 21)) { false }
        assertTrue(s.usedQuestionIds.all { bank.byId.getValue(it).brazil })
    }

    @Test
    fun tieOffersAFreshTiebreakQuestion() {
        var s = engine.newGame(GameConfig(rounds = 1), TestSupport.family.take(2), 4)
        s = playUntilPhase(s, Phase.GAME_OVER) { true } // os dois acertam: empate 1 x 1
        assertNotNull(s.tie)
        assertEquals(TiePurpose.FINAL, s.tie!!.purpose)
        assertFalse(s.finished)
        val usedBefore = s.usedQuestionIds.toSet()
        s = engine.reduce(s, GameAction.StartTiebreak)
        assertEquals(Phase.ROUND_INTRO, s.phase)
        assertEquals(RoundKind.TIEBREAK, s.round!!.kind)
        assertTrue(s.round!!.slots.none { it.questionId in usedBefore })
        val scoresBefore = scores(s)
        s = engine.reduce(s, GameAction.BeginRound)
        s = engine.answer(s, true) // p1 acerta
        s = engine.reduce(s, GameAction.Next)
        s = engine.answer(s, false) // p2 erra
        assertEquals("desempate não altera o placar", scoresBefore, scores(s))
        s = engine.reduce(s, GameAction.Next)
        assertTrue(s.finished)
        assertEquals(listOf("p1"), s.winners)
    }

    @Test
    fun acceptingATieSharesTheVictory() {
        var s = engine.newGame(GameConfig(rounds = 1), TestSupport.family.take(3), 4)
        s = playUntilPhase(s, Phase.GAME_OVER) { it.currentPlayer!!.id != "p3" }
        s = engine.reduce(s, GameAction.AcceptTie)
        assertTrue(s.finished)
        assertEquals(listOf("p1", "p2"), s.winners)
    }

    private fun playUntilPhase(start: GameState, phase: Phase, correct: (GameState) -> Boolean): GameState {
        var s = start
        while (s.phase != phase) {
            s = when (s.phase) {
                Phase.ROUND_INTRO -> engine.reduce(s, GameAction.BeginRound)
                Phase.ASKING -> engine.answer(s, correct(s))
                Phase.REVEAL -> engine.reduce(s, GameAction.Next)
                else -> engine.reduce(s, GameAction.NextMatch)
            }
        }
        return s
    }

    @Test
    fun bestOfThreeChampionIsFirstToTwoMatchWins() {
        val cfg = GameConfig(mode = GameMode.BEST_OF_THREE, roundsPerMatch = 2)
        var s = engine.newGame(cfg, TestSupport.family.take(3), 8)
        s = playUntilPhase(s, Phase.MATCH_END) { it.currentPlayer!!.id == "p2" }
        assertEquals(listOf(listOf("p2")), s.matchWinners)
        assertFalse(s.finished)
        s = engine.reduce(s, GameAction.NextMatch)
        assertEquals(2, s.match)
        assertEquals("placar da partida recomeça", 0, s.score("p2"))
        assertEquals(2, s.score("p2", inMatch = 1))
        s = playToEnd(s) { it.currentPlayer!!.id == "p2" }
        assertTrue(s.finished)
        assertEquals(listOf("p2"), s.winners)
        assertEquals(2, s.matchWins("p2"))
        assertEquals(2, s.match)
    }

    @Test
    fun bestOfThreeWithThreeDifferentWinnersGoesToTiebreak() {
        val cfg = GameConfig(mode = GameMode.BEST_OF_THREE, roundsPerMatch = 1)
        var s = engine.newGame(cfg, TestSupport.family.take(3), 12)
        for ((i, winner) in listOf("p1", "p2", "p3").withIndex()) {
            s = playUntilPhase(s, if (i < 2) Phase.MATCH_END else Phase.GAME_OVER) { it.currentPlayer!!.id == winner }
            if (i < 2) s = engine.reduce(s, GameAction.NextMatch)
        }
        assertEquals(TiePurpose.FINAL, s.tie!!.purpose)
        assertEquals(listOf("p1", "p2", "p3"), s.tie!!.playerIds)
    }

    @Test
    fun endEarlyKeepsScoresAndFinishes() {
        var s = start()
        s = engine.answer(s, true)
        s = engine.reduce(s, GameAction.EndEarly)
        assertTrue(s.finished)
        assertEquals(listOf("p1"), s.winners)
        assertNull(s.round)
    }

    @Test
    fun noPlayersOrNoThemesIsRejected() {
        try {
            engine.newGame(GameConfig(themes = emptyList()), TestSupport.family)
            error("deveria falhar")
        } catch (e: NotEnoughQuestionsException) {
            assertTrue(e.message!!.isNotBlank())
        }
        try {
            engine.newGame(GameConfig(), emptyList())
            error("deveria falhar")
        } catch (e: IllegalArgumentException) {
            assertTrue(e.message!!.isNotBlank())
        }
    }

    @Test
    fun themeWithoutEnoughQuestionsIsReplacedAndAnnounced() {
        // Esgota o tema Novelas no histórico: a rodada usa outro tema e avisa o grupo.
        history = UsageHistory(bank.questions.filter { it.theme == Theme.NOVELAS }.map { it.id }.toSet(), emptySet())
        val s = engine.newGame(GameConfig(themes = listOf(Theme.NOVELAS, Theme.GEOGRAFIA), rounds = 1), TestSupport.family, 1)
        assertEquals(Theme.GEOGRAFIA, s.round!!.theme)
    }

    // ------------------------------------------------------------ persistência

    @Test
    fun gameStateSurvivesSerializationAndDiskRoundTrip() {
        var s = engine.newGame(GameConfig(mode = GameMode.BEST_OF_THREE), TestSupport.seven, 99)
        s = engine.reduce(s, GameAction.BeginRound)
        s = engine.answer(s, true)
        val json = Json { encodeDefaults = true }
        val decoded = json.decodeFromString(GameState.serializer(), json.encodeToString(GameState.serializer(), s))
        assertEquals(s, decoded)

        val dir = Files.createTempDirectory("perguntaloei").toFile()
        val store = LocalStore(dir)
        store.saveGame(s)
        store.savePlayers(TestSupport.seven)
        assertEquals(s, LocalStore(dir).loadGame())
        assertEquals(TestSupport.seven, LocalStore(dir).loadPlayers())
        // A partida continua exatamente de onde parou.
        val resumed = engine.reduce(LocalStore(dir).loadGame()!!, GameAction.Next)
        assertEquals(TestSupport.seven[1].id, resumed.currentPlayer!!.id)
        dir.deleteRecursively()
    }

    @Test
    fun corruptedSaveFileDoesNotCrash() {
        val dir = Files.createTempDirectory("perguntaloei").toFile()
        java.io.File(dir, "partida_atual.json").writeText("{ isto não é json")
        assertNull(LocalStore(dir).loadGame())
        dir.deleteRecursively()
    }

    @Test
    fun usersWithAllOriginalThemesGetTheNewOnes() {
        val old = br.com.perguntaloei.data.AppSettings(lastConfig = GameConfig(themes = Theme.entries.take(15)))
        assertEquals(Theme.entries, migrateThemes(old).lastConfig.themes)
        val partial = br.com.perguntaloei.data.AppSettings(lastConfig = GameConfig(themes = listOf(Theme.GEOGRAFIA)))
        assertEquals(listOf(Theme.GEOGRAFIA), migrateThemes(partial).lastConfig.themes)
    }
}
