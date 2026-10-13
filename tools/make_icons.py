#!/usr/bin/env python3
"""Gera o ícone do PERGUNTÁ-LO-EI (pixel art original): balão de fala com "?" sobre fundo arcade.

Saídas (em app/src/main/res):
  drawable/ic_launcher_foreground.xml, ic_launcher_background.xml, ic_launcher_monochrome.xml
  mipmap-anydpi-v26/ic_launcher.xml, ic_launcher_round.xml
  mipmap-{m,h,xh,xxh,xxxh}dpi/ic_launcher.png, ic_launcher_round.png
E docs/icone-512.png (vitrine).

Uso: python3 tools/make_icons.py
"""
import os
from PIL import Image, ImageDraw

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RES = os.path.join(ROOT, "app", "src", "main", "res")

# O = contorno, Y = balão, W = brilho, M = interrogação, S = sombra do "?"
ART = [
    "....OOOOOOOOOOOO....",
    "..OOYYYYYYYYYYYYOO..",
    ".OYWWYYYYYYYYYYYYYO.",
    ".OYWYYYMMMMMMYYYYYO.",
    "OYYYYYMMMMMMMMYYYYYO",
    "OYYYYMMMSYYYMMMSYYYO",
    "OYYYYMMMSYYYMMMSYYYO",
    "OYYYYYSSSYYMMMSSYYYO",
    "OYYYYYYYYYMMMSSYYYYO",
    "OYYYYYYYYMMMSSYYYYYO",
    "OYYYYYYYYMMMSYYYYYYO",
    ".OYYYYYYYYSSSYYYYYO.",
    ".OYYYYYYYYYYYYYYYYO.",
    ".OYYYYYYYMMMYYYYYYO.",
    "..OOYYYYYMMMSYYYOO..",
    "....OOYYOOOOOOOO....",
    "......OYYO..........",
    "......OYO...........",
    "......OO............",
]
COLORS = {"O": "#0D0A2B", "Y": "#FFE14D", "W": "#FFFFFF", "M": "#FF2E97", "S": "#B3105F"}
BG_TOP = "#3A1C8C"
BG_BOTTOM = "#1A0F4F"
STARS = [(14, 16), (90, 22), (20, 84), (88, 80), (30, 10), (78, 94), (96, 50), (10, 54)]

CELL = 3.3  # 20 células * 3.3 = 66dp (zona segura do ícone adaptativo)
OX = 21.0
OY = (108 - len(ART) * CELL) / 2


def runs(art, keys):
    """Agrupa células consecutivas da mesma cor em retângulos horizontais."""
    out = {}
    for y, row in enumerate(art):
        x = 0
        while x < len(row):
            c = row[x]
            if c in keys:
                start = x
                while x < len(row) and row[x] == c:
                    x += 1
                out.setdefault(c, []).append((start, y, x - start))
            else:
                x += 1
    return out


def path_for(rects):
    parts = []
    for (x, y, w) in rects:
        px, py = OX + x * CELL, OY + y * CELL
        parts.append(f"M{px:.2f},{py:.2f}h{w * CELL:.2f}v{CELL:.2f}h{-w * CELL:.2f}z")
    return "".join(parts)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def vector(paths):
    body = "\n".join(f'    <path android:fillColor="{c}" android:pathData="{d}" />' for c, d in paths)
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<!-- Gerado por tools/make_icons.py -->\n'
        '<vector xmlns:android="http://schemas.android.com/apk/res/android"\n'
        '    android:width="108dp" android:height="108dp"\n'
        '    android:viewportWidth="108" android:viewportHeight="108">\n'
        f"{body}\n</vector>\n"
    )


