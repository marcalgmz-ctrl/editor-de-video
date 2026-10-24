#!/usr/bin/env bash
# Gera a capa do Reels no estilo "Doentes por UFC" (1080x1920, mesmo layout do vídeo em escala 1,5x).
#
# Uso:
#   scripts/gerar_capa.sh video.mp4 SEGUNDO chamada.png saida.jpg "@perfilfonte" [logo.png] [pasta_fontes]
#
# - video.mp4      vídeo de origem (o quadro da capa sai dele)
# - SEGUNDO        instante do quadro, ex.: 36.5
# - chamada.png    gerada com: scripts/gerar_chamada.py chamada.png --escala 1.5 --x 360 ...
#                  (--x 360 centraliza: na capa não há botões do Reels por cima)
# - "@perfilfonte" crédito exibido como "VÍDEO: @PERFILFONTE"
#
# O grid do perfil mostra só o miolo 3:4 (y=240 a 1680), por isso a chamada fica dentro do vídeo principal.
set -euo pipefail

if [ $# -lt 5 ]; then
  sed -n '2,13p' "$0"
  exit 1
fi

RAIZ=$(cd "$(dirname "$0")/.." && pwd)
IN=$1
T=$2
CHAMADA=$3
OUT=$4
CREDITO="VÍDEO: $(echo "$5" | tr '[:lower:]' '[:upper:]')"
LOGO=${6:-$RAIZ/assets/logo-doentes-por-ufc.png}
FONTES=${7:-$RAIZ/assets/fonts}

CREDITO_ESC=$(printf '%s' "$CREDITO" | sed "s/[:\\\\']/\\\\&/g")
FILTRO="[0:v]split[a][b];\
[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=36:2,eq=brightness=-0.22:saturation=1.15[bg];\
[b]scale=1080:1440:force_original_aspect_ratio=increase,crop=1080:1440[fg];\
[bg][fg]overlay=0:270[v0];\
[1:v]scale=180:-1[lg];[v0][lg]overlay=(W-w)/2:105[v1];\
[v1][2:v]overlay=0:0[v2];\
[v2]drawtext=fontfile='$FONTES/Montserrat-Medium.ttf':text='$CREDITO_ESC':fontsize=22:fontcolor=0xD8D8D8:x=(w-text_w)/2:y=232"

ffmpeg -v error -y -ss "$T" -i "$IN" -i "$LOGO" -i "$CHAMADA" -filter_complex "$FILTRO" \
  -frames:v 1 -q:v 2 "$OUT"
echo "$OUT"
