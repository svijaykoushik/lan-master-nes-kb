---
type: Assembly Module
title: Rendering
description: Logic for mapping internal game map tiles to NES PPU VRAM addresses and character patterns.
resource: sources/Source/game.asm
tags: [system, rendering, ppu]
timestamp: 2026-06-29T13:15:00Z
---

# Implementation
# PPU Mapping Logic

Lan Master maps its internal 16x16 `GAME_MAP` grid to the NES PPU nametables.

## 1. Address Calculation (`getTileAddr`)

The game converts 2D (X, Y) coordinates into a 1D offset for the `GAME_MAP` array.
- **Formula**: `offset = (Y * 16) + X + 17`
- The `+17` offset is used to avoid zero-page conflicts or alignment issues.

## 2. VRAM Address Calculation (`updateTile`)

The `updateTile` routine maps these coordinates to the actual PPU memory addresses.

### Nametable Mapping
The NES Nametable is 32x30 tiles. The game center-aligns its 12x12 gameplay area.
- **X Offset**: The calculation involves adding a base offset of `$84` to the X coordinate.
- **Y Offset**: The Y coordinate is shifted (multiplied by 32 or 64 depending on the PPU page) and added to the base.

### Tile Pattern Selection
The internal tile ID from `GAME_MAP` is used to index into the `tilesTable` (see [Pattern Mapping](../assets/pattern_mapping.md)). Each entry in `tilesTable` provides four bytes of data:
- **Byte 1**: The tile character index for the top-left half of the tile.
- **Byte 2**: The tile character index for the top-right half of the tile.
- **Byte 3**: The tile character index for the bottom-left half of the tile.
- **Byte 4**: The tile character index for the bottom-right half of the tile.

Because the NES uses 8x8 pixel tiles and the game uses 16x8 "double-height" tiles for wires, every logical tile update writes two consecutive entries to PPU VRAM.

## 3. Visual Enhancements

### Column Coloring
The game updates the color of a specific column in the UI area by writing to the PPU attribute table. The color is determined by `GAME_CUR_COL` and the `curColors` table.

### Terminal Highlighting
Terminals are visually distinct. When a terminal is "online" (verified by `traceMap`), the `updateTile` routine adds an offset (`GAME_TERM_ONGFX`) to the tile index to render a "powered-on" version of the terminal graphic.

# Citations
[1] [Source Code: game.asm](../../sources/Source/game.asm)
