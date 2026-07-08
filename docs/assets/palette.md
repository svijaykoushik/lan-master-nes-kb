---
type: Assembly Module
title: Palette
description: Logic for managing NES color palettes and implementing fade effects.
resource: sources/Source/palette.asm
tags: [assets, graphics, hardware]
timestamp: 2026-06-29T12:50:00Z
---

# Implementation
# [Palette](palette.md) Management

The palette system handles the colors used by the PPU, providing routines to reset palettes and create smooth transitions via fade-in and fade-out effects.

## [Palette](palette.md) Reset (`palReset`)
The `palReset` routine clears the current PPU palette by writing the default color `$0f` to the palette registers.

## Fade Effects

The game uses a technique to fade colors by interpolating between a base palette and a "brightened" version of that palette.

### 1. Fade-In (`palFadeIn`)
- **Mechanism**: Gradually transitions the colors from dark/default to the target palette.
- **Implementation**:
    - Uses `palBrightTable`, which contains pre-calculated brightness levels for NES colors.
    - Iteratively updates the PPU palette registers over 16 frames (`PAL_CNT`).
    - It reads the target palette (`PAL_LOW/HIGH`) and uses the value as an index into `palBrightTable` to find the corresponding brightened color.

### 2. Fade-Out (`palFadeOut`)
- **Mechanism**: Gradually transitions the colors from the current palette back to a dark state.
- **Implementation**: Similar to `palFadeIn`, but traverses the `palBrightTable` in the opposite direction (decreasing brightness) before finally calling `palReset`.

## [Palette](palette.md) Definitions

The file defines three primary palettes:
- `palTitle`: Used for the main menu screen.
- `palGame`: Used during active gameplay.
- `palDone`: Used for the victory screen.

# Citations
[1] [Source Code: palette.asm](../../sources/Source/palette.asm)
