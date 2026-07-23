---
type: Assembly Module
title: "Timing & Sync"
description: Low-level routines for synchronizing game logic and rendering with the NES NMI and VBlank.
resource: sources/Source/game.asm
tags: [system, timing, sync, hardware]
timestamp: 2026-07-03T11:00:00Z
---

# Implementation

*Lan Master* uses strict NMI timing synchronization to ensure consistent framerates across both NTSC (60Hz) and PAL (50Hz) NES consoles.

---

## Blargg's Cycle-Timing NTSC/PAL Detection (`detectNTSC`)

During boot initialization, `game.asm` executes `detectNTSC` (a cycle-timing detection algorithm originally authored by Blargg):

```assembly
detectNTSC:
    jsr waitVBlank       ; Wait for VBlank start
    ldx #52              ; Outer delay loop (52 iterations)
.l1:
    ldy #24              ; Inner delay loop (24 iterations)
.l2:
    dey
    bne .l2
    dex
    bne .l1
    bit PPU_STATUS       ; Read bit 7 ($2002)
    bpl .isPal           ; If VBlank flag is cleared -> PAL system
    lda #1               ; NTSC detected
    sta GAME_NTSC
    rts
.isPal:
    lda #0               ; PAL detected
    sta GAME_NTSC
    rts
```

### Technical Explanation
- **NTSC VBlank**: Lasts ~2,273 CPU cycles (20 scanlines).
- **PAL VBlank**: Lasts ~7,500 CPU cycles (70 scanlines).
- After waiting ~2,500 cycles via nested loops, reading `PPU_STATUS` bit 7 determines if VBlank is still active (PAL) or has already ended (NTSC).

---

## 50Hz Frame Normalization (`ntscIsSkip` / `waitNMI50`)

Because NTSC runs at 60Hz and PAL runs at 50Hz, uncompensated games run 20% faster on NTSC.

To normalize gameplay timing:
- In NTSC mode, `ntscIsSkip` tracks frames using `FRAME_CNT2`.
- Drops 1 out of every 6 frames (`FRAME_CNT2 == 5`), synchronizing game logic to 50Hz updates while maintaining 60Hz audio updates via `FamiToneUpdate`.

---

## Citations
[1] [Source Code: game.asm](../../sources/Source/game.asm)
[2] [Dynamic Vectoring Spec: nmi_vectoring.md](nmi_vectoring.md)

