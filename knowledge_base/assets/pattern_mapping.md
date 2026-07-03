---
type: Reference
title: Pattern Mapping (tilesTable)
description: Mapping of internal logical tile IDs to PPU character pattern indices in patterns.chr.
resource: sources/Source/game.asm
tags: [assets, graphics, ppu, mapping]
timestamp: 2026-07-03T10:30:00Z
---

# Pattern Mapping Overview

Lan Master uses a layer of indirection between the logical map (`GAME_MAP`) and the physical PPU character patterns stored in `patterns.chr`. This is managed via the `tilesTable` in `game.asm`.

## The Mapping Logic

The game employs "double-height" tiles. Each logical tile in the game world corresponds to a 16x8 pixel area, which requires two 8x8 PPU character tiles for the top half and two for the bottom half.

### Translation Process
When the `updateTile` routine is called:
1. **Logical ID**: The value from `GAME_MAP` (the logical tile ID) is retrieved.
2. **Table Offset**: The ID is multiplied by 4 (via two `asl` instructions) to find the offset into the `tilesTable`.
3. **PPU Indices**: Four bytes are read from the `tilesTable` to determine the physical pattern indices in `patterns.chr`:
   - **Byte 0**: Top-left character index.
   - **Byte 1**: Top-right character index.
   - **Byte 2**: Bottom-left character index.
   - **Byte 3**: Bottom-right character index.

## Logical to Physical Map

Based on the `tilesTable` definitions in `game.asm`, the following mapping is established:

| Logical ID | Description | Top Indices | Bottom Indices | PPU Pattern (Hex) |
| :--- | :--- | :--- | :--- | :--- |
| 0 | Empty | `$8d, $8e` | `$a1, $a2` | `8D 8E A1 A2` |
| 1 | Horizontal Wire | `$8f, $90` | `$a3, $a4` | `8F 90 A3 A4` |
| 2 | Vertical Wire | `$91, $92` | `$a5, $a6` | `91 92 A5 A6` |
| 3 | Crossed Separate | `$93, $94` | `$a7, $a8` | `93 94 A7 A8` |
| 4 | Crossed Connection | `$95, $96` | `$a9, $aa` | `95 96 A9 AA` |
| 5 | Left-Down | `$97, $98` | `$a9, $a6` | `97 98 A9 A6` |
| 6 | Left-Up | `$99, $9a` | `$ab, $a2` | `99 9A AB A2` |
| 7 | Right-Up | `$9b, $96` | `$ac, $a4` | `9B 96 AC A4` |
| 8 | Right-Down | `$9c, $90` | `$a5, $aa` | `9C 90 A5 AA` |
| 15 | Terminal Right (Off) | `$b3, $b5` | `$c5, $c6` | `B3 B5 C5 C6` |
| 16 | Terminal Down (Off) | `$b3, $b5` | `$c7, $c8` | `B3 B5 C7 C8` |
| 17 | Terminal Left (Off) | `$b6, $b5` | `$c9, $ca` | `B6 B5 C9 CA` |
| 18 | Terminal Up (Off) | `$b7, $b8` | `$c5, $ca` | `B7 B8 C5 CA` |
| 19 | Terminal Right (On) | `$b9, $ba` | `$c5, $c6` | `B9 BA C5 C6` |
| 20 | Terminal Down (On) | `$b9, $bb` | `$c7, $c8` | `B9 BB C7 C8` |
| 21 | Terminal Left (On) | `$bc, $bb` | `$c9, $ca` | `BC BB C9 CA` |
| 22 | Terminal Up (On) | `$bd, $be` | `$c5, $ca` | `BD BE C5 CA` |

*Note: IDs 9-14 follow a similar pattern for expanded wiring variants.*

# Citations
[1] [Source Code: game.asm](/sources/Source/game.asm)
