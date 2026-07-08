---
type: Reference
title: Project Map
description: Mapping of the source codebase to functional game components.
tags:
  - project-structure
  - mapping
timestamp: 2026-06-29T11:05:00Z
---

# Source Code Map

## Core Logic & Systems
- [Main Game Loop](../sources/Source/game.asm) - Central game state and logic.
- [Input Handling](../sources/Source/controller.asm) - Processing A, B, and Select buttons.
- [Level Definitions](../sources/Source/levels.asm) - Data and logic for the 50 game levels.
- [Trace Mapping](../sources/Source/tracemap.asm) - Logic for calculating network connectivity.

## [User Interface & Menus](ui/menus.md)
- [Main Menu](../sources/Source/mainmenu.asm) - Initial game entry and pass-code entry.
- [Game Menu](../sources/Source/gamemenu.asm) - In-game pause and status menu.
- [Win State](../sources/Source/welldone.asm) - Level completion screen.

## Audio System
- [Sound Effects](../sources/Source/sfx.asm) - General SFX management.
- [Music Core](../sources/Source/famitone.asm) - Music engine implementation.
- [BGM Tracks](../sources/Source/bgm_title.asm, /sources/Source/bgm_game.asm, /sources/Source/bgm_done.asm, /sources/Source/bgm_timeout.asm) - Specific music compositions.

## Assets & Graphics
- [Color [Palette](assets/palette.md)s](/sources/Source/palette.asm) - NES palette definitions.
- [Character Patterns](../sources/Source/patterns.chr) - Tile data for graphics.
- [Compressed Graphics](../sources/Source/gamebg.rle, /sources/Source/title.rle, /sources/Source/welldone.rle) - RLE compressed background assets.
- [RLE Decompressor](../sources/Source/rle.asm) - Logic to expand compressed assets.

## Build Pipeline
- [Compilation Script](../sources/Source/compile.bat) - Windows batch script for assembling the 6502 code. See [Build System](system/build_system.md).

# Citations
[1] [Source Directory Listing](../sources/Source)
