---
type: Reference
title: Memory Map
description: Mapping of the NES RAM used by Lan Master.
tags: [memory, hardware, 6502]
timestamp: 2026-06-29T12:00:00Z
---

# [Memory Map](memory_map.md)

Lan Master utilizes several regions of the NES's 2KB internal RAM.

## Zero Page ($00 - $FF)

The Zero Page is used for high-speed access to global game state and temporary variables.

### 1. Hardware and Timing (Lower Zero Page)
- `$00 - $04`: [Palette](../assets/palette.md)s and temporary storage (`TEMP`, `PAL_LOW`, `PAL_HIGH`, etc.).
- `$FF`: `FRAME_CNT` - Global frame counter.
- `$FE`: `FRAME_CNT2` - Second frame counter (used for NTSC timing).
- `$FD`: `RAND_SEED` - Seed for the Galois random number generator.
- `$FA - $FD`: `NMI_CALL` - Stores the opcode and address for the dynamic NMI handler.

### 2. Input State (Near $F9)
- `$F9`: `PAD_STATE` - Continuous state of controller buttons.
- `$F8`: `PAD_STATEP` - Previous frame's controller state.
- `$F7`: `PAD_STATET` - Trigger events (buttons pressed this frame).

### 3. Menu State ($E8 - $EF)
- `$EF`: `MENU_BASE`
- `$EE`: `MENU_CUR` - Current selection index.
- `$ED`: `MENU_CNT` - Animation/timing counter.
- `$EC - $EB`: `MENU_CURADRL/H` - Address of the cursor in VRAM.
- `$EA`: `MENU_CODECUR` - Cursor position in the password entry field.
- `$E9`: `MENU_ANIM` - Animation state.
- `$E8`: `MENU_SET` - Menu display settings.

### 4. Game State ($B7 - $E7)
- `$E7`: `GAME_BASE`
- `$E6 - $E3`: Cursor coordinates (`GAME_CUR_SX`, `SY`, `DX`, `DY`).
- `$E2`: `GAME_CUR_OFF` - Cursor movement offset/delay.
- `$E1`: `GAME_CUR_COL` - Current column for status updates.
- `$E0 - $DF`: Rotation coordinates (`GAME_ROTATE_X`, `Y`).
- `$DE`: `GAME_SFX` - SFX enable flag.
- `$DD`: `GAME_BGM` - BGM enable flag.
- `$D9 - $DC`: `GAME_CODE` - 4-byte password buffer.
- `$D8`: `GAME_NTSC` - NTSC/PAL detection flag.
- `$D7`: `GAME_LEVEL` - Current level index.
- `$D5 - $D6`: `GAME_ONLINE` - Word representing connectivity status.
- `$D4`: `GAME_TIME` - Remaining time for the level.
- `$D3`: `GAME_ROTATE` - Rotation amount/state.
- `$D2`: `GAME_TIME_DIV` - Divider for timing calculations.
- `$CF - $CE`: `GAME_RROT_CNT` - Random rotation counter.
- `$CD - $CC`: `GAME_RROT_TIME` - Random rotation timing.
- `$CC`: `GAME_TERM_CNT` - Total number of terminals in the level.
- `$CB`: `GAME_TERM_OFF` - Current terminal being processed.
- `$CA`: `GAME_CALL_MENU` - Flag to trigger pause menu.
- `$C9`: `GAME_TERM_TRACE` - Terminal index used during connectivity check.
- `$C8`: `GAME_TRACE_CNT` - Countdown for periodic traceMap calls.
- `$C7`: `GAME_ONLINE_SCR` - Status value for screen display.
- `$C5 - $C4`: `GAME_TERM_FP` - Terminal starting point for trace.
- `$C4`: `GAME_DELAY` - General purpose delay timer.
- `$C2 - $C1`: `GAME_TABLE_VRAM` - VRAM address for table display.
- `$C0`: `GAME_TABLE_HGT` - Height of the table being displayed.
- `$BE - $BF`: `GAME_TABLE_SRC` - Source address of data to be displayed.
- `$BD`: `GAME_TABLE_CODE` - Code for special table behavior.
- `$BC`: `GAME_TERM_ONGFX` - Terminal graphics offset.
- `$BB`: `GAME_TRACE_SKIP` - Flag to skip trace if map was modified.
- `$BA`: `GAME_TIME_OUT` - Timer expiration flag.
- `$B9`: `GAME_ROTATE_SFX` - SFX index for rotation.
- `$B8`: `GAME_START_POS` - Starting position for level unpacking.
- `$B7`: `GAME_LOOP_ON` - Game loop active flag.

### 5. FamiTone Variables ($F0 - $F6)
Reserved for the FamiTone music engine.

## Internal RAM ($0200 - $07FF)

### 1. Level Map (`GAME_MAP`, $0300)
A 16x16 byte array (256 bytes) containing the tile types for the current level.

### 2. Visit Flags (`GAME_CHECK`, $0400)
A 16x16 byte array (256 bytes) used by the `traceMap` algorithm to mark visited tiles and their connectivity.

### 3. Terminal List (`GAME_TERM_LIST`, $0500)
A list of offsets into `GAME_MAP` for all terminal tiles in the level.

### 4. Level Init Buffer (`GAME_MAP_BUF`, $0400)
Used during level initialization for the display effect.

### 5. Menu Buffer (`GAME_MENU_BUF`, $0400)
Used during pause menu operations.

### 6. Trace Lists (`T_LISTPAGE`, $0600)
The `traceMap` routine uses this page to implement its BFS queues.

### 7. OAM Page (`OAM_PAGE`, $0700)
Buffer for sprite attributes (4 bytes per sprite).

# Citations
[1] [Source Code: game.asm](../../sources/Source/game.asm)
[2] [Source Code: tracemap.asm](../../sources/Source/tracemap.asm)
