---
type: Reference
title: Pattern Mapping
description: Mapping of internal logical tile IDs to PPU character pattern indices in patterns.chr.
resource: sources/Source/game.asm
tags: [assets, graphics, ppu, mapping]
timestamp: 2026-07-03T10:30:00Z
---

# Pattern Mapping Overview

*Lan Master* uses indirect indexing via `tilesTable` in `game.asm` to map logical game tiles (`GAME_MAP`) to physical NES PPU character patterns in `patterns.chr`.

---

## Technical Mapping Architecture

Each logical tile in the $12 \times 12$ grid is a $16 \times 16$ pixel square comprising a $2 \times 2$ matrix of four $8 \times 8$ PPU CHR pattern tiles:

```text
+-------------------+--------------------+
|  Top-Left (B0)    |   Top-Right (B1)   |
|  (8x8 CHR Tile)   |   (8x8 CHR Tile)   |
+-------------------+--------------------+
|  Bottom-Left (B2) |   Bottom-Right (B3)|
|  (8x8 CHR Tile)   |   (8x8 CHR Tile)   |
+-------------------+--------------------+
```

### Translation Routine (`updateTile`)
1. Multiplies logical Tile ID by 4 (`asl a`, `asl a`) to index into `tilesTable`.
2. Reads 4 CHR tile byte indices: `Byte 0` (Top-Left), `Byte 1` (Top-Right), `Byte 2` (Bottom-Left), `Byte 3` (Bottom-Right).
3. Writes these 4 CHR pattern bytes into PPU VRAM across two horizontal scanlines.

---

## Complete Logical to Physical Tile Map

| Logical ID | Description | Terminal State | Top CHR Indices | Bottom CHR Indices |
| :--- | :--- | :--- | :--- | :--- |
| `0` | Empty Space | N/A | `$8d, $8e` | `$a1, $a2` |
| `1` | Horizontal Wire | N/A | `$8f, $90` | `$a3, $a4` |
| `2` | Vertical Wire | N/A | `$91, $92` | `$a5, $a6` |
| `3` | Crossed Separate | N/A | `$93, $94` | `$a7, $a8` |
| `4` | Crossed Connection | N/A | `$95, $96` | `$a9, $aa` |
| `5` | Left-Down Wire | N/A | `$97, $98` | `$a9, $a6` |
| `6` | Left-Up Wire | N/A | `$99, $9a` | `$ab, $a2` |
| `7` | Right-Up Wire | N/A | `$9b, $96` | `$ac, $a4` |
| `8` | Right-Down Wire | N/A | `$9c, $90` | `$a5, $aa` |
| `15–18` | Terminal R / D / L / U | **Offline** | `$b3–$b8` | `$c5–$ca` |
| `19–22` | Terminal R / D / L / U | **Connecting** | `$b9–$be` | `$c5–$ca` |
| `23–26` | Terminal R / D / L / U | **Online (Glowing)**| `$d1–$d8` | `$e1–$e8` |

---

## Citations
[1] [Source Code: game.asm](../../sources/Source/game.asm)

