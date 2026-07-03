---
type: Assembly Module
title: Level Definitions (levels)
description: Data definitions for the 50 game levels, including map layouts, timing, and terminal locations.
resource: sources/Source/levels.asm
tags: [logic, data, levels]
timestamp: 2026-06-29T12:10:00Z
---

# Level Structure

The `levels.asm` file contains the data for all 50 levels. The levels are indexed in the `levList` table, which is a table of pointers (`.dw`) to the start of each level's data block (`.level1` through `.level50`). This allows the game to jump directly to the required data based on the `GAME_LEVEL` variable.

## Level Data Layout

Each level is defined by a block of data with the following structure:

1. **Map Data**: 18 rows of 3 bytes each (54 bytes total).
   - This data is used by `unpackLevel` in `game.asm` to populate `GAME_MAP`.
   - The data is processed in chunks, often with 3 bytes per tile entry.
   - It includes logic to randomize the rotation of elements during unpacking.
2. **Start Position**: A word (`.dw`) specifying the starting position of the cursor in the level.
3. **Random Rotation Time**: A word (`.dw`) specifying the timing/count for random rotations.
4. **Time Limit**: A byte (`.db`) defining the time allowed to complete the level (some versions store this as two words for precision).
5. **Unknown/Reserved**: A trailing byte (usually `$66` or `$67`).

## Level Generation Process

When a level is loaded (`unpackLevel` in `game.asm`):

1. **Data Loading**: The map data is read from the address in `levList` and placed into `GAME_MAP`.
2. **Randomization**: The code iterates through the map and applies random rotations to tiles based on `mapCodes` (referenced in `game.asm`).
3. **Terminal Identification**: The routine scans `GAME_MAP` for tiles with a value $\ge 15$ and adds their offsets to `GAME_TERM_LIST`.
4. **Connectivity Ensuring**: The `unpackLevel` routine includes a "disconnect" phase. It ensures that terminals are not immediately connected by rotating them if necessary until a disconnected state is achieved.

# Citations
[1] [Source Code: levels.asm](/sources/Source/levels.asm)
[2] [Source Code: game.asm](/sources/Source/game.asm)
