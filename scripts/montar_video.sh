#!/usr/bin/env bash
# Monta um vídeo no estilo "Doentes por UFC" (9:16, 720x1280).
#
# Uso:
#   scripts/montar_video.sh entrada.mp4 legendas.ass saida.mp4 "@perfilfonte" [logo.png] [pasta_fontes]
#
# - entrada.mp4    clipe já cortado (qualquer proporção; normalmente 16:9)
# - legendas.ass   cópia editada de templates/estilo-doentes-por-ufc.ass, ou "-" para não usar
# - "@perfilfonte" crédito exibido como "VÍDEO: @PERFILFONTE"
# - logo.png       padrão: assets/logo-doentes-por-ufc.png
# - pasta_fontes   padrão: assets/fonts
#
# Chamada em PNG (gerada por scripts/gerar_chamada.py), opcional, via variáveis:
#   CHAMADA=chamada.png CHAMADA_INI=0.2 CHAMADA_FIM=2.8 scripts/montar_video.sh ...
set -euo pipefail

if [ $# -lt 4 ]; then
  sed -n '2,15p' "$0"
  exit 1
fi

RAIZ=$(cd "$(dirname "$0")/.." && pwd)
IN=$1
ASS=$2
OUT=$3
CREDITO="VÍDEO: $(echo "$4" | tr '[:lower:]' '[:upper:]')"
LOGO=${5:-$RAIZ/assets/logo-doentes-por-ufc.png}
FONTES=${6:-$RAIZ/assets/fonts}
CHAMADA=${CHAMADA:-}
CHAMADA_INI=${CHAMADA_INI:-0.2}
CHAMADA_FIM=${CHAMADA_FIM:-2.8}

# Fundo: o próprio vídeo ampliado, desfocado e escurecido (aparece nas faixas de cima e de baixo).
# Frente: recorte central 3:4 (720x960) colado em y=180.
FILTRO="[0:v]split[a][b];\
[a]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,boxblur=24:2,eq=brightness=-0.22:saturation=1.15[bg];\
[b]scale=720:960:force_original_aspect_ratio=increase,crop=720:960[fg];\
[bg][fg]overlay=0:180,setsar=1[v0]"

INPUTS=(-i "$IN" -loop 1 -i "$LOGO")
FILTRO="$FILTRO;[1:v]scale=120:-1[lg];[v0][lg]overlay=(W-w)/2:70:shortest=1[v1]"

if [ -n "$CHAMADA" ]; then
  # Entra e sai com fade de 0,12 s, como no vídeo de referência
  INPUTS+=(-loop 1 -i "$CHAMADA")
  FADE_SAIDA=$(echo "$CHAMADA_FIM - 0.12" | bc -l)
  FILTRO="$FILTRO;[2:v]format=rgba,fade=in:st=$CHAMADA_INI:d=0.12:alpha=1,fade=out:st=$FADE_SAIDA:d=0.12:alpha=1[ch];\
[v1][ch]overlay=0:0:shortest=1:enable='between(t,$CHAMADA_INI,$CHAMADA_FIM)'[v2]"
else
  FILTRO="$FILTRO;[v1]null[v2]"
fi

CREDITO_ESC=$(printf '%s' "$CREDITO" | sed "s/[:\\\\']/\\\\&/g")
FILTRO="$FILTRO;[v2]drawtext=fontfile='$FONTES/Montserrat-Medium.ttf':text='$CREDITO_ESC':fontsize=15:fontcolor=0xD8D8D8:x=(w-text_w)/2:y=155"
if [ "$ASS" != "-" ]; then
  FILTRO="$FILTRO,ass='$ASS':fontsdir='$FONTES'"
fi
FILTRO="$FILTRO,format=yuv420p[v]"

ffmpeg -y "${INPUTS[@]}" -filter_complex "$FILTRO" -map "[v]" -map 0:a? \
  -r 30 -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 192k -ar 48000 \
  -movflags +faststart "$OUT"
