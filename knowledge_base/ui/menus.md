---
type: Assembly Module
title: User Interface & Menus
description: Analysis of the main menu, in-game pause menu, and win screen.
resource: sources/Source/mainmenu.asm, sources/Source/gamemenu.asm, sources/Source/welldone.asm
tags: [ui, menus, graphics]
timestamp: 2026-06-29T12:20:00Z
---

# User Interface Overview

The game features three primary UI states: the Main Menu, the Game Menu (Pause), and the Well Done (Win) screen. All menus utilize the NES's nametables for text and attribute tables for color.

## 1. Main Menu ([mainmenu.asm](/knowledge_base/ui/mainmenu.md))
The main menu is the entry point of the game.

- **Features**:
    - **Navigation**: Uses `MENU_CUR` to track the selected option.
    - **Options**: "Start Game", "Enter Code", "SFX Toggle", "BGM Toggle".
    - **Password System**: Allows users to enter a 4-digit code. The code is verified against the `passwords` table in `mainmenu.asm`. If valid, `GAME_LEVEL` is set to the corresponding level.
    - **Visuals**: Includes a fade-in effect using `palFadeIn` and a blinking cursor.

## 2. Game Menu ([gamemenu.asm](/knowledge_base/ui/gamemenu.md))
The in-game pause menu, triggered by pressing the `START` button.

- **Functionality**:
    - **State Preservation**: When opened, it reads the current screen state into `GAME_MENU_BUF` to allow restoring the game screen upon closing.
    - **Options**: "Resume" (returns to `gameLoopInit`), "Restart" (calls `restartLevel`), and "Exit Game" (calls `exitGame`).
    - **Passcode Display**: Displays the passcode for the current level using `showPassCode`.

## 3. Well Done Screen ([welldone.asm](/knowledge_base/ui/welldone.md))
The screen displayed after completing all 50 levels.

- **Visuals**:
    - **Text Animation**: Displays a victory message (`wellDoneText`) with a typewriter-like animation and a fade-out effect.
    - **Background Animation**: Implements a scrolling/shifting background using `wellDoneBG` data and the `nmiDone` handler.
    - **Timing**: Uses `GAME_CHANGE_CNT` to control the timing of text and background shifts.

# Citations
[1] [Source Code: mainmenu.asm](/sources/Source/mainmenu.asm)
[2] [Source Code: gamemenu.asm](/sources/Source/gamemenu.asm)
[3] [Source Code: welldone.asm](/sources/Source/welldone.asm)
