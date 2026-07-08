# Assembly Modules
* [Input System](controller.md) - Logic for polling the NES gamepad and detecting button presses.
* [OAM Management](oam_management.md) - Logic for managing the NES Object Attribute Memory (OAM) and rendering the game cursor.
* [Rendering](rendering.md) - Logic for mapping internal game map tiles to NES PPU VRAM addresses and character patterns.
* [RNG Subsystem](rng.md) - Implementation of a Galois Linear Feedback Shift Register (LFSR) for pseudo-random number generation.
* [Timing & Sync](timing_sync.md) - Low-level routines for synchronizing game logic and rendering with the NES NMI and VBlank.

# Build Systems
* [Build System](build_system.md) - Documentation of the assembly and compilation process for Lan Master NES.

# Game Mechanics
* [Level Editor](level_editor.md) - Analysis of the C++ based level editor used to create and export levels for Lan Master.

# References
* [Binary Layout](binary_layout.md) - Technical mapping of the Lan Master ROM binary, including iNES header and memory bank organization.
* [Memory Map](memory_map.md) - Mapping of the NES RAM used by Lan Master.
