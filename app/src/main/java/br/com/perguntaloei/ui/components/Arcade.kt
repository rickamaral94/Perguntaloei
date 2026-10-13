package br.com.perguntaloei.ui.components

import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.RepeatMode
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.interaction.collectIsPressedAsState
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ColumnScope
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.CutCornerShape
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.scale
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Shadow
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.TextUnit
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import br.com.perguntaloei.ui.theme.Arcade
import kotlin.random.Random

val PixelShape = CutCornerShape(6.dp)

/**
 * Respeita a opção de acessibilidade "Remover animações" do Android: com a escala de
 * animação em zero, os efeitos contínuos (estrelas, título, piscar) ficam parados.
 */
@Composable
fun animationsEnabled(): Boolean = remember {
    if (android.os.Build.VERSION.SDK_INT >= 26) android.animation.ValueAnimator.areAnimatorsEnabled() else true
}

/** Valor animado em loop, ou fixo quando as animações estão desligadas. */
@Composable
private fun looping(from: Float, to: Float, millis: Int, mode: RepeatMode, label: String): Float {
    if (!animationsEnabled()) return from
    val v by rememberInfiniteTransition(label = label).animateFloat(
        from, to, infiniteRepeatable(tween(millis, easing = LinearEasing), mode), label = label,
    )
    return v
}

/** Texto em fonte pixel com sombra dura, estilo fliperama. */
@Composable
fun PixelText(
    text: String,
    modifier: Modifier = Modifier,
    size: TextUnit = 14.sp,
    color: Color = Arcade.Yellow,
    align: TextAlign = TextAlign.Start,
    shadow: Color = Arcade.Magenta,
) {
    // A Silkscreen tem letras baixas: compensa para manter a leitura fácil.
    val scaled = size * 1.3f
    Text(
        text = text,
        modifier = modifier,
        textAlign = align,
        style = TextStyle(
            fontFamily = Arcade.Pixel,
            fontSize = scaled,
            lineHeight = scaled * 1.3f,
            color = color,
            shadow = Shadow(shadow, Offset(4f, 4f), 0f),
        ),
    )
}

