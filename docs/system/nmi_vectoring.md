---
type: Assembly Module
title: Dynamic NMI Trampoline Vectoring
description: Low-latency NMI handler dispatch mechanism utilizing RAM vector trampoline.
resource: sources/Source/game.asm
tags:
  - system
  - nmi
  - timing
  - 6502
timestamp: 2026-07-24T00:20:00Z
---

# Dynamic NMI Trampoline Vectoring Engine

## System Overview

*Lan Master* utilizes a dynamic NMI (Non-Maskable Interrupt) vectoring mechanism to switch between frame handling modes without conditional branching overhead or bank-switching latencies inside VBlank. 

The hardware NMI interrupt vector at `$FFFA` points directly to a 3-byte RAM vector located at Zero Page address `$FA` (`NMI_CALL`).

---

## Technical Implementation

### RAM Vector Layout (`NMI_CALL` at `$FA`)

The RAM at address `$FA` is populated as a 6502 `JMP` opcode (`$4C`) followed by a 16-bit target address:

```text
Address  | Byte Value | Instruction
-----------------------------------
$00FA    | $4C        | JMP abs
$00FB    | Target LSB | Target address low byte
$00FC    | Target MSB | Target address high byte
```

When an NMI occurs, execution vectors to `$FFFA`, which immediately jumps to `$00FA` in RAM, executing the trampoline `JMP` to the currently assigned handler routine.

---

## Handlers & State Machine

The system provides four primary NMI handler modes:

| Routine | Purpose | Operations |
| :--- | :--- | :--- |
| `nmiEmpty` | Idle / Waiting | Increments `FRAME_CNT`. Immediate `RTI`. |
| `nmiSound` | Sound-only Updates | Increments `FRAME_CNT` $\rightarrow$ calls `FamiToneUpdate`. |
| `nmiGame` | Full Gameplay Loop | Increments `FRAME_CNT` $\rightarrow$ decrements `GAME_TIME` timer $\rightarrow$ executes main game loop. |
| `nmiDone` | Stage Victory Animation | Increments `FRAME_CNT` $\rightarrow$ handles victory background scrolling & animation. |

---

## Vector Modification (`setNmiHandler`)

To switch NMI handlers safely without corrupting vector execution mid-interrupt, `game.asm` implements the `setNmiHandler` routine:

```assembly
setNmiHandler:
    sta NMI_CALL+1    ; Write target LSB
    stx NMI_CALL+2    ; Write target MSB
    rts
```

Calling `setNmiHandler` with target LSB in `A` and MSB in `X` atomically updates the trampoline destination vector for the next VBlank cycle.

---

## Citations
[1] [Source Code: game.asm](../../sources/Source/game.asm)
