---
type: Assembly Module
title: Welldone
description: Logic for the final win screen, including animated text and background effects.
resource: sources/Source/welldone.asm
tags: [ui, completion, animation]
timestamp: 2026-06-29T12:40:00Z
---

# Implementation

The `wellDone` screen (`welldone.asm`) executes after the player completes all 50 game levels. It employs advanced NES hardware raster techniques, dual-nametable horizontal scrolling, and a typewriter text animation.

---

## Mid-Frame Raster Split via Hardware Sprite 0 Hit

To keep the top header ("WELL DONE!") stationary while the bottom background credits scroll horizontally, `nmiDone` implements a hardware **Sprite 0 Hit** raster split:

1. **Sprite 0 Placement**: Sprite 0 is placed at Y-coordinate 63 (`Y=$3F`) with opaque pixel overlap against a background tile.
2. **VBlank Wait**: During `nmiDone`, execution waits for `PPU_STATUS` bit 6 (Sprite 0 Hit) to be set.
3. **Cycle Delay Loop**: Runs a 50-cycle delay loop (`ldx #50`, `dex`, `bne`).
4. **Mid-Frame Scroll Register Update**: Writes to `PPU_SCROLL` (`$2005`) mid-frame to set the horizontal scroll offset (`GAME_BG_OFF`) for the lower section of the screen without affecting the top header.

---

## Dual-Nametable Horizontal Scrolling Engine

The scrolling background credits utilize both NES PPU nametables (`$2000` and `$2400`):
- `GAME_BG_OFF`: Tracks horizontal sub-pixel/pixel scroll offset (0–255).
- `GAME_BG_PAGE`: Toggles base nametable selection (`$2000` vs `$2400`) when `GAME_BG_OFF` wraps around 256.

---

## Typewriter Control Codes (`wellDoneText`)

The typewriter engine parses script string streams in `wellDoneText` containing embedded control codes:

| Control Code | Hex Value | Behavior |
| :--- | :--- | :--- |
| `LINE_PAUSE` | `$FE` | Pauses typing for a line delay duration before advancing to the next row. |
| `MSG_PAUSE`  | `$FF` | Pauses typing for a long message delay before starting a new paragraph. |
| `MSG_END`    | `$00` | Loop terminator; resets typewriter script offset to `$0000` for infinite replay. |

---

## Citations
[1] [Source Code: welldone.asm](../../sources/Source/welldone.asm)
[2] [Source Code: game.asm](../../sources/Source/game.asm)

