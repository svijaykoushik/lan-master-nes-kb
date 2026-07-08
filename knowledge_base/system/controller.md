---
type: Assembly Module
title: Input System
description: Logic for polling the NES gamepad and detecting button presses.
resource: sources/Source/controller.asm
tags: [system, input, hardware]
timestamp: 2026-06-29T11:40:00Z
---

# Implementation
The input system handles low-level interaction with the NES controller hardware via `CTRL_PORT1`.

## Input Polling
The `padPoll` routine implements a debounced polling mechanism:
1. **Port Read**: `padPollPort` is called three times to read the controller state into `PAD_BUF` to avoid noise.
2. **State Comparison**: The current state is compared against the previous state (`PAD_STATEP`).
3. **Edge Detection**: 
   - `PAD_STATE`: Stores the current continuous state of the buttons.
   - `PAD_STATET`: Stores "trigger" events (buttons that were just pressed this frame).

## Button Mapping
The following constants are used to mask the input state:
- `PAD_A`, `PAD_B`, `PAD_SELECT`, `PAD_START`
- `PAD_UP`, `PAD_DOWN`, `PAD_LEFT`, `PAD_RIGHT`

# Citations
[1] [Source Code: controller.asm](../../sources/Source/controller.asm)
