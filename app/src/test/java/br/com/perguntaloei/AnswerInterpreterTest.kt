package br.com.perguntaloei

import br.com.perguntaloei.game.AnswerChoice
import br.com.perguntaloei.game.AnswerInterpreter
import br.com.perguntaloei.game.AnswerMatcher
import br.com.perguntaloei.game.CommandKind
import br.com.perguntaloei.game.Interpretation
import br.com.perguntaloei.game.NumberWords
import br.com.perguntaloei.game.Transcript
import br.com.perguntaloei.model.Difficulty
import br.com.perguntaloei.model.Question
import br.com.perguntaloei.model.QuestionFormat
import br.com.perguntaloei.model.Theme
import br.com.perguntaloei.questions.QuestionBank
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class AnswerInterpreterTest {

    private val capital = Question(
        id = "t1", text = "Qual é a capital do Brasil?", theme = Theme.GEOGRAFIA, subtheme = "capitais",
        difficulty = Difficulty.FACIL, format = QuestionFormat.MULTIPLE_CHOICE,
        options = listOf("Brasília", "Rio de Janeiro", "São Paulo", "Salvador"), answer = "Brasília",
        explanation = "x", source = "y",
    )
    private val lua = Question(
        id = "t2", text = "A Lua tem luz própria.", theme = Theme.CIENCIA, subtheme = "astronomia",
        difficulty = Difficulty.FACIL, format = QuestionFormat.TRUE_FALSE, options = QuestionBank.TRUE_FALSE_OPTIONS,
        answer = "Falso", explanation = "x", source = "y",
    )
    private val autor = Question(
        id = "t3", text = "Quem escreveu Dom Casmurro?", theme = Theme.LITERATURA, subtheme = "romance",
        difficulty = Difficulty.MEDIA, format = QuestionFormat.OPEN, answer = "Machado de Assis",
        synonyms = listOf("machado"), explanation = "x", source = "y",
    )

    private fun voice(q: Question, text: String, confidence: Float? = 0.9f) =
        AnswerInterpreter.interpret(q, listOf(Transcript(text, confidence)))

    private fun assertClearOption(i: Interpretation, index: Int) {
        assertTrue("esperava resposta clara, veio $i", i is Interpretation.Clear)
        assertEquals(AnswerChoice.Option(index), (i as Interpretation.Clear).choice)
    }

    @Test
    fun letterAndOptionTextAreClearAnswers() {
        assertClearOption(voice(capital, "letra B"), 1)
        assertClearOption(voice(capital, "alternativa d"), 3)
        assertClearOption(voice(capital, "b"), 1)
        assertClearOption(voice(capital, "é a c"), 2)
        assertClearOption(voice(capital, "Brasília"), 0)
        assertClearOption(voice(capital, "minha resposta é Rio de Janeiro"), 1)
        assertClearOption(voice(capital, "a segunda"), 1)
    }

    @Test
    fun articleAIsNotTakenAsLetterA() {
        // "a" como artigo antes do nome da alternativa não vira "letra A".
        assertClearOption(voice(capital, "é a São Paulo"), 2)
    }

    @Test
    fun hesitationNeedsConfirmation() {
        val i = voice(capital, "acho que é Brasília")
        assertTrue(i is Interpretation.NeedsConfirmation)
        assertEquals(AnswerChoice.Option(0), (i as Interpretation.NeedsConfirmation).choice)
        assertTrue(voice(capital, "será que é Salvador") is Interpretation.NeedsConfirmation)
    }

    @Test
    fun lowConfidenceNeedsConfirmation() {
        assertTrue(voice(capital, "Brasília", confidence = 0.3f) is Interpretation.NeedsConfirmation)
    }

    @Test
    fun alwaysConfirmSettingForcesConfirmation() {
        val i = AnswerInterpreter.interpret(capital, listOf(Transcript("letra a", 0.95f)), alwaysConfirm = true)
        assertTrue(i is Interpretation.NeedsConfirmation)
    }

    @Test
    fun mentioningTwoOptionsIsAmbiguous() {
        assertTrue(voice(capital, "Brasília ou Salvador") is Interpretation.Ambiguous)
        assertTrue(voice(capital, "letra a ou letra c") is Interpretation.Ambiguous)
    }

    @Test
    fun negatedMentionIsNotAnAnswer() {
        val i = voice(capital, "não é Brasília")
        assertFalse(i is Interpretation.Clear)
        assertFalse(i is Interpretation.NeedsConfirmation)
    }

    @Test
    fun commentsAndRepeatRequestsAreNotAnswers() {
        assertEquals(CommandKind.REPEAT, (voice(capital, "repete") as Interpretation.Command).kind)
        assertEquals(CommandKind.REPEAT, (voice(capital, "pode repetir por favor") as Interpretation.Command).kind)
        assertEquals(CommandKind.REPEAT, (voice(capital, "não entendi") as Interpretation.Command).kind)
        assertEquals(CommandKind.SKIP, (voice(capital, "passo") as Interpretation.Command).kind)
        assertEquals(CommandKind.DONT_KNOW, (voice(capital, "não sei") as Interpretation.Command).kind)
        assertTrue(voice(capital, "hmm deixa eu pensar") is Interpretation.Unclear)
        assertTrue(voice(capital, "nossa que difícil essa") is Interpretation.Unclear)
    }

    @Test
    fun emptyOrSilentInputIsUnclear() {
        assertTrue(AnswerInterpreter.interpret(capital, emptyList()) is Interpretation.Unclear)
        assertTrue(voice(capital, "   ") is Interpretation.Unclear)
    }

    @Test
    fun otherHypothesesAreUsedOnlyWithConfirmation() {
        val i = AnswerInterpreter.interpret(capital, listOf(Transcript("brasa lia", null), Transcript("Brasília", null)))
        assertTrue("$i", i is Interpretation.NeedsConfirmation)
    }

    @Test
    fun trueFalseAnswers() {
        assertClearOption(voice(lua, "verdadeiro"), 0)
        assertClearOption(voice(lua, "é falso"), 1)
        assertClearOption(voice(lua, "não é verdade"), 1)
        assertTrue(voice(lua, "sim") is Interpretation.NeedsConfirmation)
        assertTrue(voice(lua, "verdadeiro ou falso") is Interpretation.Ambiguous)
    }

    @Test
    fun openAnswersUseSynonymsAndAskWhenUnclear() {
        assertTrue(voice(autor, "Machado de Assis") is Interpretation.Clear)
        assertTrue(voice(autor, "machado") is Interpretation.Clear)
        // Resposta diferente falada: confirma a transcrição antes de marcar errado.
        assertTrue(voice(autor, "José de Alencar") is Interpretation.NeedsConfirmation)
        // Quase igual (provável erro de transcrição/grafia): pede esclarecimento, não marca certo nem errado.
        val close = AnswerInterpreter.interpretTyped(autor, "Machado de Asis")
        assertTrue("$close", close is Interpretation.Ambiguous && close.allowGroupDecision)
        assertTrue(AnswerInterpreter.interpretTyped(autor, "Jorge Amado") is Interpretation.Clear)
    }

    @Test
    fun openAnswerMatcher() {
        assertTrue(AnswerMatcher.isCorrectOpen("a resposta é Machado de Assis", autor))
        assertTrue(AnswerMatcher.isCorrectOpen("MACHADO DE ASSIS!", autor))
        assertFalse(AnswerMatcher.isCorrectOpen("não é Machado de Assis", autor))
        assertFalse(AnswerMatcher.isCorrectOpen("José de Alencar", autor))
    }

    @Test
    fun extraWordsAroundASynonymAreNotAccepted() {
        val rio = autor.copy(answer = "Rio de Janeiro", synonyms = listOf("rio"))
        assertTrue(AnswerMatcher.isCorrectOpen("acho que é o Rio mesmo", rio))
        assertFalse(AnswerMatcher.isCorrectOpen("Rio Grande do Sul", rio))
        assertFalse(AnswerMatcher.isCorrectOpen("José Machado", autor))
    }

    @Test
    fun ordinalsNeedContext() {
        val dias = capital.copy(options = listOf("Segunda-feira", "Sábado", "Terça-feira", "Sexta-feira"), answer = "Segunda-feira")
        assertClearOption(voice(dias, "segunda-feira"), 0)
        assertTrue(voice(dias, "terça") is Interpretation.NeedsConfirmation)
        assertClearOption(voice(capital, "a terceira alternativa"), 2)
        assertClearOption(voice(capital, "a terceira"), 2)
    }

    @Test
    fun spokenNumbersBecomeDigits() {
        assertEquals("1822", NumberWords.replace("mil oitocentos e vinte e dois"))
        assertEquals("7 a 1", NumberWords.replace("7 a 1"))
        assertEquals("o ano 1500", NumberWords.replace("o ano mil e quinhentos"))
        assertEquals("um gato", NumberWords.replace("um gato"))
        val anos = TestSupport.bank.byId.values.first { it.answer == "1822" }
        assertClearOption(voice(anos, "mil oitocentos e vinte e dois"), anos.correctIndex)
    }

    @Test
    fun everyBankAnswerIsRecognizedWhenSpokenExactly() {
        // Falar exatamente a resposta (ou a letra certa) sempre é entendido como a alternativa correta.
        for (q in TestSupport.bank.questions) {
            val i = voice(q, q.answer)
            when (q.format) {
                QuestionFormat.OPEN -> assertTrue("${q.id}: $i", i is Interpretation.Clear)
                else -> {
                    assertTrue("${q.id}: '${q.answer}' -> $i", i is Interpretation.Clear)
                    assertEquals(q.id, AnswerChoice.Option(q.correctIndex), (i as Interpretation.Clear).choice)
                }
            }
            if (q.format == QuestionFormat.MULTIPLE_CHOICE) {
                assertClearOption(voice(q, "letra ${'a' + q.correctIndex}"), q.correctIndex)
            }
        }
    }
}
