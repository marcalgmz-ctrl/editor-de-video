#!/usr/bin/env python3
"""Remove o fundo preto de um logo e salva PNG transparente recortado.

Uso: python3 scripts/limpar_logo.py logo-com-fundo-preto.png assets/logo-doentes-por-ufc.png
"""
import sys

from PIL import Image

PRETO, CHEIO = 25, 140  # brilho abaixo de PRETO some; acima de CHEIO fica 100% opaco

im = Image.open(sys.argv[1]).convert("RGB")
out = Image.new("RGBA", im.size)
src, dst = im.load(), out.load()
for y in range(im.size[1]):
    for x in range(im.size[0]):
        r, g, b = src[x, y]
        m = max(r, g, b)
        a = min(255, max(0, (m - PRETO) * 255 // (CHEIO - PRETO)))
        if a == 0:
            dst[x, y] = (0, 0, 0, 0)
        elif a < 255:
            # tira o preto misturado na borda para não ficar halo escuro
            dst[x, y] = (r * 255 // m, g * 255 // m, b * 255 // m, a)
        else:
            dst[x, y] = (r, g, b, a)
out.crop(out.getbbox()).save(sys.argv[2])
