---
type: Assembly Module
title: Welldone
description: Logic for the final win screen, including animated text and background effects.
resource: sources/Source/welldone.asm
tags: [ui, completion, animation]
timestamp: 2026-06-29T12:40:00Z
---

# Implementation
The `wellDone` module handles the end-game sequence when the player completes all 50 levels. It is characterized by high-effort visual effects and a dedicated NMI handler.

## [Rendering](../system/rendering.md) Pipeline
1. **Static Background**: Loads the `wellDoneTable` (via RLE) into the nametables.
2. **Text Animation**: 
   - Uses `wellDoneText` as a source.
   - Implements a gradual "typing" effect where characters appear one by one.
   - Includes a "fade" effect for the text using the `wellDoneFade` table and `wellDoneTextColor` routine.
3. **Dynamic Background**: The `nmiDone` handler implements a unique background animation by shifting the PPU scroll and changing the palette/attribute of columns based on `wellDoneBG` data.

## Execution Flow
- **Initialization**: Sets up the background, starts the `BGM_DONE` music, and switches the NMI handler to `nmiDone`.
- **NMI Loop (`nmiDone`)**:
    - **Text Display**: Manages the timing and printing of the completion text.
    - **Column Animation**: Calculates screen-splitting and color shifts to create a shimmering background effect.
    - **PPU Sync**: Uses `bit PPU_STATUS` to synchronize visual changes with the screen's vertical blank and sprite-0 hit.

# Citations
[1] [Source Code: welldone.asm](../../sources/Source/welldone.asm)
[2] [Source Code: game.asm](../../sources/Source/game.asm)
