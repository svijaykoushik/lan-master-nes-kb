---
type: Assembly Module
title: Level Generation & Unpacking
description: Logic for expanding level data from ROM into RAM, including randomization and terminal initialization.
resource: sources/Source/game.asm, sources/Source/levels.asm
tags: [logic, generation, randomization]
timestamp: 2026-06-29T13:00:00Z
---

# Level Generation Process

The process of transforming compressed level data from `levels.asm` into the playable `GAME_MAP` occurs in two primary stages: **Unpacking** and **Visualization**.

## 1. Unpacking (`unpackLevel`)

The `unpackLevel` routine is responsible for populating the 16x16 `GAME_MAP` buffer and initializing level-specific parameters.

### Data Expansion
The routine reads data from the address pointed to by `levList`. The map is processed in blocks, where each tile is expanded and placed into `GAME_MAP`.

### Tile Randomization
To ensure variety, tiles are subject to random rotation during the unpacking phase:
1. A random number (0-3) is generated via `jsr rand`.
2. This value is used to rotate the tile's orientation using the `rotateLeft` table.
3. This process ensures that the starting configuration of the network differs across play sessions.

### Terminal Identification
As the map is unpacked, the engine scans for "terminal" tiles (those with values $\ge 15$):
- The offset of every terminal found is stored in the `GAME_TERM_LIST`.
- The total count is stored in `GAME_TERM_CNT`.
- The first terminal's position is saved in `GAME_TERM_FP` to serve as the seed for the connectivity trace (`traceMap`).

### Connectivity Enforcement (The "Disconnect" Phase)
To prevent levels from being solved instantly, the engine performs a pass to ensure terminals are not pre-connected:
- It iterates through the `GAME_TERM_LIST`.
- For each terminal, it checks if it is currently connected to another terminal.
- If a connection is found, it rotates the terminal tile (up to 3 times) until the connection is broken.

## 2. Visualization (`showLevel`)

Once the `GAME_MAP` is finalized in RAM, `showLevel` handles the "unfolding" animation where tiles appear on the NES screen.

### The "Splay" Effect
Instead of a static load, the game uses a buffer `GAME_MAP_BUF` to perform a flood-fill-like animation:
1. **Seed**: It starts with the tile at `GAME_START_POS`.
2. **Expansion**: It iteratively marks neighboring tiles (Left, Right, Up, Down) as "next to visit".
3. **Rendering**: Tiles are rendered to the PPU in waves, alternating between storing coordinates and updating the screen.
4. **Iteration**: This continues until all reachable tiles in the map have been drawn.

# Citations
[1] [Source Code: game.asm](/sources/Source/game.asm)
[2] [Source Code: levels.asm](/sources/Source/levels.asm)
