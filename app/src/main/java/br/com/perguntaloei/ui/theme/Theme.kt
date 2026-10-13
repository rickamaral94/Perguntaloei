package br.com.perguntaloei.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Typography
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.Font
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp
import br.com.perguntaloei.R
import br.com.perguntaloei.model.Theme as QuizTheme

/** Paleta arcade de alto contraste. */
object Arcade {
    val Bg = Color(0xFF0D0A2B)
    val Panel = Color(0xFF1E1A4F)
    val PanelLight = Color(0xFF2C2770)
    val Ink = Color(0xFF05040F)
    val Cyan = Color(0xFF00E5FF)
    val Magenta = Color(0xFFFF2E97)
    val Yellow = Color(0xFFFFE14D)
    val Green = Color(0xFF3DFF6E)
    val Red = Color(0xFFFF4D4D)
    val Orange = Color(0xFFFF9F1C)
    val Purple = Color(0xFFB17BFF)
    val White = Color(0xFFFFFFFF)
    val Muted = Color(0xFFC9C4F2)

    val Pixel = FontFamily(Font(R.font.press_start_2p))

    fun themeColor(t: QuizTheme): Color = when (t) {
        QuizTheme.GEOGRAFIA -> Color(0xFF3DDC97)
        QuizTheme.HISTORIA -> Color(0xFFFFB347)
        QuizTheme.CIENCIA -> Color(0xFF4FC3F7)
        QuizTheme.TECNOLOGIA -> Color(0xFF00E5FF)
        QuizTheme.CINEMA -> Color(0xFFFF6E6E)
        QuizTheme.FILMES_INFANTIS -> Color(0xFFFFE14D)
        QuizTheme.NOVELAS -> Color(0xFFFF7BD5)
        QuizTheme.TELEVISAO -> Color(0xFFB17BFF)
        QuizTheme.ESPORTES -> Color(0xFF3DFF6E)
        QuizTheme.MARCAS -> Color(0xFFFF9F1C)
        QuizTheme.MUSICA -> Color(0xFFFF2E97)
        QuizTheme.LITERATURA -> Color(0xFFE0C097)
        QuizTheme.NATUREZA -> Color(0xFF8BE36B)
        QuizTheme.CULTURA_BRASILEIRA -> Color(0xFFFFD60A)
        QuizTheme.CURIOSIDADES -> Color(0xFF7DF9FF)
    }

    fun themeIcon(t: QuizTheme): String = when (t) {
        QuizTheme.GEOGRAFIA -> "🌎"
        QuizTheme.HISTORIA -> "🏛️"
        QuizTheme.CIENCIA -> "🔬"
        QuizTheme.TECNOLOGIA -> "💻"
        QuizTheme.CINEMA -> "🎬"
        QuizTheme.FILMES_INFANTIS -> "🧸"
        QuizTheme.NOVELAS -> "📺"
        QuizTheme.TELEVISAO -> "📡"
        QuizTheme.ESPORTES -> "⚽"
        QuizTheme.MARCAS -> "🏷️"
        QuizTheme.MUSICA -> "🎵"
        QuizTheme.LITERATURA -> "📚"
        QuizTheme.NATUREZA -> "🌿"
        QuizTheme.CULTURA_BRASILEIRA -> "🇧🇷"
        QuizTheme.CURIOSIDADES -> "💡"
    }
}

private val typography = Typography(
    bodyLarge = TextStyle(fontSize = 18.sp, lineHeight = 26.sp, fontWeight = FontWeight.Medium),
    bodyMedium = TextStyle(fontSize = 16.sp, lineHeight = 22.sp),
    titleLarge = TextStyle(fontSize = 22.sp, fontWeight = FontWeight.Bold),
    titleMedium = TextStyle(fontSize = 18.sp, fontWeight = FontWeight.Bold),
    labelLarge = TextStyle(fontSize = 17.sp, fontWeight = FontWeight.Bold),
)

@Composable
fun ArcadeTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = darkColorScheme(
            primary = Arcade.Yellow,
            onPrimary = Arcade.Ink,
            secondary = Arcade.Cyan,
            onSecondary = Arcade.Ink,
            tertiary = Arcade.Magenta,
            background = Arcade.Bg,
            onBackground = Arcade.White,
            surface = Arcade.Panel,
            onSurface = Arcade.White,
            surfaceVariant = Arcade.PanelLight,
            onSurfaceVariant = Arcade.Muted,
            error = Arcade.Red,
        ),
        typography = typography,
        content = content,
    )
}
