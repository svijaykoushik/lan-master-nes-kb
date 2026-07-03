---
type: Software Tool
title: Level Editor (lanme)
description: Analysis of the C++ based level editor used to create and export levels for Lan Master.
resource: sources/Source/lanme/src/Unit1.cpp
tags: [tooling, level-editor, cpp, export]
timestamp: 2026-06-29T14:00:00Z
---

# Level Editor Overview

The `lanme` tool is a Windows VCL application used by the developer to design the 50 levels of Lan Master. It allows for visual map editing, connectivity testing, and exporting the data into both binary (`levels.bin`) and assembly (`levels.asm`) formats.

## Level Design Workflow

1. **Map Editing**: The editor manages a 12x12 grid. The user can place tiles from a palette and rotate them.
2. **Connectivity Testing**: The `CheckMap()` function implements a C++ version of the BFS connectivity algorithm. This allows the designer to verify that a level is solvable before exporting.
3. **Exporting**: When the editor is closed, it generates the necessary files for the game build.

## Assembly Export Logic (`FormDestroy`)

The tool converts the visual grid into the highly compressed format found in `levels.asm`.

### 1. Tile Compression
Instead of storing each tile as a full byte, the editor uses a `tilePaletteReverse` table to map tiles to 3-bit identifiers. 
- 8 tiles are packed into 3 bytes ( $8 \times 3 = 24$ bits).
- This is why the `levels.asm` file contains sequences of three `.db` bytes for every 8 tiles.

### 2. Parameter Calculation
The editor automatically calculates several level parameters:
- **Time Limit**: The time is calculated as $\text{ceil}(100.0 \times 256.0 / \text{tcnt})$, where `tcnt` is the number of terminal tiles. This ensures that levels with more terminals have proportionally different time limits.
- **Random Rotation Offset**: A value based on the level index is calculated to vary the randomness of the initial state.
- **Start Position**: The tool scans the map from the center outwards in concentric squares to find the first non-empty tile, which is then set as the `GAME_START_POS`.

## Connectivity Logic (C++ vs Assembly)

The `CheckMap` function in `Unit1.cpp` is the functional equivalent of the `traceMap` routine in `tracemap.asm`. Both use:
- A `pins` table to define directional connectivity.
- Two alternating lists (BFS) to traverse the network.
- A `checked` map to track visited tiles.

# Citations
[1] [Source Code: Unit1.cpp](/sources/Source/lanme/src/Unit1.cpp)
