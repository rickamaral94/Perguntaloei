package br.com.perguntaloei.diag

import android.app.ActivityManager
import android.app.ApplicationExitInfo
import android.content.Context
import android.os.Build
import android.os.Handler
import android.os.Looper
import android.os.SystemClock
import java.io.File
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale
import java.util.concurrent.Executors
import java.util.concurrent.atomic.AtomicBoolean

/**
 * Registro técnico de diagnóstico, só no aparelho, para descobrir travamentos e falhas.
 *
 * Guarda eventos do app (telas, início e fim de partida, tempos), travamentos da tela com o ponto
 * do código onde ela parou, falhas e os motivos de encerramento informados pelo Android.
 * Nunca guarda nomes, idades, respostas nem o texto das perguntas. Só sai do aparelho se o
 * jogador tocar em "Compartilhar diagnóstico" (e escolher para onde mandar).
 */
object Diagnostics {

    private const val MAX_BYTES = 200_000L
    private const val KEEP_BYTES = 120_000

    /** Tela parada por mais que isso conta como travamento. */
    private const val FREEZE_MS = 2_500L

    private val writer = Executors.newSingleThreadExecutor { Thread(it, "diagnostico").apply { isDaemon = true } }
    private val time = SimpleDateFormat("dd/MM HH:mm:ss.SSS", Locale.ROOT)
    @Volatile private var file: File? = null
    @Volatile private var started = false

    fun init(context: Context, version: String) {
        val dir = File(context.filesDir, "diagnostico").apply { mkdirs() }
        file = File(dir, "registro.txt")
        if (started) return
        started = true
        log(
            "app",
            "início · versão $version · Android ${Build.VERSION.RELEASE} (API ${Build.VERSION.SDK_INT}) · " +
                "${Build.MANUFACTURER} ${Build.MODEL} · ${memoryInfo(context)}",
        )
        installCrashHandler()
        writer.execute { runCatching { recordPreviousExits(context, dir) } }
        if (!isRobolectric()) startWatchdog()
    }

    fun log(tag: String, message: String) {
        val f = file ?: return
        val line = "${time.format(Date())} [$tag] $message\n"
        writer.execute { append(f, line) }
    }

    /** Mede um trecho e registra se demorar mais que [slowMs]. */
    inline fun <T> timed(tag: String, what: String, slowMs: Long = 0, block: () -> T): T {
        val start = SystemClock.elapsedRealtime()
        val result = block()
        val ms = SystemClock.elapsedRealtime() - start
        if (ms >= slowMs) log(tag, "$what: $ms ms")
        return result
    }

    /** Conteúdo do registro para compartilhar (o mais recente, até ~100 KB). */
    fun export(): String {
        val f = file ?: return "Registro indisponível."
        val text = runCatching { writer.submit<String> { if (f.exists()) f.readText() else "" }.get() }.getOrDefault("")
        val body = if (text.length > 100_000) "…(início cortado)\n" + text.takeLast(100_000) else text
        return "Diagnóstico do PERGUNTÁ-LO-EI\n" +
            "(sem nomes, idades, respostas ou perguntas; só dados técnicos)\n\n" + body.ifBlank { "Nada registrado ainda.\n" }
    }

    fun clear() {
        val f = file ?: return
        writer.execute { f.delete() }
        log("app", "registro apagado pelo jogador")
    }

    private fun append(f: File, line: String) {
        runCatching {
            f.appendText(line)
            if (f.length() > MAX_BYTES) {
                val text = f.readText()
                f.writeText(text.takeLast(KEEP_BYTES).substringAfter('\n'))
            }
        }
    }

    private fun installCrashHandler() {
        val previous = Thread.getDefaultUncaughtExceptionHandler()
        Thread.setDefaultUncaughtExceptionHandler { thread, error ->
            // Escreve na hora: o processo vai terminar.
            file?.let { append(it, "${time.format(Date())} [falha] thread ${thread.name}: ${error.stackTraceToString().take(6_000)}\n") }
            previous?.uncaughtException(thread, error)
        }
    }

