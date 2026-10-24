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
    ap.add_argument("--x", type=int, default=CENTRO_X, help="centro horizontal do bloco (360 = centro da tela)")
    ap.add_argument("--escala", type=float, default=1.0, help="1.5 gera em 1080x1920 (capa)")
    a = ap.parse_args()
    k = a.escala

    bebas_topo = fonte("BebasNeue-Regular.ttf", round(56 * k))
    bebas_principal = fonte("BebasNeue-Regular.ttf", round(91 * k))
    oswald = fonte("Oswald-Bold.ttf", round(52 * k))

    # (imagem, espaço acima)
    blocos = []
    if a.topo:
        blocos.append((render_linha(a.topo, bebas_topo, BRANCO, espaco=1, grossura=1), 0))
    for i, l in enumerate(filter(None, a.principal.split("|"))):
        blocos.append((render_linha(l, bebas_principal, VERMELHO, espaco=0, grossura=1), round((24 if i == 0 else 8) * k)))
    for i, l in enumerate(filter(None, a.sub.split("|"))):
        blocos.append((render_linha(l, oswald, BRANCO, espaco=1), round((22 if i == 0 else 8) * k)))

    n_principal = len(list(filter(None, a.principal.split("|"))))
    idx_ultima_vermelha = (1 if a.topo else 0) + n_principal - 1 if n_principal else None
    emoji = Image.open(a.emoji).convert("RGBA") if a.emoji else None

    larg_tela, alt_tela, y0 = round(W * k), round(H * k), round(a.y * k)
    texto = Image.new("RGBA", (larg_tela, alt_tela), (0, 0, 0, 0))
    y = y0
    for i, (im, acima) in enumerate(blocos):
        y += acima
        larg_total = im.width
        if emoji is not None and i == idx_ultima_vermelha:
            e = emoji.resize((int(emoji.width * im.height * 0.95 / emoji.height), int(im.height * 0.95)), Image.LANCZOS)
            larg_total += round(10 * k) + e.width
        x = round(a.x * k) - larg_total // 2
        margem = round(24 * k)
        if x < margem or x + larg_total > larg_tela - margem:
            print(f"AVISO: linha {i + 1} encosta na borda ({larg_total} px); encurte o texto ou quebre com |")
        texto.alpha_composite(im, (x, y))
        if emoji is not None and i == idx_ultima_vermelha:
            texto.alpha_composite(e, (x + im.width + round(10 * k), y + (im.height - e.height) // 2))
        y += im.height
    fim = y

    # Faixa escura (~60% preto) atrás do texto, largura total, bordas suaves
    faixa = Image.new("RGBA", (larg_tela, alt_tela), (0, 0, 0, 0))
    ImageDraw.Draw(faixa).rectangle([0, y0 - round(15 * k), larg_tela, fim + round(25 * k)], fill=(0, 0, 0, 153))
    faixa = faixa.filter(ImageFilter.GaussianBlur(12 * k))

    Image.alpha_composite(faixa, texto).save(a.saida)
    print(f"{a.saida}: bloco de y={y0} a y={fim}")


if __name__ == "__main__":
    main()
