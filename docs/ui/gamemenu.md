---
type: Assembly Module
title: Gamemenu
description: A contextual menu allowing players to resume the game, restart the level, or exit.
resource: sources/Source/gamemenu.asm
tags: [ui, menu, interaction]
timestamp: 2026-06-29T12:30:00Z
---

# Implementation

The `gameMenu` module (`gamemenu.asm`) manages the in-game pause overlay triggered by pressing `Start` during puzzle gameplay.

---

## 140-Byte VRAM Snapshot & Restoration Algorithm

To render a clean modal popup window over the active puzzle grid without corrupting tile graphics or requiring a full screen redraw:

1. **Snapshot on Pause (`gameMenuSave`)**:
   - Reads 140 bytes directly from PPU VRAM starting at Nametable address `$2169` (7 rows $\times$ 20 columns overlay window).
   - Backups these 140 bytes into RAM buffer `GAME_MENU_BUF` (located at RAM address `$0400`).
2. **Modal Overlay Render**:
   - Overwrites VRAM `$2169` with the pause menu box graphics (`gameMenuTable`) and level passcode string (`showPassCode`).
3. **Restoration on Resume (`gameMenuRestore`)**:
   - Reads 140 bytes back from `GAME_MENU_BUF` ($0400) and writes them back into VRAM `$2169`.
   - Restores exact pre-pause game board visuals instantly without loading or recalculating tile layout.

---

## Dynamic Attribute Table Highlighting

The pause selection cursor highlights options by dynamically altering PPU Attribute Table bytes:
- Targets PPU Attribute addresses `$23DA` and `$23E2`.
- Toggles attribute palette bits between standard background palette and bright menu highlight palette.

---

## Citations
[1] [Source Code: gamemenu.asm](../../sources/Source/gamemenu.asm)
[2] [Source Code: game.asm](../../sources/Source/game.asm)

