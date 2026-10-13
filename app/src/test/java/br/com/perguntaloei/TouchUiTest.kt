package br.com.perguntaloei

import android.graphics.Bitmap
import androidx.compose.ui.test.SemanticsNodeInteraction
import androidx.compose.ui.test.hasContentDescription
import androidx.compose.ui.test.hasSetTextAction
import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.compose.ui.test.onAllNodesWithText
import androidx.compose.ui.test.hasText
import androidx.compose.ui.test.hasAnyAncestor
import androidx.compose.ui.test.isDialog
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import androidx.compose.ui.test.performScrollTo
import androidx.compose.ui.test.performTextInput
import androidx.lifecycle.ViewModelProvider
import androidx.test.ext.junit.runners.AndroidJUnit4
import br.com.perguntaloei.game.Phase
import br.com.perguntaloei.model.GameConfig
import br.com.perguntaloei.model.GameMode
import br.com.perguntaloei.model.QuestionFormat
import br.com.perguntaloei.game.GameAction
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.annotation.Config
import org.robolectric.annotation.GraphicsMode
import java.io.File

/**
 * Partida completa jogada pela interface, só com toques (modo sem voz e sem microfone).
 * Também salva capturas das telas em app/build/telas/.
 */
@RunWith(AndroidJUnit4::class)
@GraphicsMode(GraphicsMode.Mode.NATIVE)
class TouchUiTest {

    private val composeRule = createAndroidComposeRule<MainActivity>()

    /** Liga "Remover animações" antes de abrir a tela (efeitos contínuos ficam parados). */
    @get:Rule
    val chain: org.junit.rules.RuleChain = org.junit.rules.RuleChain
        .outerRule(object : org.junit.rules.ExternalResource() {
            override fun before() {
                android.animation.ValueAnimator::class.java.getMethod("setDurationScale", Float::class.javaPrimitiveType).invoke(null, 0f)
            }
        })
        .around(composeRule)

    private val rule get() = composeRule

    private val vm: AppViewModel by lazy { ViewModelProvider(rule.activity)[AppViewModel::class.java] }

    private fun settle() = rule.waitForIdle()

    private fun button(label: String): SemanticsNodeInteraction =
        rule.onNode(hasContentDescription(label, substring = false))

    private fun tap(label: String) {
        val node = button(label)
        runCatching { node.performScrollTo() } // nem todo botão está dentro de uma área rolável
        node.performClick()
        settle()
    }

    /** Desenha a janela inteira num bitmap (gráficos nativos do Robolectric) e salva em build/telas. */
    private fun shot(name: String) {
        settle()
        val activity = rule.activity
        rule.runOnUiThread {
            val view = activity.window.decorView
            val bmp = Bitmap.createBitmap(view.width, view.height, Bitmap.Config.ARGB_8888)
            view.draw(android.graphics.Canvas(bmp))
            val dir = File("build/telas").apply { mkdirs() }
            File(dir, "$name.png").outputStream().use { bmp.compress(Bitmap.CompressFormat.PNG, 100, it) }
        }
    }

    private fun setupPlayers(config: GameConfig) {
        val v = vm // fora da thread principal: obter a Activity espera a interface ficar ociosa
        settle()
        // As perguntas carregam em segundo plano; "Novo jogo" aparece quando terminam.
        val until = System.currentTimeMillis() + 10_000
        while (!v.bankReady && System.currentTimeMillis() < until) { Thread.sleep(20); settle() }
        assertTrue("perguntas não carregaram", v.bankReady)
        // Primeira abertura: o app pede as permissões (só uma vez); aqui seguimos só com toque.
        if (v.dialog == AppDialog.Permissions) {
            shot("00-permissoes")
            rule.onNodeWithText("Agora não (só toque)").performClick()
            settle()
        }
        assertTrue(v.settings.permissionsAsked)
        rule.runOnUiThread {
            listOf("Paula" to 45, "Katharina" to 39, "Ricardo" to 32, "Vilma" to 63, "Lia" to 6, "Theo" to 9, "Bruno" to 13)
                .filter { (n, _) -> v.players.none { it.name == n } }
                .forEach { (n, a) -> v.addPlayer(n, a) }
            v.players.forEach { v.setPlayerActive(it.id, true) }
            v.updateSettings { it.copy(lastConfig = config) }
        }
        settle()
    }

