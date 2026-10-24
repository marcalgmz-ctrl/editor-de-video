#!/usr/bin/env python3
"""Renderiza um emoji colorido (Noto Color Emoji) como PNG transparente.

Uso: python3 scripts/gerar_emoji.py 💀 assets/emoji-caveira.png
"""
import sys

from PIL import Image, ImageDraw, ImageFont

FONTE = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"

f = ImageFont.truetype(FONTE, 109)  # Noto Color Emoji só funciona no tamanho 109
im = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
ImageDraw.Draw(im).text((10, 10), sys.argv[1], font=f, embedded_color=True)
im.crop(im.getbbox()).save(sys.argv[2])
