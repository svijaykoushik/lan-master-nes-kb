---
type: Assembly Module
title: Rle
description: Analysis of the RLE decompression logic used for background graphics.
resource: sources/Source/rle.asm
tags: [assets, graphics, compression]
timestamp: 2026-06-29T12:40:00Z
---

# Implementation

The `unrle` routine (`rle.asm`) expands RLE compressed graphics streams directly into PPU VRAM ($2000 / $2400 nametables).

---

## Stream Decompression Algorithm

1. **Header Byte (Tag)**: The first byte of an RLE stream defines the `RLE_TAG` byte value.
2. **Literal Processing**:
   - Fetches byte $B$. If $B \ne \text{RLE\_TAG}$, $B$ is written to `PPU_DATA` ($2007) and saved as `RLE_BYTE`.
3. **Run-Length Expansion**:
   - If $B = \text{RLE\_TAG}$, the subsequent byte is read as run count $N$.
   - **Stream Termination Check (EOF)**: If $N = 0$, `unrle` immediately terminates decompression and returns.
   - Otherwise, `RLE_BYTE` is repeated $N$ times to `PPU_DATA`.

---

## Citations
[1] [Source Code: rle.asm](../../sources/Source/rle.asm)
[2] [Source Code: game.asm](../../sources/Source/game.asm)

