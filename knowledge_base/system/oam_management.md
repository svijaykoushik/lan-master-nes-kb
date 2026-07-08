---
type: Assembly Module
title: Sprite & OAM Management
description: Logic for managing the NES Object Attribute Memory (OAM) and rendering the game cursor.
resource: sources/Source/game.asm
tags: [system, rendering, oam, sprites]
timestamp: 2026-07-03T11:30:00Z
---

# OAM Management

Lan Master uses the NES's sprite system to render the game cursor. The game maintains a local copy of the sprite attributes in RAM before transferring them to the PPU's OAM (Object Attribute Memory).

## OAM Buffer (`OAM_PAGE`)

To avoid the timing constraints of writing directly to PPU registers, the game uses a dedicated RAM buffer:
- **Location**: `$0700` (`OAM_PAGE`).
- **Structure**: Each sprite requires 4 bytes:
    1. Y-coordinate
    2. Sprite Tile Index
    3. Attribute (Color/Priority)
    4. X-coordinate

## Sprite Operations

### `clearOAM`
This routine initializes the OAM buffer to a "blank" state. It fills the buffer with the value `$ef`, which effectively places sprites outside the visible screen area or marks them as inactive.

### `updateOAM`
This routine performs a Direct Memory Access (DMA) transfer to move the local `OAM_PAGE` buffer into the PPU's internal OAM.
- **Mechanism**: 
    - Sets `PPU_OAM_ADDR` to 0.
    - Writes the high byte of `OAM_PAGE` to `PPU_OAM_DMA` (`$4014`).
    - This triggers the hardware to copy 256 bytes from RAM to the PPU in a single frame.

## The Game Cursor

The cursor is the only dynamic sprite used during gameplay. It is rendered as a set of four sprites to create a visually distinct marker.

### `showCursor`
This routine updates the `OAM_PAGE` buffer with the current cursor coordinates (`GAME_CUR_SX`, `GAME_CUR_SY`).
- **Symmetry**: It writes 4 sprite entries to the buffer, offsetting them to form a cohesive cursor graphic.
- **Coordinate Mapping**: It translates the game's internal coordinate system to the PPU's sprite coordinates.

# Citations
[1] [Source Code: game.asm](/sources/Source/game.asm)