def make_vectors():
    r = runs(ART, COLORS.keys())
    # sombra pixelada deslocada do balão inteiro
    shadow = [(x, y, w) for c in "OYWMS" for (x, y, w) in r.get(c, [])]
    shadow_path = "".join(
        f"M{OX + x * CELL + 2.5:.2f},{OY + y * CELL + 2.5:.2f}h{w * CELL:.2f}v{CELL:.2f}h{-w * CELL:.2f}z" for (x, y, w) in shadow
    )
    fg = [("#66000000", shadow_path)] + [(COLORS[c], path_for(r[c])) for c in "OYWMS" if c in r]
    write(os.path.join(RES, "drawable", "ic_launcher_foreground.xml"), vector(fg))

    # Monocromático: balão sólido com "?" vazado (o sistema aplica a cor do tema).
    mono_body = vector([("#FF000000", path_for([x for c in "OYW" for x in r.get(c, [])]))])
    write(os.path.join(RES, "drawable", "ic_launcher_monochrome.xml"), mono_body)

    stars = "".join(f"M{x},{y}h3v3h-3z" for (x, y) in STARS)
    floor = "".join(f"M{i * 12},{96 + (i % 2) * 6}h6v6h-6z" for i in range(9))
    bg = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<!-- Gerado por tools/make_icons.py -->\n'
        '<vector xmlns:android="http://schemas.android.com/apk/res/android"\n'
        '    xmlns:aapt="http://schemas.android.com/aapt"\n'
        '    android:width="108dp" android:height="108dp"\n'
        '    android:viewportWidth="108" android:viewportHeight="108">\n'
        '    <path android:pathData="M0,0h108v108h-108z">\n'
        '        <aapt:attr name="android:fillColor">\n'
        f'            <gradient android:type="linear" android:startX="0" android:startY="0" android:endX="0" android:endY="108"'
        f' android:startColor="{BG_TOP}" android:endColor="{BG_BOTTOM}" />\n'
        '        </aapt:attr>\n'
        '    </path>\n'
        f'    <path android:fillColor="#FF00E5FF" android:pathData="{stars}" />\n'
        f'    <path android:fillColor="#5500E5FF" android:pathData="{floor}" />\n'
        '</vector>\n'
    )
    write(os.path.join(RES, "drawable", "ic_launcher_background.xml"), bg)

    adaptive = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n'
        '    <background android:drawable="@drawable/ic_launcher_background" />\n'
        '    <foreground android:drawable="@drawable/ic_launcher_foreground" />\n'
        '    <monochrome android:drawable="@drawable/ic_launcher_monochrome" />\n'
        '</adaptive-icon>\n'
    )
    write(os.path.join(RES, "mipmap-anydpi-v26", "ic_launcher.xml"), adaptive)
    write(os.path.join(RES, "mipmap-anydpi-v26", "ic_launcher_round.xml"), adaptive)


def hex_rgba(h, alpha=255):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (alpha,)


def render(size_px):
    """Renderiza o ícone completo (fundo + frente) em alta resolução e reduz."""
    scale = 10
    full = 108 * scale
    img = Image.new("RGBA", (full, full))
    d = ImageDraw.Draw(img)
    top, bottom = hex_rgba(BG_TOP), hex_rgba(BG_BOTTOM)
    for y in range(full):
        t = y / full
        d.line([(0, y), (full, y)], fill=tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)) + (255,))
    for (x, y) in STARS:
        d.rectangle([x * scale, y * scale, (x + 3) * scale - 1, (y + 3) * scale - 1], fill=hex_rgba("#00E5FF"))
    for i in range(9):
        x, y = i * 12, 96 + (i % 2) * 6
        d.rectangle([x * scale, y * scale, (x + 6) * scale - 1, (y + 6) * scale - 1], fill=(0, 229, 255, 85))
    shadow = Image.new("RGBA", (full, full), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    for y, row in enumerate(ART):
        for x, c in enumerate(row):
            if c in COLORS:
                px, py = (OX + x * CELL + 2.5) * scale, (OY + y * CELL + 2.5) * scale
                sd.rectangle([px, py, px + CELL * scale, py + CELL * scale], fill=(0, 0, 0, 102))
    img = Image.alpha_composite(img, shadow)
    d = ImageDraw.Draw(img)
    for y, row in enumerate(ART):
        for x, c in enumerate(row):
            if c in COLORS:
                px, py = (OX + x * CELL) * scale, (OY + y * CELL) * scale
                d.rectangle([px, py, px + CELL * scale, py + CELL * scale], fill=hex_rgba(COLORS[c]))
    # Ícone legado: recorta a área útil (como a máscara do launcher faria).
    crop = 15 * scale
    img = img.crop((crop, crop, full - crop, full - crop))
    return img.resize((size_px, size_px), Image.LANCZOS)


def masked(img, round_mask):
    n = img.size[0]
    mask = Image.new("L", (n * 4, n * 4), 0)
    md = ImageDraw.Draw(mask)
    if round_mask:
        md.ellipse([0, 0, n * 4 - 1, n * 4 - 1], fill=255)
    else:
        md.rounded_rectangle([0, 0, n * 4 - 1, n * 4 - 1], radius=n * 4 // 6, fill=255)
    mask = mask.resize((n, n), Image.LANCZOS)
    out = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def make_pngs():
    sizes = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}
    for dens, px in sizes.items():
        folder = os.path.join(RES, f"mipmap-{dens}")
        os.makedirs(folder, exist_ok=True)
        base = render(px)
        masked(base, False).save(os.path.join(folder, "ic_launcher.png"))
        masked(base, True).save(os.path.join(folder, "ic_launcher_round.png"))
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    masked(render(512), False).save(os.path.join(ROOT, "docs", "icone-512.png"))


if __name__ == "__main__":
    make_vectors()
    make_pngs()
    print("ícones gerados")
