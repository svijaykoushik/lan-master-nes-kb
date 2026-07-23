---
type: Assembly Module
title: Dual-Channel SFX Priority & Allocation Scheme
description: Sound channel assignment and priority management logic.
resource: sources/Source/game.asm
tags:
  - audio
  - sfx
  - famitone
timestamp: 2026-07-24T00:20:00Z
---

# Dual-Channel SFX Priority & Audio Allocation Scheme

## System Overview

*Lan Master* utilizes a dual-channel sound effect allocation strategy implemented inside `sfxPlay` (`game.asm`) operating on top of the FamiTone sound engine.

---

## Channel Allocation Architecture

FamiTone allocates two dedicated sound effect hardware channels (`FT_SFX_CH0` and `FT_SFX_CH1`):

```text
       +--------------------------------------------+
       |             sfxPlay(Sound_ID)              |
       +---------------------+----------------------+
                             |
            +----------------+----------------+
            |                                 |
 [Sound_ID == SFX_TIME (10)]     [Sound_ID != SFX_TIME]
            |                                 |
            v                                 v
     Target Channel 1                  Target Channel 0
     (FT_SFX_CH1)                      (FT_SFX_CH0)
            |                                 |
            +----------------+----------------+
                             |
                             v
                Dispatch to FamiTone Engine
```

---

## Technical Rationale

1. **`FT_SFX_CH0` (General Gameplay & UI Sound Effects)**:
   - Reserved for player interaction SFX (cursor movement, tile rotations, menu selection, stage start, stage win, and error alerts).
2. **`FT_SFX_CH1` (Dedicated Time Countdown Channel)**:
   - Exclusively reserved for `SFX_TIME` (Sound ID 10), the urgent low-time countdown tick sound effect.

### Benefits
By isolating `SFX_TIME` to `FT_SFX_CH1`, low-time tick warnings play continuously on a separate sound channel without being cut off or muted when the player rapidly moves the cursor or rotates tiles on `FT_SFX_CH0`.

---

## Citations
[1] [Source Code: game.asm](../../sources/Source/game.asm)
[2] [Source Code: sfx.asm](../../sources/Source/sfx.asm)
