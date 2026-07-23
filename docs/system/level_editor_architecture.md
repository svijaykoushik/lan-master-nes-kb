---
type: Build System
title: Level Editor Architecture & 3-Bit Level Format
description: Analysis of the lanme level editor and 3-bit binary level packing format.
resource: sources/Source/lanme/src/Unit1.cpp
tags:
  - system
  - tools
  - level-format
  - compression
timestamp: 2026-07-24T00:20:00Z
---

# Level Editor Architecture & 3-Bit Level Data Format

## Overview

The companion level editor for *Lan Master* (`lanme`) is a Delphi/C++ Builder application written to author, solve, and compile all 50 game levels into compact 60-byte level definition blocks for the 6502 ROM.

---

## 3-Bit Tile Packing Specification

To store a full $12 \times 12$ grid (144 tiles) in 54 bytes, `lanme` uses a 3-bit packing scheme.

### Tile Palette Index Mapping (`tilePaletteReverse`)

Rather than storing raw 8-bit tile IDs, the 8 most frequent tile types used in level creation are mapped to 3-bit palette indices (0–7):

| 3-Bit Index | Raw Tile ID | Description |
| :--- | :--- | :--- |
| `000` (0) | 0 | Empty space |
| `001` (1) | 1 | Horizontal wire |
| `010` (2) | 2 | Vertical wire |
| `011` (3) | 4 | Crossed connection wire |
| `100` (4) | 5 | Left-Down corner wire |
| `101` (5) | 6 | Left-Up corner wire |
| `110` (6) | 7 | Right-Up corner wire |
| `111` (7) | 8 | Right-Down corner wire |

---

## 24-Bit Bitpacking Algorithm (8 Tiles per 3 Bytes)

Each group of 8 consecutive grid tiles is packed into 3 bytes (24 bits total):

$$\text{Bit Stream} = [T_0 \ll 21] \,|\, [T_1 \ll 18] \,|\, [T_2 \ll 15] \,|\, [T_3 \ll 12] \,|\, [T_4 \ll 9] \,|\, [T_5 \ll 6] \,|\, [T_6 \ll 3] \,|\, T_7$$

This packs 144 tiles into exactly $\frac{144 \times 3}{8} = 54$ bytes.

---

## 60-Byte Level Header Layout

Each compiled level block comprises exactly 60 bytes:

```text
Offset | Length | Purpose & Formula
---------------------------------------------------------------------------------------
$00-$35| 54 B   | 3-bit packed 12x12 grid layout (144 tiles)
$36-$37| 2 B    | Fixed-point score multiplier: GAME_TERM_FP = ceil(100.0 * 256.0 / tcnt)
$38-$39| 2 B    | GAME_TIME (Target completion time in 60Hz frames, Little-Endian)
$3A    | 1 B    | GAME_TERM_CNT (Total number of terminals on board)
$3B    | 1 B    | GAME_START_POS (Offset in GAME_MAP where level splay animation begins)
```

---

## Technical Formulas & Automation

1. **Fixed-Point Score Multiplier**: Computes `GAME_TERM_FP = ceil(100.0 * 256.0 / tcnt)`. In assembly, adding `GAME_TERM_FP` for each connected terminal allows fast 16-bit integer addition to compute exact 0–100% online percentage display.
2. **Auto Center Finder**: `lanme` searches outward from grid center `(6,6)` to locate the first non-zero tile for `GAME_START_POS`.

---

## Citations
[1] [Source Code: Unit1.cpp](../../sources/Source/lanme/src/Unit1.cpp)
[2] [Source Code: levels.asm](../../sources/Source/levels.asm)
