package br.com.perguntaloei

import android.app.Application
import androidx.test.core.app.ApplicationProvider
import androidx.test.ext.junit.runners.AndroidJUnit4
import br.com.perguntaloei.diag.Diagnostics
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.annotation.Config

@RunWith(AndroidJUnit4::class)
@Config(sdk = [34])
class DiagnosticsTest {

    private val app: Application = ApplicationProvider.getApplicationContext()

    @Test
    fun recordsEventsAndExportsOnlyTechnicalData() {
        Diagnostics.init(app, "teste")
        Diagnostics.log("tela", "HOME → SETTINGS")
        val text = Diagnostics.export()
        assertTrue(text.contains("[tela] HOME → SETTINGS"))
        assertTrue(text.contains("sem nomes, idades, respostas ou perguntas"))
    }

    @Test
    fun clearingStartsAFreshRecord() {
        Diagnostics.init(app, "teste")
        Diagnostics.log("tela", "antes")
        Diagnostics.clear()
        val text = Diagnostics.export()
        assertFalse(text.contains("antes"))
        assertTrue(text.contains("registro apagado"))
    }

    @Test
    fun keepsOnlyTheMainThreadPartOfAnAndroidFreezeReport() {
        val trace = """
            ----- pid 123 at 2026-10-13 -----
            "Signal Catcher" daemon prio=10
              at nada

            "main" prio=5 tid=1 Blocked
              at br.com.perguntaloei.AppViewModel.refreshThemeStats(AppViewModel.kt:350)
              at androidx.compose.runtime.Recomposer.run

            "outra" prio=5
              at x
        """.trimIndent()
        val main = Diagnostics.mainThreadSection(trace)!!
        assertTrue(main.contains("refreshThemeStats"))
        assertFalse(main.contains("Signal Catcher"))
        assertFalse(main.contains("outra"))
        assertEquals(null, Diagnostics.mainThreadSection("sem thread principal"))
    }
}
