---
type: Reference
title: Audio Catalog
description: Mapping of sound effect indices and BGM modules to their game functions.
resource: sources/Source/sfx.asm, sources/Source/bgm_title.asm, sources/Source/bgm_game.asm, sources/Source/bgm_done.asm, sources/Source/bgm_timeout.asm
tags: [audio, sfx, bgm, catalog]
timestamp: 2026-07-03T10:45:00Z
---

# [Audio Catalog](audio_catalog.md)

This document provides a mapping between the internal audio indices used by the game logic and the specific audio assets defined in the source code.

## Sound Effects (SFX)

The game uses a table of sound effects defined in `sfx.asm`. These are triggered via the `sfxPlay` routine.

| Index | Label | Game Event | Description |
| :--- | :--- | :--- | :--- |
| 0 | `.sfx0` | `SFX_CURSOR` | Cursor movement/UI interaction. |
| 1 | `.sfx1` | `SFX_SELECT` | Selecting an option in a menu. |
| 2 | `.sfx2` | `SFX_START` | Starting the game or a level. |
| 3 | `.sfx3` | `SFX_TEXT` | Text scrolling/typewriter effect. |
| 4 | `.sfx4` | `SFX_ERROR` | Invalid action or error state. |
| 5 | `.sfx5` | `SFX_ROTATE1` | Manual tile rotation (A/B/Select). |
| 6 | `.sfx6` | `SFX_ROTATE2` | Manual tile rotation (A/B/Select). |
| 7 | `.sfx7` | `SFX_ROTATE3` | Manual tile rotation (A/B/Select). |
| 8 | `.sfx8` | `SFX_ROTATE4` | Manual tile rotation (A/B/Select). |
| 9 | `.sfx9` | `SFX_LEVEL` | Level completion/transition. |
| 10 | `.sfx10` | `SFX_TIME` | Timer warning. |
| 11 | `.sfx11` | `SFX_TIMEOUT` | Time expiration. |

## Background Music (BGM)

BGM is managed as modules, each consisting of channel data, envelopes, and instruments.

| Index | Module Label | Game State | Description |
| :--- | :--- | :--- | :--- |
| 0 | `BGM_NONE` | N/A | Silence / No music playing. |
| 1 | `bgm_title_module` | `BGM_MENU` | Main Menu theme. |
| 2 | `bgm_game_module` | `BGM_GAME` | Primary gameplay theme. |
| 3 | `bgm_done_module` | `BGM_DONE` | Victory screen theme. |
| 4 | `bgm_timeout_module` | `BGM_TIMEOUT` | Timeout/Failure theme. |

# Citations
[1] [Source Code: sfx.asm](../../sources/Source/sfx.asm)
[2] [Source Code: game.asm](../../sources/Source/game.asm)
[3] [Source Code: bgm_title.asm](../../sources/Source/bgm_title.asm)
[4] [Source Code: bgm_game.asm](../../sources/Source/bgm_game.asm)
[5] [Source Code: bgm_done.asm](../../sources/Source/bgm_done.asm)
[6] [Source Code: bgm_timeout.asm](../../sources/Source/bgm_timeout.asm)
