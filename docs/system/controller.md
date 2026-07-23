---
type: Assembly Module
title: Input System
description: Logic for polling the NES gamepad and detecting button presses.
resource: sources/Source/controller.asm
tags: [system, input, hardware]
timestamp: 2026-06-29T11:40:00Z
---

# Implementation

The input system in `controller.asm` manages gamepad interface registers (`$4016` / `$4017`) and provides debounced button state and edge detection.

---

## Hardware DPCM DMA Glitch Filter (Triple Sampling)

On standard NES hardware, playing DPCM audio samples can corrupt controller port reads (`$4016`) due to DPCM DMA cycle stealing coinciding with clock transitions.

To guarantee 100% reliable input readings, `padPoll` calls `padPollPort` three times into temporary buffers (`PAD_BUF+0`, `PAD_BUF+1`, `PAD_BUF+2`) and applies a bitwise majority-vote filter:

$$\text{PAD\_STATE} = (B_0 \land B_1) \lor (B_1 \land B_2) \lor (B_0 \land B_2)$$

This voting scheme discards single-bit glitches caused by DPCM DMA interrupts during controller shifts.

---

## Button Edge Detection Math

To distinguish continuous button holds from new single-frame button presses, `padPoll` computes:

$$\text{PAD\_STATET} = \text{PAD\_STATE} \land (\text{PAD\_STATE} \oplus \text{PAD\_STATEP})$$

- `PAD_STATE`: Bitmask of buttons currently held down.
- `PAD_STATEP`: Bitmask of buttons held during the previous frame.
- `PAD_STATET`: Trigger events (buttons pressed down on the *current* frame).

---

## Button Bitmask Constants

| Constant | Bitmask (Hex) | Game Action |
| :--- | :--- | :--- |
| `PAD_RIGHT` | `$01` | Move cursor Right / Navigate Menu |
| `PAD_LEFT`  | `$02` | Move cursor Left / Navigate Menu |
| `PAD_DOWN`  | `$04` | Move cursor Down / Decrement Code |
| `PAD_UP`    | `$08` | Move cursor Up / Increment Code |
| `PAD_START` | `$10` | Pause Game / Confirm Menu Option |
| `PAD_SELECT`| `$20` | Toggle Option / Change Target |
| `PAD_B`     | `$40` | Rotate Tile Counter-Clockwise ($270^\circ$) |
| `PAD_A`     | `$80` | Rotate Tile Clockwise ($90^\circ$) |

---

## Citations
[1] [Source Code: controller.asm](../../sources/Source/controller.asm)

