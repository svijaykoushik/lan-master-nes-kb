---
type: Assembly Module
title: Rle
description: Analysis of the RLE decompression logic used for background graphics.
resource: sources/Source/rle.asm
tags: [assets, graphics, compression]
timestamp: 2026-06-29T12:40:00Z
---

# Implementation
# RLE Decompression

Lan Master uses a custom Run-Length Encoding (RLE) scheme to compress large graphical assets (like `title.rle`, `gamebg.rle`, and `welldone.rle`) and decompress them directly into the PPU VRAM during screen transitions.

## The `unrle` Routine

The `unrle` routine performs the decompression. It reads data from a source address (passed in `X` and `Y` registers) and writes the resulting tiles to `PPU_DATA`.

### Algorithm

1. **Byte Fetching**: The `rle_byte` helper routine fetches a single byte from the source address and increments the source pointer.
2. **Tag Identification**: The first byte is read as a `tag` (`RLE_TAG`).
3. **Literal Copy**: 
   - If a fetched byte does not match the current tag, it is treated as a literal and written directly to `PPU_DATA`.
   - This literal byte is then stored as the new `RLE_BYTE` for potential subsequent runs.
4. **Run Expansion**:
   - When a byte matches the current tag, the next byte is read as a count.
   - The `RLE_BYTE` (the last literal byte encountered) is then written to `PPU_DATA` for the number of times specified by the count.

## Graphics Integration

The decompression is used in several key areas:
- **Main Menu**: `mainmenu.asm` calls `unrle` to load the title screen background.
- **Gameplay**: `game.asm` calls `unrle` during `gamePlayInit` to load the game background.
- **Win Screen**: `welldone.asm` calls `unrle` to load the "Well Done" screen assets.

# Citations
[1] [Source Code: rle.asm](../../sources/Source/rle.asm)
[2] [Source Code: game.asm](../../sources/Source/game.asm)
