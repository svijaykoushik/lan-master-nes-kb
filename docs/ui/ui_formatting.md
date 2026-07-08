---
type: Assembly Module
title: UI Formatting
description: Utility routines for rendering numbers, tables, and passcodes to the PPU.
resource: sources/Source/game.asm
tags: [ui, rendering, ppu, utility]
timestamp: 2026-07-03T11:15:00Z
---

# Implementation
# [UI Formatting](ui_formatting.md) Subsystem

Lan Master utilizes a set of specialized primitives to convert internal game state into visual representations on the NES screen. These routines handle the translation of binary values into character patterns and manage the rendering of tabular data.

## Numerical Display (`putNum` series)

The game implements basic decimal-to-character conversion for displaying levels, online counts, and time.

### `putNum3` (3-Digit Display)
Used for the "Online" count and the "Time" remaining.
- **Logic**: 
    - It subtracts 100 iteratively from the accumulator to determine the "hundreds" digit.
    - The remainder is then processed to find "tens" and "units".
    - The resulting values are converted to ASCII/Character indices by adding a base offset (`$56`) and written to `PPU_DATA`.

### `putNum2` (2-Digit Display)
Used for the current level number.
- **Logic**: Similar to `putNum3`, but only processes two digits (subtracting 10 iteratively).
- **Output**: Renders the tens and units digits to `PPU_DATA`.

## Tabular Data [Rendering](../system/rendering.md)

The game uses a flexible table system to display lists of information, such as the "Level Clear" summary or the "Time Out" screen.

### `showTable`
This routine renders a block of text/data from a source table in ROM to the screen.
- **Execution Flow**:
    1. **Setup**: Takes width, height, and a source address.
    2. **Buffering**: Reads data from the source and stores it in `GAME_MENU_BUF` to allow for synchronized screen updates.
    3. **[Rendering](../system/rendering.md)**: Writes the buffer to `PPU_DATA` while handling VBlank synchronization via `waitNMI50`.
    4. **Special Case**: If `GAME_TABLE_CODE` is set, it may call `showPassCode` as part of the table render.

### `clearTable`
The inverse of `showTable`. It restores the screen area by writing the original content stored in `GAME_MENU_BUF` back to the PPU, effectively "hiding" the table.

## Passcode Display (`showPassCode`)

A specialized routine that renders the 4-digit passcode for the current level.
- **Logic**:
    - Retrieves the password from the `passwords` table.
    - Splits each password byte into two 4-bit nibbles.
    - Converts each nibble to a character index (adding `$57`) and writes it to `PPU_DATA`.

# Citations
[1] [Source Code: game.asm](../../sources/Source/game.asm)