/** Botão grande e "gordinho" com sombra pixelada; afunda ao ser pressionado. */
@Composable
fun ArcadeButton(
    text: String,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    color: Color = Arcade.Yellow,
    textColor: Color = Arcade.Ink,
    enabled: Boolean = true,
    icon: String? = null,
    minHeight: Dp = 56.dp,
    fontSize: TextUnit = 17.sp,
) {
    val interaction = remember { MutableInteractionSource() }
    val pressed by interaction.collectIsPressedAsState()
    val fill = if (enabled) color else Color(0xFF4A4670)
    val ink = if (enabled) textColor else Color(0xFFA8A4C8)
    val depth = if (pressed) 1.dp else 5.dp
    // propagateMinConstraints: o botão só ocupa a largura toda quando o chamador pede (fillMaxWidth/weight).
    Box(
        modifier = modifier
            .heightIn(min = minHeight)
            .semantics { contentDescription = text }
            .clickable(interaction, indication = null, enabled = enabled, role = Role.Button, onClick = onClick),
        propagateMinConstraints = true,
    ) {
        Box(
            Modifier
                .matchParentSize()
                .offset(x = 5.dp, y = 5.dp)
                .background(Arcade.Ink, PixelShape),
        )
        Row(
            modifier = Modifier
                .heightIn(min = minHeight)
                .offset(x = 5.dp - depth, y = 5.dp - depth)
                .background(fill, PixelShape)
                .border(3.dp, Arcade.Ink, PixelShape)
                .padding(horizontal = 14.dp, vertical = 10.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.Center,
        ) {
            if (icon != null) {
                Text(icon, fontSize = fontSize * 1.1f)
                Spacer(Modifier.width(8.dp))
            }
            Text(text, color = ink, fontSize = fontSize, fontWeight = FontWeight.ExtraBold, textAlign = TextAlign.Center)
        }
    }
}

/** Painel com borda neon e cantos cortados. */
@Composable
fun PixelPanel(
    modifier: Modifier = Modifier,
    border: Color = Arcade.Cyan,
    background: Color = Arcade.Panel,
    padding: Dp = 14.dp,
    content: @Composable ColumnScope.() -> Unit,
) {
    Column(
        modifier = modifier
            .background(background, PixelShape)
            .border(3.dp, border, PixelShape)
            .padding(padding),
        content = content,
    )
}

@Composable
fun Tag(text: String, color: Color, modifier: Modifier = Modifier, textColor: Color = Arcade.Ink) {
    Text(
        text,
        modifier = modifier
            .background(color, CutCornerShape(4.dp))
            .padding(horizontal = 8.dp, vertical = 3.dp),
        color = textColor,
        fontSize = 13.sp,
        fontWeight = FontWeight.Bold,
    )
}

/** Céu estrelado pixelado e animado ao fundo. */
@Composable
fun StarField(modifier: Modifier = Modifier) {
    val stars = remember {
        val r = Random(42)
        List(70) { Triple(r.nextFloat(), r.nextFloat(), r.nextFloat()) }
    }
    val t = looping(0f, 1f, 4000, RepeatMode.Restart, "stars")
    Canvas(modifier.fillMaxSize()) {
        drawRect(Arcade.Bg)
        stars.forEachIndexed { i, (x, y, p) ->
            val phase = ((t + p) % 1f)
            val alpha = if (phase < 0.5f) 0.25f + phase else 1.25f - phase
            val px = if (i % 7 == 0) 6f else 3f
            drawRect(
                color = if (i % 5 == 0) Arcade.Cyan.copy(alpha = alpha) else Color.White.copy(alpha = alpha * 0.8f),
                topLeft = Offset(x * size.width, y * size.height),
                size = Size(px, px),
            )
        }
    }
}

/** Título PERGUNTÁ-LO-EI ajustado à largura da tela, com leve "pulo". */
@Composable
fun GameTitle(modifier: Modifier = Modifier, animate: Boolean = true) {
    val bounce = looping(1f, 1.05f, 700, RepeatMode.Reverse, "title")
    BoxWithConstraints(modifier.fillMaxWidth(), contentAlignment = Alignment.Center) {
        val size = (maxWidth.value / 21f).coerceIn(12f, 32f).sp
        PixelText(
            "PERGUNTÁ-LO-EI",
            modifier = Modifier.scale(if (animate) bounce else 1f),
            size = size,
            color = Arcade.Yellow,
            align = TextAlign.Center,
        )
    }
}

@Composable
fun Blink(text: String, modifier: Modifier = Modifier, color: Color = Arcade.Cyan) {
    val a = looping(1f, 0f, 600, RepeatMode.Reverse, "blink")
    PixelText(text, modifier = modifier.semantics { contentDescription = text }, size = 11.sp, color = color.copy(alpha = if (a > 0.5f) 1f else 0.2f), align = TextAlign.Center, shadow = Color.Transparent)
}

/** Indicador grande de microfone ativo. */
@Composable
fun MicIndicator(listening: Boolean, level: Float, modifier: Modifier = Modifier) {
    val pulse = looping(0.9f, 1.15f, 500, RepeatMode.Reverse, "mic")
    Box(modifier.size(64.dp), contentAlignment = Alignment.Center) {
        if (listening) {
            Box(
                Modifier
                    .size(64.dp)
                    .scale(pulse + level * 0.25f)
                    .clip(CircleShape)
                    .background(Arcade.Red.copy(alpha = 0.35f)),
            )
        }
        Box(
            Modifier
                .size(46.dp)
                .clip(CircleShape)
                .background(if (listening) Arcade.Red else Arcade.PanelLight)
                .border(3.dp, Arcade.Ink, CircleShape),
            contentAlignment = Alignment.Center,
        ) { Text("🎤", fontSize = 22.sp) }
    }
}

@Composable
fun ScreenScaffold(
    title: String,
    onBack: (() -> Unit)?,
    modifier: Modifier = Modifier,
    content: @Composable ColumnScope.() -> Unit,
) {
    Box(modifier.fillMaxSize()) {
        StarField()
        Column(Modifier.fillMaxSize().padding(horizontal = 16.dp, vertical = 12.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.fillMaxWidth()) {
                if (onBack != null) {
                    ArcadeButton("◀ Voltar", onBack, color = Arcade.Cyan, minHeight = 44.dp, fontSize = 15.sp)
                    Spacer(Modifier.width(14.dp))
                }
                PixelText(title, size = 14.sp, modifier = Modifier.weight(1f))
            }
            Spacer(Modifier.size(12.dp))
            content()
        }
    }
}
