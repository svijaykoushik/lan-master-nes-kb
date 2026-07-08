---
type: Assembly Module
title: Password System
description: Logic for entering and verifying 4-digit passcodes to unlock specific game levels.
resource: sources/Source/mainmenu.asm
tags: [logic, security, input]
timestamp: 2026-07-03T11:30:00Z
---

# Implementation
# [Password System](passwords.md)

Lan Master features a password system that allows players to bypass early levels and jump directly to a specific level in the 50-level sequence.

## User Interface

The password entry is a sub-state of the Main Menu.
- **Input**: The user navigates a 4-digit number using the D-pad.
- **Cursor**: A visual cursor (`MENU_CODECUR`) identifies which digit is currently being edited.
- **Entry**: The entered digits are stored in the `GAME_CODE` buffer (4 bytes).

## Verification Logic

Verification occurs when the user confirms their entry (`mainMenuCodeSelect`). The game compares the entered 4-digit code against a table of 16-bit words stored in the `passwords` table.

### The Nibble-Based Comparison

The `passwords` table stores each password as a 16-bit word. Each digit of the password is represented by a 4-bit nibble.

1. **Data Extraction**: The routine iterates through the `passwords` table. For each entry, it extracts four nibbles using bit-shifting (`ror a` 4 times) and masking (`and #15`).
2. **Matching**:
   - The entered `GAME_CODE` buffer is compared against these extracted nibbles.
   - A match is confirmed if all four nibbles match the extracted values of a password entry in the table.
3. **Level Unlocking**: If a match is found at index `x`, the game sets the current level to `(x / 2) + 1`.

## Special Modes

### SFX Test Mode
The password system includes a hidden diagnostic mode. If a specific code is entered (e.g., a code starting with 6 or 8), the game enters `mainMenuSfxTest`.
- **Function**: This mode allows the user to trigger and test various sound effects from the `sfx.asm` library by entering specific numerical sequences.

# Citations
[1] [Source Code: mainmenu.asm](../../sources/Source/mainmenu.asm)
[2] [Source Code: game.asm](../../sources/Source/game.asm)
