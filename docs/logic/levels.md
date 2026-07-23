---
type: Assembly Module
title: Level Definitions
description: Data definitions for the 50 game levels, including map layouts, timing, and terminal locations.
resource: sources/Source/levels.asm
tags: [logic, data, levels]
timestamp: 2026-06-29T12:10:00Z
---

# Level Structure & Binary Specifications

The `levels.asm` file contains definitions for all 50 game stages. Levels are indexed via `levList`, a table of 16-bit pointers (`.dw`) to stage data blocks (`.level1` through `.level50`).

---

## 60-Byte Level Block Layout

Each level is defined by an exact 60-byte data block:

```text
Offset | Length | Field Name        | Purpose & Assembly Description
------------------------------------------------------------------------------------------------------
$00-$35| 54 B   | Packed Map Data   | 3-bit packed 12x12 grid (144 tiles total, 8 tiles per 3 bytes).
$36-$37| 2 B    | GAME_TERM_FP      | 16-bit fixed-point score scaling factor = ceil(100.0 * 256.0 / tcnt).
$38-$39| 2 B    | GAME_TIME         | Target completion time limit in 60Hz frames (16-bit Little-Endian).
$3A    | 1 B    | GAME_TERM_CNT     | Total number of terminal computer tiles present in level.
$3B    | 1 B    | GAME_START_POS    | Offset in GAME_MAP ($0300) where level splay animation begins.
```

---

## Technical Details & Data Formulas

1. **3-Bit Tile Packing**: Compresses 144 grid tiles into 54 bytes by mapping tile IDs to 3-bit palette indices (`000`–`111`) and storing 8 tiles across 24 bits (3 bytes). See [Level Editor Architecture](../system/level_editor_architecture.md).
2. **Fixed-Point Online Percentage (`GAME_TERM_FP`)**: Stores $\left\lceil \frac{100 \times 256}{N_{\text{terminals}}} \right\rceil$. As the BFS engine discovers connected terminals, it accumulates `GAME_TERM_FP` to calculate exact 0–100% online status for HUD display without requiring hardware division.
3. **Start Position (`GAME_START_POS`)**: Computed automatically by `lanme` by searching outwards from center grid `(6,6)` to locate the first non-empty tile for the splay load animation.

---

## Citations
[1] [Source Code: levels.asm](../../sources/Source/levels.asm)
[2] [Source Code: game.asm](../../sources/Source/game.asm)
[3] [Level Editor Source: Unit1.cpp](../../sources/Source/lanme/src/Unit1.cpp)

