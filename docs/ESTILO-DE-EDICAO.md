# Estilo de edição — "Doentes por UFC"

Análise do vídeo de referência (Dillon Danis × Arman Tsarukyan, coletiva RAF 14) para repetir o mesmo estilo nos próximos vídeos.

| | |
|---|---|
| Formato | 9:16, **720×1280**, 30 fps, H.264 + AAC 48 kHz estéreo |
| Duração | **24 s** |
| Áudio | **Só o áudio original** (sem música, sem efeitos sonoros), pico −0,3 dB, média −19,7 dB |
| Final | Corte seco, sem CTA nem tela final |

Imagens de referência: [`referencia/01-hook.jpg`](referencia/01-hook.jpg), [`referencia/02-legenda.jpg`](referencia/02-legenda.jpg), [`referencia/03-linha-do-tempo.jpg`](referencia/03-linha-do-tempo.jpg) (1 quadro por segundo).

---

## 1. Layout da tela (fixo durante o vídeo todo)

```
y=0     ┌────────────────────────────┐
        │   fundo desfocado + escuro │
y≈70    │        [LOGO DOENTES       │  logo centralizado, ~120 px de largura
        │          POR UFC]          │
y≈155   │  VÍDEO: @PERFILDAFONTE     │  crédito, ~15 px, cinza-claro (#D8D8D8), caixa alta
y=180   ├────────────────────────────┤
        │                            │
        │   VÍDEO PRINCIPAL 720×960  │  recorte 3:4 do meio do vídeo original 16:9
        │        (proporção 3:4)     │
        │                            │
y=1140  ├───────────────────────────┤
        │   fundo desfocado + escuro │
y=1280  └────────────────────────────┘
```

- **Fundo:** o próprio vídeo ampliado para cobrir 720×1280, com desfoque forte e escurecido (fica um roxo/cinza bem escuro). Ele aparece só nas faixas de cima (0–180) e de baixo (1140–1280).
- **Vídeo principal:** recorte 3:4 colado de y=180 a y=1140. Em cada take, o recorte acompanha quem está em foco (ex.: no Dillon quando ele mostra a camisa).
- **Logo + crédito** ficam na faixa de cima o vídeo inteiro. O crédito sempre no formato `VÍDEO: @PERFIL`.

## 2. Estrutura / ritmo (linha do tempo)

| Tempo | Take | O que acontece | Texto na tela |
|---|---|---|---|
| 0,0–2,8 s | Plano aberto dos dois sentados | Contexto, "calmaria antes da tempestade" | **HOOK** (entra em 0,2 s) |
| 2,8–6,4 s | Dillon em pé mostrando a camisa | Provocação: o motivo da treta | **Legendas traduzidas** (2 frases) |
| 6,4–11,2 s | Panorâmica até o Arman | Arman levanta e parte pra cima | Nada, a ação fala sozinha |
| 11,2–13 s | Ângulo da plateia | Confusão no palco | Nada |
| 13–16 s | Ângulo mais aberto (celular de fã) | Seguranças separando | Nada |
| 16–24 s | Close de celular de fã | Arman sendo segurado (clímax) | Nada |

Padrão da narrativa:
1. **Hook (0–3 s):** a manchete resume a história toda antes de qualquer coisa acontecer.
2. **Contexto (3–6 s):** só a fala que explica *por que* deu briga, legendada em PT-BR.
3. **Ação (6 s até o fim):** briga sem texto, juntando vários ângulos (oficial e celular de fã) em ordem cronológica.
4. **Fim seco:** termina ainda na ação, sem despedida. Isso ajuda o vídeo a rodar em loop.

Cortes: **todos secos** (sem transição nem zoom digital). O dinamismo vem da troca de ângulo, cerca de 1 corte a cada 2–5 s, mais rápido na parte da ação.

## 3. Hook (manchete de abertura)

Referência: [`referencia/01-hook.jpg`](referencia/01-hook.jpg)

- **Tempo:** entra em **0,2 s** com fade de ~0,12 s e sai em **~2,8 s** com fade curto, junto com o 1º corte.
- **Fonte:** condensada e bem grossa, toda em caixa alta (**Bebas Neue** ou similar: Anton, Oswald Bold).
- **Linha 1 (contexto):** branca `#FFFFFF`, ~56 px, uma linha, termina com reticências (`...`).
  Ex.: `MEXERAM COM O CHIMAEV...`
- **Linhas 2–3 (o impacto):** vermelha `#E00000`, ~82 px (≈1,5× a linha 1), quebrada em 2 linhas equilibradas, termina com `!`.
  Ex.: `E O ARMAN NÃO / DEIXOU BARATO!`
