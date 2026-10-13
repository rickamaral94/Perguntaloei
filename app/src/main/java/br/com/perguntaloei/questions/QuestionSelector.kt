package br.com.perguntaloei.questions

import br.com.perguntaloei.model.Difficulty
import br.com.perguntaloei.model.GameConfig
import br.com.perguntaloei.model.GameMode
import br.com.perguntaloei.model.Player
import br.com.perguntaloei.model.Question
import br.com.perguntaloei.model.Theme
import kotlin.random.Random

/** Perguntas já usadas em partidas anteriores (histórico salvo no aparelho). */
data class UsageHistory(
    val usedIds: Set<String> = emptySet(),
    val usedFingerprints: Set<String> = emptySet(),
) {
    /** Palavras de cada impressão digital usada, separadas uma única vez. */
    val usedTokens: List<Set<String>> by lazy { usedFingerprints.map { it.split(' ').toSet() } }

    companion object { val EMPTY = UsageHistory() }
}

/** Como a dificuldade é adaptada à idade de cada jogador. */
object AgePolicy {

    fun groupLabel(age: Int?): String = when {
        age == null -> "Adulto"
        age < 10 -> "Criança"
        age < 13 -> "Pré-adolescente"
        age < 16 -> "Adolescente"
        else -> "Adulto"
    }

    /**
     * Dificuldades preferidas para o jogador. Adultos (ou idade não informada) usam a
     * configuração escolhida; crianças e adolescentes recebem níveis adequados à idade,
     * independentemente da escolha dos adultos.
     */
    fun preferredDifficulties(age: Int?, adultChoice: Set<Difficulty>): List<Difficulty> {
        val adult = adultChoice.ifEmpty { setOf(Difficulty.MEDIA) }
        return when {
            age == null || age >= 16 -> adult.sortedBy { it.level }
            age < 10 -> listOf(Difficulty.FACIL)
            age < 13 -> listOf(Difficulty.FACIL, Difficulty.MEDIA)
            else -> adult.filter { it.level <= Difficulty.DIFICIL.level }
                .ifEmpty { listOf(Difficulty.MEDIA, Difficulty.DIFICIL) }
                .sortedBy { it.level }
        }
    }

    /** Dificuldades aceitáveis quando faltam perguntas no nível preferido. */
    fun fallbackDifficulties(age: Int?): List<Difficulty> = when {
        age == null || age >= 16 -> Difficulty.entries
        age < 10 -> listOf(Difficulty.FACIL, Difficulty.MEDIA)
        age < 13 -> listOf(Difficulty.FACIL, Difficulty.MEDIA, Difficulty.DIFICIL)
        else -> listOf(Difficulty.FACIL, Difficulty.MEDIA, Difficulty.DIFICIL)
    }

    /** A faixa etária sugerida da pergunta nunca é ultrapassada. */
    fun ageAllows(q: Question, age: Int?): Boolean = age == null || q.minAge <= age
}

data class Pick(
    val question: Question,
    /** true quando todas as inéditas acabaram e foi preciso reaproveitar uma do histórico. */
    val reusedFromHistory: Boolean,
    /** true quando foi preciso usar um nível vizinho ao preferido. */
    val difficultyAdjusted: Boolean,
)

class QuestionSelector(private val bank: QuestionBank) {

    /** Usada (ou quase igual a uma usada) nesta partida. */
    fun usedInGame(q: Question, gameUsed: Set<String>): Boolean =
        q.id in gameUsed || bank.nearDuplicates[q.id].orEmpty().any { it in gameUsed }

    /** Usada (ou quase igual a uma usada) em partidas anteriores, segundo o histórico salvo. */
    fun usedInHistory(q: Question, history: UsageHistory): Boolean {
        if (q.id in history.usedIds) return true
        if (bank.nearDuplicates[q.id].orEmpty().any { it in history.usedIds }) return true
        if (history.usedFingerprints.isEmpty()) return false
        val fp = bank.fingerprints[q.id] ?: TextNormalizer.fingerprint(q.text)
        if (fp in history.usedFingerprints) return true
        val tokens = bank.fingerprintTokens[q.id] ?: fp.split(' ').toSet()
        return history.usedTokens.any { other -> TextNormalizer.jaccardOf(tokens, other) >= 0.8 }
    }

    fun pool(config: GameConfig, theme: Theme?): List<Question> = bank.questions.filter {
        (theme == null || it.theme == theme) && (config.mode != GameMode.BRAZIL || it.brazil)
    }

    /**
     * Escolhe uma pergunta para o jogador. Nunca repete na mesma partida e nunca passa da
     * faixa etária. Ordem de preferência: inédita no nível ideal → inédita em nível vizinho →
     * do histórico no nível ideal → do histórico em nível vizinho.
     */
    fun pick(
        player: Player,
        theme: Theme?,
        config: GameConfig,
        gameUsed: Set<String>,
        history: UsageHistory,
        random: Random,
        allowHistoryReuse: Boolean = true,
    ): Pick? {
        val base = pool(config, theme).filter { AgePolicy.ageAllows(it, player.age) && !usedInGame(it, gameUsed) }
        val preferred = AgePolicy.preferredDifficulties(player.age, config.difficulties)
        val fallback = AgePolicy.fallbackDifficulties(player.age)
        val fresh = base.filter { !usedInHistory(it, history) }

        chooseBalanced(fresh, preferred, random)?.let { return Pick(it, reusedFromHistory = false, difficultyAdjusted = false) }
        chooseNearest(fresh, nearestFirst(fallback, preferred), random)?.let { return Pick(it, false, true) }
        if (!allowHistoryReuse) return null
        chooseBalanced(base, preferred, random)?.let { return Pick(it, true, false) }
        chooseNearest(base, nearestFirst(fallback, preferred), random)?.let { return Pick(it, true, true) }
        return null
    }

    /** Níveis fora dos preferidos, do mais próximo ao mais distante. */
    private fun nearestFirst(levels: List<Difficulty>, preferred: List<Difficulty>): List<Difficulty> {
        val center = preferred.map { it.level }.average()
        return levels.filter { it !in preferred }.sortedBy { kotlin.math.abs(it.level - center) }
    }

    /** Sorteia um nível entre os disponíveis (equilíbrio) e depois uma pergunta desse nível. */
    private fun chooseBalanced(candidates: List<Question>, levels: List<Difficulty>, random: Random): Question? {
        val byLevel = candidates.filter { it.difficulty in levels }.groupBy { it.difficulty }
        if (byLevel.isEmpty()) return null
        val level = byLevel.keys.sortedBy { it.level }.random(random)
        return byLevel.getValue(level).random(random)
    }

    /** Usa o primeiro nível da lista que tiver perguntas. */
    private fun chooseNearest(candidates: List<Question>, levels: List<Difficulty>, random: Random): Question? {
        for (level in levels) {
            val options = candidates.filter { it.difficulty == level }
            if (options.isNotEmpty()) return options.random(random)
        }
        return null
    }
}
