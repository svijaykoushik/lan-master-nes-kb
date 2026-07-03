---
type: Reference
title: Binary Layout (ROM Structure)
description: Technical mapping of the Lan Master ROM binary, including iNES header and memory bank organization.
resource: sources/Source/game.asm
tags: [system, binary, rom, hardware]
timestamp: 2026-07-03T10:15:00Z
---

# ROM Binary Structure

Lan Master is distributed as an `.nes` file, which follows the iNES format. The binary is structured to fit the NES's memory mapping requirements, using multiple banks to extend the available program memory.

## iNES Header

The ROM starts with a 16-byte header that tells the emulator how to map the memory:

- **PRG ROM Size**: 2 banks (16 KB $\times$ 2 = 32 KB).
- **CHR ROM Size**: 1 bank (8 KB).
- **Mirroring**: Vertical mirroring (`.inesmir 1`).
- **Mapper**: NROM (Mapper 0), the simplest NES mapper.

## Memory Bank Mapping

The project uses a multi-bank structure to organize code, audio, and assets.

### Bank 0: Core Logic & Systems
- **Address**: `$8000 - $BFFF` (when mirrored).
- **Contents**: 
    - Hardware initialization and the main game loop.
    - Core system modules (Input, Rendering, Memory Management).
    - The `nmiHandlersList` and the dynamic NMI dispatcher.
    - Included modules: `mainmenu.asm`, `gamemenu.asm`, `tracemap.asm`, `rle.asm`, `palette.asm`, `controller.asm`, `famitone.asm`.
    - **Interrupt Vectors**: Located at `$FFFA - $FFFF`, containing the pointers for `NMI_CALL` and `reset`.

### Bank 1: BGM Modules (Part 1)
- **Address**: `$A000`
- **Contents**: 
    - `bgm_title.asm`
    - `bgm_done.asm`
    - `bgm_timeout.asm`

### Bank 2: BGM Modules (Part 2) & Level Data
- **Address**: `$C000`
- **Contents**: 
    - `bgm_game.asm`
    - `levels.asm` (The binary data for all 50 levels).

### Bank 3: Samples & Final Screens
- **Address**: `$E000`
- **Contents**: 
    - `bgm_game_dpcm.bin` (Raw DPCM samples).
    - `bgm_game_dpcm.asm` (Sample offsets).
    - `sfx.asm` (Sound effect definitions).
    - `welldone.asm` (The victory screen logic).

### Bank 4: Graphics (CHR-ROM)
- **Address**: `$0000` (CHR Space)
- **Contents**: 
    - `patterns.chr`: The raw 8x8 pixel tile data used by the PPU.

# Citations
[1] [Source Code: game.asm](/sources/Source/game.asm)
