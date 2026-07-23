---
type: Assembly Module
title: FamiTone Engine
description: Implementation of the FamiTone audio library used for BGM and SFX.
resource: sources/Source/famitone.asm, sources/Source/sfx.asm
tags: [audio, hardware, apu]
timestamp: 2026-06-29T12:30:00Z
---


# Implementation
# System Overview

Lan Master uses the **FamiTone** audio library, a custom implementation for the NES APU (Audio Processing Unit). It supports both sequenced background music (BGM) and triggered sound effects (SFX), as well as DPCM samples.

## [Architecture](../architecture.md)

FamiTone manages the five NES audio channels:
- **Pulse 1 & 2**: Used for melodies and harmonies.
- **Triangle**: Used for bass or percussive elements.
- **Noise**: Used for percussion and sound effects.
- **DMC**: Used for sampled audio.

### 1. Music Engine (`FamiToneMusicStart`)
Music is played using "modules" (sequences of notes and instrument changes).
- **Channel Management**: Each channel has a structure (`FT_CHN_STRUCT_SIZE` = 9 bytes) tracking the current note, instrument, pointer into the music data, and reference lengths.
- **Envelopes**: FamiTone uses envelopes to control volume and pitch over time.
- **Reference Logic**: Supports "references" (jumps to other parts of the music sequence) to reduce data size.
- **Timing**: `FT_SONG_SPEED` controls the tempo, and `FT_FRAME_CNT` synchronizes updates with the TV frame.

### 2. Sound Effects Engine (`FamiToneSfxStart`)
SFX are handled as short, high-priority streams that can overwrite the BGM.
- **Streams**: Supports multiple simultaneous SFX streams (`FT_SFX_STREAMS`).
- **Mixing**: The `FamiToneSfxUpdate` routine compares the volume of the active SFX against the current BGM output and overwrites the APU registers if the SFX is louder.
- **Data Format**: SFX are defined as a series of register writes and repeat counts.

### 3. DPCM Sample Playback (`FamiToneSampleStart`)
Direct Memory Access (DMA) is used to play samples from the bank 3 memory region.
- **Sample Table**: A table defines the offset, length, and pitch/loop parameters for each sample.
- **Priority**: SFX samples have higher priority than BGM samples.

# Hardware Interface

The library writes directly to the NES APU registers:
- `$4000 - $400F`: Volume, sweep, and frequency registers for Pulse, Triangle, and Noise channels.
- `$4010 - $4013`: DMC frequency, raw data, start, and length.
- `$4015`: Channel enable register.

# Citations
[1] [Source Code: famitone.asm](../../sources/Source/famitone.asm)
[2] [Source Code: sfx.asm](../../sources/Source/sfx.asm)
