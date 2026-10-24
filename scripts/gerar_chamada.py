#!/usr/bin/env python3
"""Gera a chamada (hook) do estilo "Doentes por UFC" como PNG 720x1280 transparente.

Uso:
  python3 scripts/gerar_chamada.py saida.png \
      --topo "OLHA O QUE ESSES CARAS" \
      --principal "JÁ APRONTARAM!" --emoji assets/emoji-caveira.png \
      --sub "os melhores nocautes dos|lutadores do ufc 333"

  --topo       linha branca de contexto (Bebas Neue)
  --principal  linhas vermelhas de impacto (Bebas Neue); use | para quebrar linha
  --emoji      PNG colado à direita da última linha vermelha (opcional)
  --sub        linhas brancas em minúsculo (Oswald Bold), um pouco menores; | quebra linha
  --y          topo do bloco de texto (padrão 610, como no vídeo de referência)
"""
import argparse
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTES = os.path.join(RAIZ, "assets", "fonts")

W, H = 720, 1280
CENTRO_X = 316  # ~44 px à esquerda do centro, longe dos botões do Reels
BRANCO = (255, 255, 255, 255)
VERMELHO = (224, 0, 0, 255)


def fonte(nome, tamanho):
    return ImageFont.truetype(os.path.join(FONTES, nome), tamanho)


def render_linha(texto, f, cor, escala_x=1.0, espaco=1, grossura=0):
    """Desenha uma linha num layer próprio (com sombra leve) e devolve a imagem recortada."""
    larg = sum(f.getlength(c) + espaco + grossura * 2 for c in texto) + 20
    asc, desc = f.getmetrics()
    im = Image.new("RGBA", (int(larg) + 20, asc + desc + 20), (0, 0, 0, 0))
    sombra = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ds, d = ImageDraw.Draw(sombra), ImageDraw.Draw(im)
    x = 10
    for c in texto:
        # contorno da mesma cor = letra mais grossa, como na referência
        ds.text((x + grossura + 2, 12), c, font=f, fill=(0, 0, 0, 140), stroke_width=grossura, stroke_fill=(0, 0, 0, 140))
        d.text((x + grossura, 10), c, font=f, fill=cor, stroke_width=grossura, stroke_fill=cor)
        x += f.getlength(c) + espaco + grossura * 2
    sombra = sombra.filter(ImageFilter.GaussianBlur(2))
    im = Image.alpha_composite(sombra, im)
    im = im.crop(im.getbbox())
    if escala_x != 1.0:
        im = im.resize((max(1, int(im.width * escala_x)), im.height), Image.LANCZOS)
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("saida")
    ap.add_argument("--topo", default="")
    ap.add_argument("--principal", default="")
    ap.add_argument("--emoji")
    ap.add_argument("--sub", default="")
    ap.add_argument("--y", type=int, default=610)
    a = ap.parse_args()

    bebas_topo = fonte("BebasNeue-Regular.ttf", 56)
    bebas_principal = fonte("BebasNeue-Regular.ttf", 91)
    oswald = fonte("Oswald-Bold.ttf", 52)

    # (imagem, espaço acima)
    blocos = []
    if a.topo:
        blocos.append((render_linha(a.topo, bebas_topo, BRANCO, espaco=1, grossura=1), 0))
    for i, l in enumerate(filter(None, a.principal.split("|"))):
        blocos.append((render_linha(l, bebas_principal, VERMELHO, espaco=0, grossura=1), 24 if i == 0 else 8))
    for i, l in enumerate(filter(None, a.sub.split("|"))):
        blocos.append((render_linha(l, oswald, BRANCO, espaco=1), 22 if i == 0 else 8))

    n_principal = len(list(filter(None, a.principal.split("|"))))
    idx_ultima_vermelha = (1 if a.topo else 0) + n_principal - 1 if n_principal else None
    emoji = Image.open(a.emoji).convert("RGBA") if a.emoji else None

    texto = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    y = a.y
    for i, (im, acima) in enumerate(blocos):
        y += acima
        larg_total = im.width
        if emoji is not None and i == idx_ultima_vermelha:
            e = emoji.resize((int(emoji.width * im.height * 0.95 / emoji.height), int(im.height * 0.95)), Image.LANCZOS)
            larg_total += 10 + e.width
        x = CENTRO_X - larg_total // 2
        texto.alpha_composite(im, (x, y))
        if emoji is not None and i == idx_ultima_vermelha:
            texto.alpha_composite(e, (x + im.width + 10, y + (im.height - e.height) // 2))
        y += im.height
    fim = y

    # Faixa escura (~60% preto) atrás do texto, largura total, bordas suaves
    faixa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(faixa).rectangle([0, a.y - 15, W, fim + 25], fill=(0, 0, 0, 153))
    faixa = faixa.filter(ImageFilter.GaussianBlur(12))

    Image.alpha_composite(faixa, texto).save(a.saida)
    print(f"{a.saida}: bloco de y={a.y} a y={fim}")


if __name__ == "__main__":
    main()
