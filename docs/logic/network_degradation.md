---
type: Game Mechanic
title: Random Network Degradation Engine
description: Automatic tile misalignment mechanic active on higher difficulty levels.
resource: sources/Source/game.asm
tags:
  - logic
  - mechanics
  - difficulty
timestamp: 2026-07-24T00:20:00Z
---

# Random Network Degradation Engine

## System Overview

Beginning at Level 10, *Lan Master* introduces an active difficulty mechanic known as **Network Degradation**. Over time, populated wire segments on the game board randomly rotate out of alignment, requiring the player to re-establish connectivity before timers expire.

---

## Technical Implementation

### Activation Threshold & Degradation Timing

Network degradation timing is configured during level loading based on the stage number:

$$\text{Degradation Interval } (rt) = (110 - \text{Level}) \times 10 \text{ frames}$$

- For Levels 1–9, network degradation is disabled (`GAME_RROT_TIME` = 0).
- At Level 10, degradation triggers every 1,000 frames (~16.6 seconds).
- At Level 50, degradation triggers every 600 frames (10.0 seconds).

---

## Execution Logic (`randomRotateTile`)

1. **Timer Decrement**: On every frame in `nmiGame`, `GAME_RROT_CNT` is decremented.
2. **Trigger**: When `GAME_RROT_CNT` reaches 0, `randomRotateTile` is invoked.
3. **Random Selection**:
   - Uses the Galois LFSR (`rand`) to select a random tile offset in `GAME_MAP` ($16 \times 16$ grid).
   - Verifies that the selected tile is non-empty (Tile ID $\ne 0$). Empty tiles are ignored and bypassed.
4. **Tile Rotation**:
   - Rotates the tile by $90^\circ$ or $270^\circ$ clockwise.
   - Updates `GAME_MAP` RAM.
5. **Audio Dispatch**:
   - Plays automatic degradation rotation sound effects (`SFX_ROTATE3` / `SFX_ROTATE4`, sound IDs 7 and 8). These distinct sound effects alert the player that a background tile has shifted position.

---

## Citations
[1] [Source Code: game.asm](../../sources/Source/game.asm)
