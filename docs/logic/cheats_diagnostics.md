---
type: Game Mechanic
title: Hidden Main Menu Diagnostics & Secret Passcodes
description: Built-in passcode diagnostics mode for sound effect testing and level cheats.
resource: sources/Source/mainmenu.asm
tags:
  - logic
  - cheats
  - diagnostics
  - audio
timestamp: 2026-07-24T00:20:00Z
---

# Hidden Main Menu Diagnostics & Secret Passcodes

## System Overview

*Lan Master* contains a secret diagnostic test mode built into the Main Menu passcode entry system (`mainmenu.asm`), allowing developers and testers to preview and play all sound effects directly from the title screen.

---

## Technical Implementation (`mainMenuSfxTest`)

### Trigger Condition

When the player enters a 4-digit passcode starting with `68` (Digit 0 = 6, Digit 1 = 8), the main menu bypasses standard level passcode lookup and jumps to `mainMenuSfxTest`.

### Sound Effect Index Calculation

The sound effect ID played is calculated from the remaining two passcode digits (Digit 2 and Digit 3):

$$\text{SFX ID} = (\text{Digit 2} \times 10) + \text{Digit 3}$$

```assembly
; mainmenu.asm lines 545-561
mainMenuSfxTest:
    lda GAME_CODE+2    ; Load 3rd digit
    asl a              ; Multiply by 10 (asl*2 + asl*8)
    sta TEMP
    asl a
    asl a
    clc
    adc TEMP
    adc GAME_CODE+3    ; Add 4th digit
    jsr sfxPlay        ; Trigger SFX test
```

### Supported Sound Effect Range

Passcodes `6800` through `6811` trigger SFX IDs 0 through 11:

| Passcode | Played SFX | Description |
| :--- | :--- | :--- |
| `6800` | SFX 0 | Menu Cursor Move |
| `6801` | SFX 1 | Menu Select / Confirm |
| `6802` | SFX 2 | Stage Clear Fanfare |
| `6803` | SFX 3 | Menu Back / Error |
| `6804` | SFX 4 | Stage Start |
| `6805`–`6806` | SFX 5–6 | Player Tile Rotation 1 & 2 |
| `6807`–`6808` | SFX 7–8 | Network Degradation Rotation 3 & 4 |
| `6809` | SFX 9 | Network Online Connection Spark |
| `6810` | SFX 10 | Low Time Countdown Tick |
| `6811` | SFX 11 | Timeout Alarm |

---

## Citations
[1] [Source Code: mainmenu.asm](../../sources/Source/mainmenu.asm)
