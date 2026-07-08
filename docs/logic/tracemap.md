---
type: Assembly Module
title: Connectivity Engine
description: Logic for verifying network connectivity and win conditions.
resource: sources/Source/tracemap.asm
tags: [logic, graph-traversal, win-condition]
timestamp: 2026-06-29T11:30:00Z
---

# Implementation
The `traceMap` routine implements a connectivity check to determine if all terminal computers on a level are linked. It uses a breadth-first search (BFS) approach with two alternating lists (`T_CURLIST` and `T_NEWLIST`) to track visited tiles.

## Algorithm Flow
1. **Initialization**: Clears the `GAME_CHECK` map and initializes lists.
2. **Seed**: Starts the traversal from a terminal defined in `GAME_TERM_LIST`.
3. **Expansion**:
    - For each tile in the current list, it checks the `pinsTable` to see which directions are active.
    - It verifies if the neighbor in that direction has a matching pin (e.g., if the current tile has a `T_LEFT` pin, the neighbor to the left must have a `T_RIGHT` pin).
    - Valid neighbors are added to the `T_NEWLIST`.
4. **Verification**: If a terminal tile is reached, the `T_ONLINE_CNT` is incremented.
5. **Termination**: The loop continues until no new tiles can be reached. If `T_ONLINE_CNT` equals `GAME_TERM_CNT`, the level is considered cleared.

## Pin Logic (`pinsTable`)
The `pinsTable` defines the connectivity of each tile type. Pins are represented as bitmasks:
- `T_LEFT` (1), `T_RIGHT` (2), `T_UP` (4), `T_DOWN` (8).
- Some tiles have "secondary" pins (shifted by 4 bits), which may represent internal connectivity or special terminal properties.

# Citations
[1] [Source Code: tracemap.asm](../../sources/Source/tracemap.asm)
