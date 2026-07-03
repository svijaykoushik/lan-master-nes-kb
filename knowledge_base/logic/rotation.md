---
type: Game Mechanic
title: Tile Rotation Mechanic
description: Logic for rotating network elements to establish connectivity.
resource: sources/Source/game.asm
tags: [logic, mechanics, interaction]
timestamp: 2026-06-29T13:30:00Z
---

# Rotation Mechanics

The core gameplay of Lan Master involves rotating tiles to connect terminals.

## 1. Manual Rotation

The player can rotate the tile currently under the cursor using the **A**, **B**, or **Select** buttons.

### Rotation Logic
- **Input**: The buttons map to different rotation amounts:
    - `B` $\rightarrow$ Rotation 3
    - `A` $\rightarrow$ Rotation 1
    - `Select` $\rightarrow$ Rotation 2
- **Execution**: The `setRotate` routine calculates the tile's coordinates in `GAME_MAP`. It then applies the rotation by looking up the current tile value in the `rotateLeft` table and replacing it with the rotated version.
- **Visual Update**: After the map value is changed, `updateTile` is called to refresh the VRAM.
- **Feedback**: A sound effect is played (`SFX_ROTATE1` through `SFX_ROTATE4`) based on the rotation amount.

## 2. Automatic Random Rotation

The game introduces a "network degradation" mechanic where tiles rotate randomly over time.

### Timing and Trigger
- The system tracks `GAME_RROT_TIME` and `GAME_RROT_CNT`.
- When the counter reaches zero, `setRandomRotate` is triggered.

### Randomization Process
1. **Target Selection**: A random tile is selected using `jsr rand`.
2. **Validity Check**: The routine ensures the selected tile is a rotatable element (not empty).
3. **Rotation**: A random rotation amount (1 or 2) is selected and applied.
4. **Feedback**: The `SFX_ROTATE3` or `SFX_ROTATE4` sound effect is played.

# Citations
[1] [Source Code: game.asm](/sources/Source/game.asm)
