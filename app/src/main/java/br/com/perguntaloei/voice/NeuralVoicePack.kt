package br.com.perguntaloei.voice

import java.io.File
import java.io.IOException
import java.net.HttpURLConnection
import java.net.URL
import java.security.MessageDigest

/** Um arquivo do pacote de voz, com tamanho e SHA-256 conferidos depois do download. */
data class VoiceFile(val path: String, val size: Long, val sha256: String)

sealed interface DownloadResult {
    data object Done : DownloadResult
    data object Cancelled : DownloadResult
    data class Failed(val message: String) : DownloadResult
}

/**
 * Voz neural opcional (Piper pt-BR "faber"), baixada só quando o jogador pede.
 *
 * Os arquivos vêm de uma versão fixa do repositório público no Hugging Face e só são aceitos
 * se o tamanho e o SHA-256 baterem com os valores abaixo. Nada sobre o jogador é enviado:
 * o app só faz requisições GET desses arquivos.
 */
class NeuralVoicePack(
    baseDir: File,
    private val baseUrl: String = DEFAULT_URL,
    val files: List<VoiceFile> = FABER_FILES,
) {
    /** Pasta com o modelo, os tokens e os dados de fonética prontos para uso. */
    val dir = File(baseDir, "faber-v1")
    private val marker = File(dir, ".instalado")

    val totalBytes: Long get() = files.sumOf { it.size }

    fun isInstalled(): Boolean = marker.exists() && files.all { File(dir, it.path).length() == it.size }

    fun hasSpaceFor(): Boolean = (dir.parentFile ?: dir).let { it.mkdirs(); it.usableSpace > totalBytes + 30L * 1024 * 1024 }

    /**
     * Baixa (ou completa) o pacote. [onProgress] recebe bytes prontos e total.
     * Arquivos já baixados e conferidos são reaproveitados se o download for retomado.
     */
    fun download(onProgress: (done: Long, total: Long) -> Unit, isCancelled: () -> Boolean): DownloadResult {
        dir.mkdirs()
        var done = 0L
        for (f in files) {
            if (isCancelled()) return DownloadResult.Cancelled
            val target = File(dir, f.path)
            if (target.length() == f.size && sha256(target) == f.sha256) {
                done += f.size
                onProgress(done, totalBytes)
                continue
            }
            target.parentFile?.mkdirs()
            val part = File(target.parentFile, target.name + ".part")
            val result = try {
                fetch("$baseUrl/${f.path}", part, f, isCancelled) { n -> onProgress(done + n, totalBytes) }
            } catch (e: IOException) {
                DownloadResult.Failed("Falha na conexão: ${e.message ?: "sem resposta"}. Confira a internet e tente de novo.")
            }
            if (result != DownloadResult.Done) {
                part.delete()
                return result
            }
            target.delete()
            if (!part.renameTo(target)) return DownloadResult.Failed("Não foi possível salvar ${f.path}.")
            done += f.size
            onProgress(done, totalBytes)
        }
        marker.writeText("ok")
        return DownloadResult.Done
    }

    private fun fetch(url: String, out: File, f: VoiceFile, isCancelled: () -> Boolean, progress: (Long) -> Unit): DownloadResult {
        val conn = (URL(url).openConnection() as HttpURLConnection).apply {
            connectTimeout = 15_000
            readTimeout = 30_000
            instanceFollowRedirects = true
            setRequestProperty("User-Agent", "PERGUNTALOEI-Android")
        }
        try {
            if (conn.responseCode !in 200..299) return DownloadResult.Failed("O servidor respondeu ${conn.responseCode} ao baixar ${f.path}.")
            val digest = MessageDigest.getInstance("SHA-256")
            var written = 0L
            conn.inputStream.use { input ->
                out.outputStream().use { output ->
                    val buf = ByteArray(64 * 1024)
                    var lastReport = 0L
                    while (true) {
                        if (isCancelled()) return DownloadResult.Cancelled
                        val n = input.read(buf)
                        if (n < 0) break
                        output.write(buf, 0, n)
                        digest.update(buf, 0, n)
                        written += n
                        if (written > f.size) return DownloadResult.Failed("Arquivo ${f.path} maior que o esperado.")
                        if (written - lastReport >= 256 * 1024) {
                            lastReport = written
                            progress(written)
                        }
                    }
                }
            }
            progress(written)
            val hash = digest.digest().joinToString("") { "%02x".format(it) }
            if (written != f.size || hash != f.sha256) {
                return DownloadResult.Failed("O arquivo ${f.path} chegou incompleto ou diferente do esperado. Tente de novo.")
            }
            return DownloadResult.Done
        } finally {
            conn.disconnect()
        }
    }

    /** Apaga a voz baixada e libera o espaço. */
    fun delete() {
        dir.deleteRecursively()
    }

    companion object {
        /** Versão fixa do repositório: o conteúdo não muda sem atualização do app. */
        const val DEFAULT_URL =
            "https://huggingface.co/csukuangfj/vits-piper-pt_BR-faber-medium/resolve/4f385076a8f9d5bc7b4cd9fea4dc77e6e8ca8167"

        const val MODEL_FILE = "pt_BR-faber-medium.onnx"

        /** Só o necessário para o português: modelo, tokens e 8 arquivos de fonética do espeak-ng. */
        val FABER_FILES = listOf(
            VoiceFile(MODEL_FILE, 63_201_428, "39fb6b580d6d40a3230b7a9d0851d282074537b9694892b5b3cd90ff87c6cbb3"),
            VoiceFile("tokens.txt", 907, "2619c1a9de1bcf928162f40c583caf39368cfd6b2340c7bcad51dc634411ec36"),
            VoiceFile("espeak-ng-data/phontab", 55_796, "886f3fa402cb0ba73d483aa8ad000af47a6b7cc06293c75a97913fba68a530f6"),
            VoiceFile("espeak-ng-data/phonindex", 39_074, "3ca7b8fa3b42624e4b0f152707e7a39245fce569aa99ea47c055d9e622fcf0c4"),
            VoiceFile("espeak-ng-data/phondata", 550_424, "4e0288957874029a8c3c9f41a8f517ad4bf18127046decbdd4b9d1d6807ce3a3"),
            VoiceFile("espeak-ng-data/phondata-manifest", 21_821, "7b387af0702c7cf0b61f0bead68feded0bd8e1620729b0b252e76acbc30d3813"),
            VoiceFile("espeak-ng-data/intonations", 2_040, "3f8af65fd3eda9759a10f021d61361c120871f463515229c925995c7f90918cc"),
            VoiceFile("espeak-ng-data/pt_dict", 67_817, "7e8398f15fa4a21db39a213381f28ec0d302b22663c644e865abb61a09c1b004"),
            VoiceFile("espeak-ng-data/lang/roa/pt", 95, "a44060072f790e41912c57b7d52f7b6438c4383e0dabdb052f6fdb7aacc23493"),
            VoiceFile("espeak-ng-data/lang/roa/pt-BR", 109, "84dd4e34c970fadbe32211eadecfdfaab52432479c0911e43300da88a33398ba"),
        )

        fun sha256(file: File): String {
            val digest = MessageDigest.getInstance("SHA-256")
            file.inputStream().use { input ->
                val buf = ByteArray(64 * 1024)
                while (true) {
                    val n = input.read(buf)
                    if (n < 0) break
                    digest.update(buf, 0, n)
                }
            }
            return digest.digest().joinToString("") { "%02x".format(it) }
        }
    }
}
