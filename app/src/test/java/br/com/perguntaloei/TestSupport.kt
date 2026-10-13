package br.com.perguntaloei

import br.com.perguntaloei.game.AnswerChoice
import br.com.perguntaloei.game.AnswerMethod
import br.com.perguntaloei.game.GameAction
import br.com.perguntaloei.game.GameEngine
import br.com.perguntaloei.game.GameState
import br.com.perguntaloei.model.Player
import br.com.perguntaloei.model.Question
import br.com.perguntaloei.model.QuestionFormat
import br.com.perguntaloei.questions.QuestionBank
import java.io.File

object TestSupport {
    /** Banco real que vai dentro do APK. */
    val bank: QuestionBank by lazy {
        val f = listOf(File("src/main/assets/questions.json"), File("app/src/main/assets/questions.json")).first { it.exists() }
        QuestionBank.fromJson(f.readText())
    }

    val family = listOf(
        Player("p1", "Paula", 45),
        Player("p2", "Katharina", 39),
        Player("p3", "Ricardo", 32),
        Player("p4", "Vilma", 63),
    )

    /** Sete jogadores com crianças e adolescentes misturados a adultos. */
    val seven = family + listOf(
        Player("p5", "Lia", 6),
        Player("p6", "Theo", 9),
        Player("p7", "Bruno", 13),
    )

    fun correctChoice(q: Question): AnswerChoice = when (q.format) {
        QuestionFormat.OPEN -> AnswerChoice.Text(q.answer)
        else -> AnswerChoice.Option(q.correctIndex)
    }

    fun wrongChoice(q: Question): AnswerChoice = when (q.format) {
        QuestionFormat.OPEN -> AnswerChoice.Text("zzz resposta errada")
        else -> AnswerChoice.Option((q.correctIndex + 1) % q.options.size)
    }

    fun GameEngine.answer(state: GameState, correct: Boolean, method: AnswerMethod = AnswerMethod.TOUCH): GameState {
        val q = currentQuestion(state)!!
        return reduce(state, GameAction.SubmitAnswer(if (correct) correctChoice(q) else wrongChoice(q), method))
    }
}
