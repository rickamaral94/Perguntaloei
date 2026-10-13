package br.com.perguntaloei

import br.com.perguntaloei.model.Difficulty
import br.com.perguntaloei.model.QuestionFormat
import br.com.perguntaloei.model.Theme
import br.com.perguntaloei.questions.QuestionBank
import br.com.perguntaloei.questions.TextNormalizer
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class QuestionBankTest {

    private val bank = TestSupport.bank

    @Test
    fun bankHasAtLeast250ValidQuestions() {
        assertTrue("banco tem ${bank.questions.size} perguntas", bank.questions.size >= 250)
        assertEquals(emptyList<String>(), bank.validate())
    }

    @Test
    fun everyQuestionHasAllRequiredFields() {
        for (q in bank.questions) {
            assertTrue(q.id, q.id.isNotBlank() && q.text.isNotBlank() && q.subtheme.isNotBlank())
            assertTrue(q.id, q.explanation.isNotBlank() && q.source.isNotBlank())
            when (q.format) {
                QuestionFormat.MULTIPLE_CHOICE -> assertTrue(q.id, q.correctIndex >= 0)
                QuestionFormat.TRUE_FALSE -> assertEquals(q.id, QuestionBank.TRUE_FALSE_OPTIONS, q.options)
                QuestionFormat.OPEN -> assertTrue(q.id, q.synonyms.isNotEmpty())
            }
        }
    }

    @Test
    fun allThemesAndDifficultiesAreCovered() {
        for (t in Theme.entries) {
            val inTheme = bank.questions.filter { it.theme == t }
            assertTrue("$t tem ${inTheme.size}", inTheme.size >= 15)
            // Crianças pequenas (6 anos) precisam de perguntas fáceis em todos os temas.
            val kids = inTheme.count { it.difficulty == Difficulty.FACIL && it.minAge <= 6 }
            assertTrue("$t tem $kids perguntas para crianças", kids >= 4)
        }
        for (d in Difficulty.entries) assertTrue(d.name, bank.questions.count { it.difficulty == d } >= 15)
        for (f in QuestionFormat.entries) assertTrue(f.name, bank.questions.any { it.format == f })
        assertTrue("perguntas do Brasil", bank.questions.count { it.brazil } >= 80)
    }

    @Test
    fun bankHasNoNearDuplicates() {
        assertEquals(emptyMap<String, Set<String>>(), bank.nearDuplicates)
    }

    @Test
    fun nearDuplicateDetectionCatchesSmallRewordings() {
        assertTrue(TextNormalizer.isNearDuplicate("Qual é a capital do Brasil?", "Brasília", "Qual a capital do Brasil?", "Brasília"))
        assertTrue(TextNormalizer.isNearDuplicate("Quem escreveu Dom Casmurro?", "Machado de Assis", "Quem foi que escreveu o livro Dom Casmurro?", "Machado de Assis"))
        assertTrue(!TextNormalizer.isNearDuplicate("Qual é a capital da França?", "Paris", "Qual é o maior oceano do planeta?", "Pacífico"))
    }
}
