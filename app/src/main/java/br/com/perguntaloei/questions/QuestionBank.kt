package br.com.perguntaloei.questions

import br.com.perguntaloei.model.Question
import br.com.perguntaloei.model.QuestionFormat
import br.com.perguntaloei.model.Theme
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json

@Serializable
private data class QuestionFile(val version: Int, val questions: List<Question>)

/**
 * Banco de perguntas embutido no app. Imutável depois de carregado.
 *
 * [nearDuplicates]: para cada pergunta, os ids de outras perguntas essencialmente iguais. O banco
 * embutido é conferido sem nenhuma quase-duplicata na hora de gerar o arquivo (teste
 * `bankHasNoNearDuplicates`), então o aparelho não precisa fazer essa comparação pesada
 * (centenas de milhares de pares) — ela chegou a travar a tela em celulares.
 */
class QuestionBank(
    val questions: List<Question>,
    val nearDuplicates: Map<String, Set<String>> = emptyMap(),
) {

    val byId: Map<String, Question> = questions.associateBy { it.id }

    val fingerprints: Map<String, String> by lazy { questions.associate { it.id to TextNormalizer.fingerprint(it.text) } }

    /** Palavras de cada impressão digital, calculadas uma única vez. */
    val fingerprintTokens: Map<String, Set<String>> by lazy { fingerprints.mapValues { (_, fp) -> fp.split(' ').toSet() } }

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

        /**
         * Compara todas as perguntas entre si (usado nos testes e na geração do banco).
         * Normaliza cada texto uma vez e só calcula a distância de edição quando os tamanhos permitem.
         */
        fun findNearDuplicates(questions: List<Question>): Map<String, Set<String>> {
            val norm = questions.map { TextNormalizer.normalize(it.text) }
            val tokens = questions.map { TextNormalizer.contentTokens(it.text) }
            val answers = questions.map { TextNormalizer.normalize(it.answer) }
            val result = HashMap<String, MutableSet<String>>()
            for (i in questions.indices) {
                for (j in i + 1 until questions.size) {
                    if (TextNormalizer.isNearDuplicatePrepared(norm[i], tokens[i], answers[i], norm[j], tokens[j], answers[j])) {
                        result.getOrPut(questions[i].id) { mutableSetOf() }.add(questions[j].id)
                        result.getOrPut(questions[j].id) { mutableSetOf() }.add(questions[i].id)
                    }
                }
            }
            return result
        }
    }
}
