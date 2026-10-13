package br.com.perguntaloei

import br.com.perguntaloei.voice.DownloadResult
import br.com.perguntaloei.voice.NeuralVoicePack
import br.com.perguntaloei.voice.VoiceFile
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Rule
import org.junit.Test
import org.junit.rules.TemporaryFolder
import java.io.File
import java.net.InetAddress
import java.net.ServerSocket
import kotlin.concurrent.thread
import java.security.MessageDigest
import java.util.concurrent.atomic.AtomicInteger

/** Download da voz neural opcional, contra um servidor local (sem internet). */
class NeuralVoicePackTest {

    @get:Rule val tmp = TemporaryFolder()

    private val contents = mapOf(
        "modelo.onnx" to ByteArray(300_000) { (it % 251).toByte() },
        "tokens.txt" to "a 1\nb 2\n".toByteArray(),
        "espeak-ng-data/lang/roa/pt-BR" to "name Portuguese".toByteArray(),
    )
    private val served = contents.toMutableMap()
    private val requests = AtomicInteger()
    private lateinit var server: ServerSocket

    private fun sha(b: ByteArray) = MessageDigest.getInstance("SHA-256").digest(b).joinToString("") { "%02x".format(it) }
    private val files = contents.map { (p, b) -> VoiceFile(p, b.size.toLong(), sha(b)) }

    /** Servidor HTTP mínimo: responde GET /v/<arquivo> com o conteúdo de [served]. */
    @Before
    fun start() {
        server = ServerSocket(0, 50, InetAddress.getLoopbackAddress())
        thread(isDaemon = true) {
            while (!server.isClosed) {
                val socket = runCatching { server.accept() }.getOrNull() ?: break
                socket.use { s ->
                    val reader = s.getInputStream().bufferedReader(Charsets.ISO_8859_1)
                    val path = reader.readLine().orEmpty().split(" ").getOrElse(1) { "" }
                    while (reader.readLine().orEmpty().isNotEmpty()) Unit
                    requests.incrementAndGet()
                    val body = served[path.removePrefix("/v/")]
                    val out = s.getOutputStream()
                    if (body == null) {
                        out.write("HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\nConnection: close\r\n\r\n".toByteArray())
                    } else {
                        out.write("HTTP/1.1 200 OK\r\nContent-Length: ${body.size}\r\nConnection: close\r\n\r\n".toByteArray())
                        out.write(body)
                    }
                    out.flush()
                }
            }
        }
    }

    @After
    fun stop() = server.close()

    private fun pack() = NeuralVoicePack(tmp.root, "http://127.0.0.1:${server.localPort}/v", files)

    @Test
    fun downloadsVerifiesAndInstalls() {
        val p = pack()
        assertFalse(p.isInstalled())
        var last = 0L
        val r = p.download({ done, total -> assertTrue(done >= last); last = done; assertEquals(p.totalBytes, total) }, { false })
        assertEquals(DownloadResult.Done, r)
        assertTrue(p.isInstalled())
        assertEquals(p.totalBytes, last)
        contents.forEach { (path, b) -> assertTrue(File(p.dir, path).readBytes().contentEquals(b)) }
        assertTrue(p.dir.walk().none { it.name.endsWith(".part") })
    }

    @Test
    fun rejectsAFileWithTheWrongContent() {
        served["tokens.txt"] = "x 9\ny 8\n".toByteArray() // mesmo tamanho, conteúdo diferente
        val p = pack()
        val r = p.download({ _, _ -> }, { false })
        assertTrue(r is DownloadResult.Failed)
        assertFalse(p.isInstalled())
        assertFalse(File(p.dir, "tokens.txt").exists())
    }

    @Test
    fun rejectsAFileBiggerThanExpected() {
        served["tokens.txt"] = ByteArray(5000)
        val r = pack().download({ _, _ -> }, { false })
        assertTrue(r is DownloadResult.Failed)
    }

    @Test
    fun reportsServerErrors() {
        served.remove("espeak-ng-data/lang/roa/pt-BR")
        val p = pack()
        val r = p.download({ _, _ -> }, { false })
        assertTrue(r is DownloadResult.Failed && "404" in r.message)
        assertFalse(p.isInstalled())
    }

    @Test
    fun canBeCancelledAndResumedWithoutDownloadingAgain() {
        val p = pack()
        var calls = 0
        // Cancela logo depois de terminar o primeiro arquivo.
        val r = p.download({ done, _ -> if (done >= files[0].size) calls++ }, { calls > 0 })
        assertEquals(DownloadResult.Cancelled, r)
        assertFalse(p.isInstalled())
        val before = requests.get()
        assertEquals(DownloadResult.Done, p.download({ _, _ -> }, { false }))
        assertEquals("o primeiro arquivo é reaproveitado", files.size - 1, requests.get() - before)
        assertTrue(p.isInstalled())
    }

    @Test
    fun deleteFreesTheSpace() {
        val p = pack()
        assertEquals(DownloadResult.Done, p.download({ _, _ -> }, { false }))
        p.delete()
        assertFalse(p.isInstalled())
        assertFalse(p.dir.exists())
    }

    @Test
    fun realPackIsPinnedAndComplete() {
        val real = NeuralVoicePack.FABER_FILES
        assertTrue(NeuralVoicePack.DEFAULT_URL.startsWith("https://huggingface.co/") && "/resolve/" in NeuralVoicePack.DEFAULT_URL)
        assertTrue(NeuralVoicePack.DEFAULT_URL.substringAfterLast("/").matches(Regex("[0-9a-f]{40}")))
        assertTrue(real.any { it.path == NeuralVoicePack.MODEL_FILE })
        assertTrue(real.any { it.path == "tokens.txt" })
        assertTrue(real.all { it.sha256.matches(Regex("[0-9a-f]{64}")) && it.size > 0 })
    }
}
