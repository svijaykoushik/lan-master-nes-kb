---
type: Assembly Module
title: Timing & Synchronization
description: Low-level routines for synchronizing game logic and rendering with the NES NMI and VBlank.
resource: sources/Source/game.asm
tags: [system, timing, sync, hardware]
timestamp: 2026-07-03T11:00:00Z
---

# Timing & Synchronization

Lan Master relies on strict synchronization with the NES hardware to ensure smooth rendering and consistent game speed. This is achieved through a set of "wait" routines that synchronize execution with the Non-Maskable Interrupt (NMI).

## VBlank Synchronization (`waitVBlank`)

The `waitVBlank` routine is the simplest form of synchronization. It polls the `PPU_STATUS` register until the VBlank flag (bit 7) is set.

- **Mechanism**:
    - Reads `PPU_STATUS`.
    - Checks the high bit (`bit PPU_STATUS`).
    - Loops until the bit is clear (indicating the start of VBlank).

## NMI Synchronization (`waitNMI`)

Because the game uses a dynamic NMI handler to drive the game loop, `waitNMI` is used to ensure the code waits for the next NMI trigger.

- **Mechanism**:
    - Captures the current value of `FRAME_CNT`.
    - Loops until `FRAME_CNT` changes.
    - Since `FRAME_CNT` is incremented at the start of every NMI handler, this effectively blocks execution until the next frame begins.

## Framerate Control (`waitNMI50`)

`waitNMI50` is a higher-level synchronization routine used to slow down animations (e.g., during level transitions or "Splay" effects) to approximately 50% of the normal speed or a specific interval.

- **Mechanism**:
    - It calls `waitNMI`.
    - It then calls `ntscIsSkip` to determine if a frame should be skipped based on the console's region (NTSC vs PAL).
    - If the frame is not skipped, it performs a `FamiToneUpdate` to keep the audio engine synchronized while the game logic is paused.

## Region Detection & Frame Skipping (`ntscIsSkip`)

To maintain a consistent game speed across different NES regions (NTSC vs PAL), the game implements a frame-skipping mechanism.

- **Mechanism**:
    - Checks the `GAME_NTSC` flag.
    - If the game is in NTSC mode, it increments `FRAME_CNT2`.
    - When `FRAME_CNT2` reaches 5, it resets and returns `C=1` (Skip).
    - This effectively skips every 6th frame in NTSC mode to match the timing of PAL hardware or a specific target speed.

# Citations
[1] [Source Code: game.asm](/sources/Source/game.asm)
