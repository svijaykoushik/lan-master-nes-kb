---
type: Reference
title: Project Map
description: Mapping of the source codebase to functional game components.
tags:
  - project-structure
  - mapping
timestamp: 2026-07-24T00:08:00Z
---

# Source Code Map

## Core Logic & Systems
- [Main Game Loop](../sources/Source/game.asm) - Central game state and logic. See [Architecture](architecture.md), [Dynamic NMI Vectoring](system/nmi_vectoring.md), and [Network Degradation](logic/network_degradation.md).
- [Input Handling](../sources/Source/controller.asm) - Processing A, B, Select, and D-Pad inputs with hardware DPCM DMA filtering. See [Input System](system/controller.md).
- [Level Definitions](../sources/Source/levels.asm) - 60-byte binary stage layouts and fixed-point score multipliers. See [Level Definitions](logic/levels.md) and [Level Editor Architecture](system/level_editor_architecture.md).
- [Trace Mapping](../sources/Source/tracemap.asm) - Graph traversal logic for network connectivity verification. See [Connectivity Engine](logic/tracemap.md).

## User Interface & Menus
- [Main Menu](../sources/Source/mainmenu.asm) - Initial game entry, passcode entry, and secret diagnostic sound test. See [Main Menu](ui/mainmenu.md) and [Hidden Main Menu Diagnostics](logic/cheats_diagnostics.md).
- [Game Menu](../sources/Source/gamemenu.asm) - In-game pause and status menu with 140-byte VRAM snapshot buffer. See [In-Game Pause Menu](ui/gamemenu.md).
- [Win State](../sources/Source/welldone.asm) - Stage completion victory screen with Sprite 0 Hit raster split. See [Victory Screen](ui/welldone.md).
- [Menu Subsystem](ui/menus.md) - Architectural summary of menu states.

## Audio System
- [Sound Effects](../sources/Source/sfx.asm) - General SFX management. See [Audio Catalog](audio/audio_catalog.md) and [Dual-Channel SFX Priority](audio/sfx_priority.md).
- [Music Core](../sources/Source/famitone.asm) - FamiTone music engine implementation. See [FamiTone Engine](audio/famitone.md).
- BGM Tracks: [Title BGM](../sources/Source/bgm_title.asm), [Game BGM](../sources/Source/bgm_game.asm), [Done BGM](../sources/Source/bgm_done.asm), [Timeout BGM](../sources/Source/bgm_timeout.asm).

## Assets & Graphics
- [Color Palettes](../sources/Source/palette.asm) - NES hardware color palette definitions and fade logic. See [Palette Management](assets/palette.md).
- [Character Patterns](../sources/Source/patterns.chr) - Tile patterns for game graphics. See [Pattern Mapping](assets/pattern_mapping.md).
- Compressed Background Graphics: [Game BG](../sources/Source/gamebg.rle), [Title BG](../sources/Source/title.rle), [Well Done BG](../sources/Source/welldone.rle).
- [RLE Decompressor](../sources/Source/rle.asm) - Logic to expand RLE compressed assets. See [RLE Decompressor](assets/rle.md).

## Build Pipeline & Tools
- [Compilation Script](../sources/Source/compile.bat) - Batch script for assembling 6502 assembly code with NESASM. See [Build System](system/build_system.md).
- [Level Editor Tool](../sources/Source/lanme/src/Unit1.cpp) - Delphi/C++ level editor source code. See [Level Editor Architecture](system/level_editor_architecture.md).

# Citations
[1] [Source Directory Listing](../sources/Source)


