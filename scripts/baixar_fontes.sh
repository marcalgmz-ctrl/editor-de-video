#!/usr/bin/env bash
# Baixa Bebas Neue, Montserrat e Oswald (OFL) do npm/Fontsource e converte para TTF em assets/fonts.
# Requer: npm, python3 com fonttools (pip install fonttools).
set -euo pipefail
RAIZ=$(cd "$(dirname "$0")/.." && pwd)
TMP=$(mktemp -d)
mkdir -p "$RAIZ/assets/fonts"
cd "$TMP"
for p in bebas-neue montserrat oswald; do
  npm pack -q "@fontsource/$p" >/dev/null
  mkdir -p "$p" && tar xzf fontsource-$p-*.tgz -C "$p"
  cp "$p/package/LICENSE" "$RAIZ/assets/fonts/OFL-$p.txt"
done
for spec in "bebas-neue/bebas-neue-latin-400:BebasNeue-Regular" \
            "montserrat/montserrat-latin-500:Montserrat-Medium" \
            "montserrat/montserrat-latin-800:Montserrat-ExtraBold" \
            "oswald/oswald-latin-700:Oswald-Bold"; do
  src=${spec%%:*}; out=${spec##*:}
  pkg=${src%%/*}; file=${src##*/}
  python3 -c "
import sys
from fontTools.ttLib import TTFont
t = TTFont(sys.argv[1]); t.flavor = None; t.save(sys.argv[2])
" "$pkg/package/files/$file-normal.woff" "$RAIZ/assets/fonts/$out.ttf"
done
rm -rf "$TMP"
ls "$RAIZ/assets/fonts"
