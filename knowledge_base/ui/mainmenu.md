---
type: Assembly Module
title: Main Menu System
description: The primary user interface for game start, passcode entry, and audio options.
resource: sources/Source/mainmenu.asm
tags: [ui, menu, interaction]
timestamp: 2026-06-29T12:20:00Z
---

# Implementation
The main menu is a state-driven interface that manages the initial game entry and configuration.

## Menu Structure
The menu consists of 4 primary options (`MENU_CUR` 0-3):
0. **Start Game**: Resets `GAME_LEVEL` to 0 and triggers `mainMenuStart`.
1. **Enter Code**: Transitions to the `mainMenuEnterCode` sub-state for passcode input.
2. **Sound Effects (SFX)**: Toggles `GAME_SFX` on/off.
3. **Background Music (BGM)**: Toggles `GAME_BGM` on/off.

## Passcode System
The menu provides a specialized interface for entering 4-digit codes to unlock levels.
- **Input**: Users navigate a 4-digit number using the D-pad.
- **Verification**: The entered code is compared against the `passwords` table.
- **Validation Logic**: The code is split into 4-bit nibbles and compared against the `passwords` array. If a match is found, `GAME_LEVEL` is updated to the corresponding level index.
- **Special Codes**: There is a hidden "SFX Test" mode triggered by specific codes (e.g., code starting with 6, 8).

## Rendering & Animation
- **Background**: Uses `titleNameTable` loaded via `unrle`.
- **Cursor**: A simple cursor is rendered using `mainMenuShowCur` and `mainMenuShowCurAttr`.
- **Animation**: `mainMenuAnim` creates visual dynamism by toggling the `PPU_CTRL` mirror/scroll settings or reacting to the Noise channel of the audio engine.

# Citations
[1] [Source Code: mainmenu.asm](/sources/Source/mainmenu.asm)
[2] [Source Code: game.asm](/sources/Source/game.asm)