    @Test
    @Config(qualifiers = "w411dp-h891dp-xxhdpi")
    fun fullTouchOnlyGameOnAPhone() {
        setupPlayers(GameConfig(mode = GameMode.THEMED_ROUNDS, rounds = 2, voiceHost = false, voiceAnswers = false))
        shot("01-inicio")
        tap("Jogadores (7)")
        // Bruno fica fora desta partida, mas continua cadastrado.
        rule.onAllNodes(hasContentDescription("Joga: sim"))[6].performScrollTo().performClick()
        settle()
        assertEquals(listOf(true, true, true, true, true, true, false), vm.players.map { it.active })
        shot("02-jogadores")
        tap("Configurar partida ▶")
        shot("03-configuracao")
        tap("COMEÇAR!")
        assertEquals(Screen.GAME, vm.screen)
        shot("04-rodada")

        val order = vm.players.filter { it.active }.map { it.name }
        assertEquals(6, vm.game!!.players.size)
        assertTrue("Bruno não joga", vm.game!!.players.none { it.name == "Bruno" })
        var turns = 0
        var guard = 0
        var shotAsk = false
        var shotReveal = false
        while (!vm.game!!.finished && guard++ < 100) {
            val g = vm.game!!
            when (g.phase) {
                Phase.ROUND_INTRO -> tap("Começar rodada ▶")
                Phase.ASKING -> {
                    // O jogador da vez aparece na tela e segue a ordem cadastrada.
                    val name = g.currentPlayer!!.name
                    assertEquals(order[turns % order.size], name)
                    assertTrue(rule.onAllNodesWithText(name.uppercase()).fetchSemanticsNodes().isNotEmpty())
                    val q = vm.engine.currentQuestion(g)!!
                    if (!shotAsk) { shot("05-pergunta"); shotAsk = true }
                    // Alterna acertos e erros: só a resposta avaliada muda o placar.
                    val correct = turns % 2 == 0
                    when (q.format) {
                        QuestionFormat.OPEN -> {
                            rule.onNode(hasSetTextAction()).performScrollTo().performTextInput(if (correct) q.answer else "resposta errada")
                            tap("Enviar resposta")
                        }
                        QuestionFormat.MULTIPLE_CHOICE -> {
                            val i = if (correct) q.correctIndex else (q.correctIndex + 1) % q.options.size
                            tap("${'A' + i})  ${q.options[i]}")
                        }
                        QuestionFormat.TRUE_FALSE -> {
                            val i = if (correct) q.correctIndex else 1 - q.correctIndex
                            tap(q.options[i])
                        }
                    }
                    assertEquals(Phase.REVEAL, vm.game!!.phase)
                    turns++
                }
                Phase.REVEAL -> {
                    if (!shotReveal) {
                        shot("06-resultado")
                        shotReveal = true
                        // Reportar a pergunta pela tela: sai do jogo, sem mexer no placar.
                        val before = vm.game!!.players.sumOf { vm.game!!.score(it.id) }
                        rule.onNodeWithText("⚑ Reportar pergunta (errada ou confusa)").performScrollTo().performClick()
                        settle()
                        tap("Resposta errada")
                        assertEquals(1, vm.reports.size)
                        assertEquals(before, vm.game!!.players.sumOf { vm.game!!.score(it.id) })
                        rule.onNodeWithText("⚑ Pergunta reportada: ela não volta mais ao jogo.").assertExists()
                    }
                    tap("Continuar ▶")
                }
                else -> tap("Aceitar empate")
            }
        }
        val end = vm.game!!
        assertTrue(end.finished)
        assertEquals(order.size * 2, turns)
        assertEquals("placar = número de acertos", (turns + 1) / 2, end.players.sumOf { end.score(it.id) })
        shot("07-fim")
        tap("📋 Histórico")
        shot("08-historico")
    }

    /** Configurações abre sem travar (contagem em segundo plano) e apaga o histórico de partidas. */
    @Test
    @Config(qualifiers = "w411dp-h891dp-xxhdpi")
    fun settingsOpensAndDeletesTheMatchHistory() {
        setupPlayers(GameConfig(mode = GameMode.THEMED_ROUNDS, rounds = 1, voiceHost = false, voiceAnswers = false))
        val v = vm
        rule.runOnUiThread { v.startNewGame(v.settings.lastConfig) }
        settle()
        rule.runOnUiThread { v.dispatch(GameAction.EndEarly) }
        rule.waitUntil(5000) { v.summaries.isNotEmpty() }
        rule.runOnUiThread { v.go(Screen.HOME) }
        settle()
        val start = System.currentTimeMillis()
        tap("Configurações")
        assertTrue("abrir Configurações levou ${System.currentTimeMillis() - start} ms", System.currentTimeMillis() - start < 5000)
        val until = System.currentTimeMillis() + 10_000
        while (v.themeStats == null && System.currentTimeMillis() < until) { Thread.sleep(20); settle() }
        assertTrue("contagem por tema não chegou", v.themeStats != null)
        rule.onNodeWithText("Apagar histórico de partidas").performScrollTo()
        shot("09-configuracoes")
        rule.onNodeWithText("Apagar histórico de partidas").performClick()
        settle()
        rule.onNode(hasText("Apagar") and hasAnyAncestor(isDialog())).performClick()
        settle()
        assertTrue(v.summaries.isEmpty())
        rule.onNodeWithText("Nenhuma partida terminada guardada.").assertExists()
    }

    @Test
    @Config(qualifiers = "w1280dp-h800dp-land-mdpi")
    fun tabletLayoutShowsQuestionAndScoreboardSideBySide() {
        setupPlayers(GameConfig(mode = GameMode.BEST_OF_THREE, roundsPerMatch = 2, voiceHost = false, voiceAnswers = false))
        tap("Novo jogo")
        tap("COMEÇAR!")
        tap("Começar rodada ▶")
        assertEquals(Phase.ASKING, vm.game!!.phase)
        shot("09-tablet-pergunta")
        assertTrue(rule.onAllNodesWithText("CAMPEONATO").fetchSemanticsNodes().isNotEmpty())
    }
}
