---
type: Assembly Module
title: Password System
description: Logic for entering and verifying 4-digit passcodes to unlock specific game levels.
resource: sources/Source/mainmenu.asm
tags: [logic, security, input]
timestamp: 2026-07-03T11:30:00Z
---

# Implementation

*Lan Master* features a 4-digit passcode system allowing players to resume gameplay from any of the 50 stages.

---

## User Interface & State Buffer

- **Input Buffer**: Stored in Zero Page RAM at `GAME_CODE` (4 bytes, `GAME_CODE+0` through `GAME_CODE+3`).
- **Cursor State**: `MENU_CODECUR` tracks active digit selection (0–3).
- **Navigation**: D-Pad Left/Right selects digit position; D-Pad Up/Down increments/decrements digit values (0–9).

---

## Verification Logic (`mainMenuCodeSelect`)

When confirmed, `mainMenuCodeSelect` scans the 49-entry 16-bit BCD password table (`passwords` in `mainmenu.asm`):

### 16-Bit Packed BCD Nibble Encoding

Each 16-bit word entry in `passwords` encodes a 4-digit BCD code in little-endian format:

$$\text{16-Bit Word} = (\text{Digit}_0 \ll 12) \,\,|\,\, (\text{Digit}_1 \ll 8) \,\,|\,\, (\text{Digit}_2 \ll 4) \,\,|\,\, \text{Digit}_3$$

- **High Byte**: High nibble = `Digit 0`, Low nibble = `Digit 1`.
- **Low Byte**: High nibble = `Digit 2`, Low nibble = `Digit 3`.

### Level Index Resolution

If a match occurs at table offset $i$ (where $0 \le i \le 48$), the target stage level is assigned as:

$$\text{Target Stage Level} = i + 2 \quad (\text{Levels 2 to 50})$$

Level 1 requires no password and starts by default from "New Game".

---

## Hidden Diagnostic SFX Test Mode

Entering passcode `68xx` (Digit 0 = 6, Digit 1 = 8) bypasses stage selection and triggers `mainMenuSfxTest`.
- The remaining two digits (`xx`) specify the sound effect ID ($00$–$11$).
- See [Hidden Main Menu Diagnostics & Secret Passcodes](cheats_diagnostics.md) for full details.

---

## Citations
[1] [Source Code: mainmenu.asm](../../sources/Source/mainmenu.asm)
[2] [Diagnostics Spec: cheats_diagnostics.md](cheats_diagnostics.md)

