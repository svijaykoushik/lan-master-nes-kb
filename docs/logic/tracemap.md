---
type: Assembly Module
title: Connectivity Engine
description: Logic for verifying network connectivity and win conditions.
resource: sources/Source/tracemap.asm
tags: [logic, graph-traversal, win-condition]
timestamp: 2026-06-29T11:30:00Z
---

# Implementation

The `traceMap` routine implements a connectivity check to determine if all terminal computers on a level are linked. It uses a Breadth-First Search (BFS) graph traversal with two alternating work queues (`T_CURLIST` and `T_NEWLIST`) to track unvisited tiles.

---

## Algorithm Flow

1. **Initialization**: Clears the `GAME_CHECK` RAM array ($0400–$04FF) to zeroes and resets online terminal accumulators.
2. **Seed**: Enqueues the first terminal tile from `GAME_TERM_LIST` into `T_CURLIST`.
3. **Neighbor Expansion**:
   - Reads the active tile ID from `GAME_MAP` ($0300) and looks up its pin bitmask in `pinsTable`.
   - Checks matching opposing pins on adjacent tiles (e.g., `T_LEFT` must pair with adjacent `T_RIGHT`).
   - Valid unvisited neighbors are pushed to `T_NEWLIST` and marked in `GAME_CHECK`.
4. **Online Terminal Counter**: If a terminal tile (Tile IDs 15–26) is reached during traversal, `T_ONLINE_CNT` increments and `GAME_TERM_FP` is accumulated into `T_ONLINE`.
5. **Termination**: Swaps `T_CURLIST` and `T_NEWLIST`. Loop terminates when no new connected tiles are found. If `T_ONLINE_CNT` matches `GAME_TERM_CNT`, stage victory is triggered.

---

## Dual-Wire Crossing & Pin Bitmasks (`pinsTable`)

Pins are represented as 8-bit masks:
- Primary Wire Pins (Low Nibble `bits 0-3`): `T_LEFT` (1), `T_RIGHT` (2), `T_UP` (4), `T_DOWN` (8).
- Secondary Wire Pins (High Nibble `bits 4-7`): Shifted by 4 bits (`pins << 4`).

### Dual-Wire Crossing Tiles (Tile IDs 3, 13, 14)
Crossing tiles allow two independent non-connecting wires to pass through the same grid space (e.g., Horizontal wire crossing a Vertical wire).
- **Primary Path** uses low-nibble pins (e.g., `T_LEFT | T_RIGHT`).
- **Secondary Crossing Path** uses high-nibble pins (e.g., `(T_UP | T_DOWN) << 4`).

---

## Traversal Visited Bitmasks (`GAME_CHECK` at $0400)

The `GAME_CHECK` array tracks visited states per tile using a 2-bit flag:
- `Bit 0` (`$01`): Primary wire pathway has been visited.
- `Bit 1` (`$02`): Secondary crossing wire pathway has been visited.

This dual-bit scheme ensures that crossing tiles can be traversed independently along both wire pathways without false cycles or prematurely blocking the second pathway.

---

## Citations
[1] [Source Code: tracemap.asm](../../sources/Source/tracemap.asm)
[2] [Connectivity Specification: connectivity_rules.md](connectivity_rules.md)