- **Faixa atrás do texto:** retângulo preto com **~60% de opacidade** na largura toda, de y≈595 a y≈870, com bordas desfocadas (sem caixa com borda definida).
- **Posição:** centro do bloco em **x≈316** (uns 44 px à esquerda do centro, longe dos botões do Reels/TikTok na direita), na metade de baixo do vídeo principal (y≈610–850). Não pode cobrir o rosto de ninguém.
- Sem contorno; só uma sombra bem leve.

**Fórmula do texto:** `[QUEM/O QUE FOI PROVOCADO]...` + `[QUEM REAGIU] + [GÍRIA DE REAÇÃO]!`
Outros exemplos no mesmo molde:
- `PROVOCARAM O POATAN...` / `E ELE RESPONDEU NA HORA!`
- `FALARAM DO PAI DO ISLAM...` / `E O MAKHACHEV PERDEU A PACIÊNCIA!`

## 4. Legendas (tradução das falas)

Referência: [`referencia/02-legenda.jpg`](referencia/02-legenda.jpg)

- **Só nas falas que dão contexto**, não no vídeo todo. Aqui foram 2 frases, de 3,0 s a 6,3 s.
- **Fonte:** Montserrat Medium (sans-serif limpa), **branca**, ~29 px, **sem contorno nem caixa**, sombra bem sutil.
- **Posição:** centralizada (x=360), centro em **y≈831** (logo abaixo da mesa/da pessoa, na faixa escura do cenário).
- **Formato:** frase normal (maiúscula só no começo), com pontuação, **no máximo 2 linhas** de ~20 caracteres. Cita o texto de camisa/cartaz entre aspas: `Isso aqui: "Khamzat é minha cadela".`
- **Animação:** fade de entrada e saída de ~0,15 s, sem pop nem destaque palavra por palavra.
- **Duração de cada legenda:** ~1,5–1,7 s, com intervalo de ~0,1 s entre elas.

## 5. Cor e áudio

- Sem color grading pesado: as imagens mantêm a cor original da fonte. Só o fundo desfocado é escurecido.
- Paleta da marca: preto/roxo escuro (fundo), branco (texto de apoio), vermelho `#E00000` (destaque e logo `#F80810`).
- Áudio original do evento, sem trilha. O som da confusão (gritos da plateia) é o que segura a atenção.
- Normalizar para pico perto de −0,3 dB e média em torno de −20 dB.

## 6. Checklist para o próximo vídeo

- [ ] Clipe de 20–30 s, começando **no momento de calma antes** do acontecimento
- [ ] Hook em 2 cores (linha branca de contexto `...` + 2 linhas vermelhas de impacto `!`), de 0,2 a 2,8 s
- [ ] Legenda só na fala que explica o motivo, Montserrat branca, sem caixa
- [ ] Ação sem texto, com vários ângulos em ordem cronológica e cortes secos
- [ ] Layout 720×1280: fundo desfocado + vídeo 3:4 em y=180, logo + `VÍDEO: @FONTE` em cima
- [ ] Só áudio original, final seco

## 7. Ferramentas neste repositório

- [`templates/estilo-doentes-por-ufc.ass`](../templates/estilo-doentes-por-ufc.ass): estilos prontos (faixa do hook, hook branco, hook vermelho, legenda) com tamanhos, cores, posições e fades já ajustados. Copie o arquivo e troque só os textos e tempos em `[Events]`.
- [`scripts/montar_video.sh`](../scripts/montar_video.sh): monta o layout (fundo desfocado, recorte 3:4, logo, crédito) e aplica o `.ass` via ffmpeg.

- [`scripts/gerar_chamada.py`](../scripts/gerar_chamada.py): gera a chamada como PNG transparente, com fontes, tamanhos, faixa escura e posição calibradas contra o vídeo de referência. Aceita emoji colorido e uma linha extra em minúsculo (Oswald Bold).
- `assets/`: logo sem fundo, emoji 💀 em PNG e as fontes (Bebas Neue, Montserrat, Oswald; licença OFL).

```bash
# chamada em PNG
python3 scripts/gerar_chamada.py chamada.png \
  --topo "OLHA O QUE ESSES CARAS" --principal "JÁ APRONTARAM!" --emoji assets/emoji-caveira.png \
  --sub "os melhores nocautes dos|lutadores do ufc 333"

# vídeo final (sem legendas: "-" no lugar do .ass)
CHAMADA=chamada.png CHAMADA_INI=0.2 CHAMADA_FIM=2.8 \
  scripts/montar_video.sh clipe.mp4 - saida.mp4 "@ufc"
```

O logo e as fontes de `assets/` são usados por padrão. Se a chamada tiver 3 partes (topo, principal e uma linha em minúsculo), a linha de baixo usa Oswald Bold, branca e um pouco menor que a principal.
