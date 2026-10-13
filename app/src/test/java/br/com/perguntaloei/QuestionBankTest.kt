package br.com.perguntaloei

import br.com.perguntaloei.model.Difficulty
import br.com.perguntaloei.model.QuestionFormat
import br.com.perguntaloei.model.Theme
import br.com.perguntaloei.questions.QuestionBank
import br.com.perguntaloei.questions.TextNormalizer
import br.com.perguntaloei.questions.QuestionSelector
import br.com.perguntaloei.questions.UsageHistory
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
        assertEquals(emptyMap<String, Set<String>>(), QuestionBank.findNearDuplicates(bank.questions))
    }

    @Test
    fun nearDuplicateDetectionCatchesSmallRewordings() {
        assertTrue(TextNormalizer.isNearDuplicate("Qual é a capital do Brasil?", "Brasília", "Qual a capital do Brasil?", "Brasília"))
        assertTrue(TextNormalizer.isNearDuplicate("Quem escreveu Dom Casmurro?", "Machado de Assis", "Quem foi que escreveu o livro Dom Casmurro?", "Machado de Assis"))
        assertTrue(!TextNormalizer.isNearDuplicate("Qual é a capital da França?", "Paris", "Qual é o maior oceano do planeta?", "Pacífico"))
    }

    /** A versão rápida dá exatamente o mesmo resultado da regra simples, par a par. */
    @Test
    fun fastNearDuplicateSearchMatchesTheSimpleRule() {
        val base = bank.questions.take(120)
        val extra = listOf(
            base[0].copy(id = "copia-1", text = base[0].text.replace("?", " mesmo?")),
            base[5].copy(id = "copia-2", text = base[5].text.lowercase()),
            base[9].copy(id = "copia-3", text = "Você sabe: " + base[9].text),
        )
        val qs = base + extra
        val naive = HashMap<String, MutableSet<String>>()
        for (i in qs.indices) for (j in i + 1 until qs.size) {
            val a = qs[i]; val b = qs[j]
            val jac = TextNormalizer.jaccard(a.text, b.text)
            val dup = jac >= 0.8 || TextNormalizer.similarity(a.text, b.text) >= 0.85 ||
                (TextNormalizer.normalize(a.answer) == TextNormalizer.normalize(b.answer) && jac >= 0.55)
            if (dup) {
                naive.getOrPut(a.id) { mutableSetOf() }.add(b.id)
                naive.getOrPut(b.id) { mutableSetOf() }.add(a.id)
            }
        }
        assertTrue(naive.keys.containsAll(listOf("copia-1", "copia-2", "copia-3")))
        assertEquals(naive, QuestionBank.findNearDuplicates(qs))
    }

    /** No celular a escolha de perguntas roda na tela: tem de ser rápida mesmo com histórico grande. */
    @Test
    fun pickingQuestionsStaysFastWithABigHistory() {
        val selector = QuestionSelector(bank)
        val used = bank.questions.take(400)
        val history = UsageHistory(used.map { it.id }.toSet(), used.map { TextNormalizer.fingerprint(it.text) }.toSet())
        val player = br.com.perguntaloei.model.Player("p", "Ana", 30)
        val config = br.com.perguntaloei.model.GameConfig()
        selector.pick(player, null, config, emptySet(), history, kotlin.random.Random(1)) // aquece
        val start = System.nanoTime()
        repeat(20) { selector.pick(player, null, config, emptySet(), history, kotlin.random.Random(it)) }
        val perPickMs = (System.nanoTime() - start) / 20 / 1_000_000.0
        assertTrue("escolha levou $perPickMs ms", perPickMs < 50)
    }
}