    /**
     * Vigia a thread da tela: se uma tarefa simples postada nela não roda em [FREEZE_MS], a tela
     * está travada — registra onde o código está parado (a mesma informação do "não está respondendo").
     */
    private fun startWatchdog() {
        val main = Handler(Looper.getMainLooper())
        val mainThread = Looper.getMainLooper().thread
        Thread({
            var reported = false
            var freezeStart = 0L
            while (true) {
                val ran = AtomicBoolean(false)
                val sent = SystemClock.elapsedRealtime()
                main.post { ran.set(true) }
                Thread.sleep(FREEZE_MS)
                if (!ran.get()) {
                    if (!reported) {
                        reported = true
                        freezeStart = sent
                        val stack = mainThread.stackTrace.take(40).joinToString("\n") { "    at $it" }
                        log("travamento", "tela parada há mais de ${FREEZE_MS / 1000.0} s. Onde está:\n$stack")
                    }
                    while (!ran.get()) Thread.sleep(100)
                    log("travamento", "tela voltou após ${SystemClock.elapsedRealtime() - freezeStart} ms")
                    reported = false
                }
            }
        }, "vigia-da-tela").apply { isDaemon = true; priority = Thread.MIN_PRIORITY }.start()
    }

    /** Motivos de encerramentos anteriores (travamento, falha, falta de memória), Android 11+. */
    private fun recordPreviousExits(context: Context, dir: File) {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.R) return
        val am = context.getSystemService(Context.ACTIVITY_SERVICE) as? ActivityManager ?: return
        val seenFile = File(dir, "ultimo_encerramento.txt")
        val lastSeen = runCatching { seenFile.readText().trim().toLong() }.getOrDefault(0L)
        val exits = am.getHistoricalProcessExitReasons(context.packageName, 0, 10).filter { it.timestamp > lastSeen }
        for (e in exits.sortedBy { it.timestamp }) {
            val reason = when (e.reason) {
                ApplicationExitInfo.REASON_ANR -> "TRAVAMENTO (não está respondendo)"
                ApplicationExitInfo.REASON_CRASH -> "falha (Java/Kotlin)"
                ApplicationExitInfo.REASON_CRASH_NATIVE -> "falha nativa"
                ApplicationExitInfo.REASON_LOW_MEMORY -> "falta de memória"
                ApplicationExitInfo.REASON_USER_REQUESTED -> "fechado pelo usuário"
                ApplicationExitInfo.REASON_USER_STOPPED -> "parado pelo usuário"
                ApplicationExitInfo.REASON_EXIT_SELF -> "saída normal"
                ApplicationExitInfo.REASON_SIGNALED -> "encerrado pelo sistema"
                else -> "motivo ${e.reason}"
            }
            val lines = StringBuilder("encerramento anterior em ${time.format(Date(e.timestamp))}: $reason")
            e.description?.let { lines.append(" · ").append(it.take(300)) }
            lines.append(" · memória ${e.pss / 1024} MB")
            if (e.reason == ApplicationExitInfo.REASON_ANR) {
                val trace = runCatching { e.traceInputStream?.bufferedReader()?.use { it.readText() } }.getOrNull()
                mainThreadSection(trace)?.let { lines.append("\n").append(it) }
            }
            file?.let { append(it, "${time.format(Date())} [android] $lines\n") }
        }
        exits.maxOfOrNull { it.timestamp }?.let { seenFile.writeText(it.toString()) }
    }

    /** Do relatório de travamento do Android, só o trecho da thread da tela. */
    internal fun mainThreadSection(trace: String?): String? {
        if (trace.isNullOrBlank()) return null
        val start = trace.indexOf("\"main\"")
        if (start < 0) return null
        val end = trace.indexOf("\n\n", start).takeIf { it > 0 } ?: trace.length
        return trace.substring(start, end).lines().take(60).joinToString("\n") { "    $it" }
    }

    private fun memoryInfo(context: Context): String = runCatching {
        val am = context.getSystemService(Context.ACTIVITY_SERVICE) as ActivityManager
        val info = ActivityManager.MemoryInfo().also { am.getMemoryInfo(it) }
        "RAM ${info.totalMem / (1024 * 1024)} MB, livre ${info.availMem / (1024 * 1024)} MB"
    }.getOrDefault("RAM ?")

    private fun isRobolectric() = Build.FINGERPRINT == "robolectric"
}
