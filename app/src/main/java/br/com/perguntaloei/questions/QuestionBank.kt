package br.com.perguntaloei.questions

import br.com.perguntaloei.model.Question
import br.com.perguntaloei.model.QuestionFormat
import br.com.perguntaloei.model.Theme
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json

@Serializable
private data class QuestionFile(val version: Int, val questions: List<Question>)

/** Banco de perguntas embutido no app. Imutável depois de carregado. */
class QuestionBank(val questions: List<Question>) {

    val byId: Map<String, Question> = questions.associateBy { it.id }

    /** Para cada pergunta, os ids de outras perguntas consideradas essencialmente iguais. */
    val nearDuplicates: Map<String, Set<String>> by lazy {
        val result = HashMap<String, MutableSet<String>>()
        for (i in questions.indices) {
            for (j in i + 1 until questions.size) {
                val a = questions[i]
                val b = questions[j]
                if (TextNormalizer.isNearDuplicate(a.text, a.answer, b.text, b.answer)) {
                    result.getOrPut(a.id) { mutableSetOf() }.add(b.id)
                    result.getOrPut(b.id) { mutableSetOf() }.add(a.id)
                }
            }
        }
        result
    }

    val fingerprints: Map<String, String> by lazy { questions.associate { it.id to TextNormalizer.fingerprint(it.text) } }

    fun themesWithQuestions(brazilOnly: Boolean): List<Theme> =
        Theme.entries.filter { t -> questions.any { it.theme == t && (!brazilOnly || it.brazil) } }

    /** Lista de problemas encontrados no banco (vazia = banco válido). */
    fun validate(): List<String> {
        val problems = mutableListOf<String>()
        val seen = HashSet<String>()
        for (q in questions) {
            val tag = "[${q.id}]"
            if (!seen.add(q.id)) problems += "$tag id duplicado"
            if (q.text.isBlank()) problems += "$tag enunciado vazio"
            if (q.answer.isBlank()) problems += "$tag resposta vazia"
            if (q.explanation.isBlank()) problems += "$tag explicação vazia"
            if (q.source.isBlank()) problems += "$tag fonte vazia"
            if (q.subtheme.isBlank()) problems += "$tag subtema vazio"
            if (q.minAge !in 0..18) problems += "$tag faixa etária inválida"
            when (q.format) {
                QuestionFormat.MULTIPLE_CHOICE -> {
                    if (q.options.size !in 3..4) problems += "$tag múltipla escolha precisa de 3 ou 4 alternativas"
                    if (q.answer !in q.options) problems += "$tag resposta não está entre as alternativas"
                    val norm = q.options.map(TextNormalizer::normalize)
                    if (norm.toSet().size != norm.size) problems += "$tag alternativas duplicadas"
                    if (answerGivenAway(q)) problems += "$tag enunciado entrega a resposta"
                }
                QuestionFormat.TRUE_FALSE -> {
                    if (q.options != TRUE_FALSE_OPTIONS) problems += "$tag V/F deve ter alternativas Verdadeiro/Falso"
                    if (q.answer !in TRUE_FALSE_OPTIONS) problems += "$tag V/F com resposta inválida"
                }
                QuestionFormat.OPEN -> {
                    if (q.options.isNotEmpty()) problems += "$tag pergunta aberta não deve ter alternativas"
                    if (answerGivenAway(q)) problems += "$tag enunciado entrega a resposta"
                }
            }
        }
        return problems
    }

    private fun answerGivenAway(q: Question): Boolean {
        val answer = TextNormalizer.normalize(q.answer)
        if (answer.length < 3) return false
        return " ${TextNormalizer.normalize(q.text)} ".contains(" $answer ")
    }

    companion object {
        val TRUE_FALSE_OPTIONS = listOf("Verdadeiro", "Falso")

        private val json = Json { ignoreUnknownKeys = true }

        fun fromJson(text: String): QuestionBank = QuestionBank(json.decodeFromString<QuestionFile>(text).questions)
    }
}
