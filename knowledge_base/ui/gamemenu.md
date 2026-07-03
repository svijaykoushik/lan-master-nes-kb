---
type: Assembly Module
title: In-Game Pause Menu
description: A contextual menu allowing players to resume the game, restart the level, or exit.
resource: sources/Source/gamemenu.asm
tags: [ui, menu, interaction]
timestamp: 2026-06-29T12:30:00Z
---

# Implementation
The `gameMenu` is a modal interface triggered during gameplay (via the Start button). It overlays the current game state and provides options for session management.

## Menu Mechanics
- **State Preservation**: Before displaying the menu, the current PPU screen content is read into `GAME_MENU_BUF`. This allows the menu to "hide" the game world and restore it perfectly when the menu is closed.
- **Visuals**:
    - Renders a custom table (`gameMenuTable`) and applies attributes via `gameMenuAttrTable`.
    - Displays the current level's pass-code using `showPassCode`.
- **Navigation**: Standard D-pad movement between 3 primary options.

## Menu Options
1. **Resume**: Closes the menu and returns the player to the `gameLoopInit` state.
2. **Restart**: Closes the menu and triggers `restartLevel` to reset the current puzzle.
3. **Exit**: Calls `exitGame`, which fades the screen out and returns the user to the main menu.

## Flow Logic
- **Entry**: `gameMenu` $\rightarrow$ Capture Screen $\rightarrow$ Render UI $\rightarrow$ Loop.
- **Exit**: `gameMenuDone` $\rightarrow$ Restore Screen from `GAME_MENU_BUF` $\rightarrow$ Branch to Resume/Restart/Exit.

# Citations
[1] [Source Code: gamemenu.asm](/sources/Source/gamemenu.asm)
[2] [Source Code: game.asm](/sources/Source/game.asm)
