---
type: Reference
title: Connectivity Rules
description: Formalization of the wiring rules used to determine connectivity between tiles.
resource: sources/Source/tracemap.asm
tags: [logic, reference, networking]
timestamp: 2026-06-29T13:45:00Z
---

# Connectivity Matrix

The `pinsTable` in `tracemap.asm` defines how each tile type connects to its neighbors. Connectivity is based on a bitmask of "pins" (available connection points).

## Pin Definitions

The following constants define the connection directions:
- `T_LEFT` (1) $\rightarrow$ `0000 0001`
- `T_RIGHT` (2) $\rightarrow$ `0000 0010`
- `T_UP` (4) $\rightarrow$ `0000 0100`
- `T_DOWN` (8) $\rightarrow$ `0000 1000`

## Connection Validation

A connection between two adjacent tiles is valid **if and only if** both tiles have matching opposing pins.

### Example: Horizontal Connection
For a connection between Tile A (Left) and Tile B (Right):
- **Tile A** must have the `T_RIGHT` pin set.
- **Tile B** must have the `T_LEFT` pin set.

### Secondary Pins (Shifted)
Some entries in `pinsTable` use shifted bits (`T_S_PIN << 4`). These are used by `traceMap` to handle special connectivity logic, such as internal terminal connections or multi-segment wires.

## Tile Pin Mapping

Based on the `pinsTable` data, here are common tile behaviors:

| Tile ID | Description | Pins | Logic |
| :--- | :--- | :--- | :--- |
| 0 | Empty | None | Blocked |
| 1 | Horizontal Wire | `T_LEFT \| T_RIGHT` | Connects Left $\leftrightarrow$ Right |
| 2 | Vertical Wire | `T_UP \| T_DOWN` | la Connects Up $\leftrightarrow$ Down |
| 3 | Crossed Separate | `L \| R \| (U \| D) << 4` | Left/Right connect; Up/Down connect separately |
| 4 | Crossed Connection | `L \| R \| U \| D` | All 4 directions connected |
| 5 | Left-Down | `T_LEFT \| T_DOWN` | Connects Left $\leftrightarrow$ Down |
| 6 | Left-Up | `T_LEFT \| T_UP` | Connects Left $\leftrightarrow$ Up |
| 7 | Right-Up | `T_RIGHT \| T_UP` | Connects Right $\leftrightarrow$ Up |
| 8 | Right-Down | `T_RIGHT \| T_DOWN` | Connects Right $\leftrightarrow$ Down |

# Citations
[1] [Source Code: tracemap.asm](../../sources/Source/tracemap.asm)
