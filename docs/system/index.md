# System Subsystems & Low-Level Architecture

The **System Subsystems** section documents low-level hardware interactions, execution timing, input polling, sprite/OAM management, PPU rendering routines, pseudo-random number generation (LFSR), RAM layout, and build pipelines for *Lan Master*.

---

## Assembly Modules & System Control
* [Input System](controller.md) - Gamepad input polling, hardware DPCM DMA glitch filtering, and button edge detection.
* [Dynamic NMI Trampoline Vectoring](nmi_vectoring.md) - RAM-based dynamic NMI trampoline vector dispatching (`NMI_CALL` at `$FA`).
* [OAM Management](oam_management.md) - Hardware Object Attribute Memory (OAM) manipulation for rendering the animated game cursor and UI sprites.
* [Rendering Subsystem](rendering.md) - Real-time PPU VRAM tile mapping and VBlank display updating routines.
* [RNG Subsystem](rng.md) - Galois Linear Feedback Shift Register (LFSR) pseudo-random number generator used for random tile rotation and level shuffling.
* [Timing & Synchronization](timing_sync.md) - NMI vector dispatching, Blargg cycle-timing region detection, and 50Hz PAL/NTSC normalization.

## Build Systems & Level Tools
* [Build Pipeline](build_system.md) - Assembly compilation workflow using NESASM and `compile.bat`.
* [Level Editor Architecture & 3-Bit Level Format](level_editor_architecture.md) - Architectural analysis of `lanme` and 3-bit binary level packing format.
* [Level Editor Overview](level_editor.md) - High-level overview of the level editor tool.

## Memory & Binary Specifications
* [Binary Layout](binary_layout.md) - iNES header configuration, ROM banking structure, and PRG/CHR ROM offset mapping.
* [Memory Map](memory_map.md) - Detailed Zero Page, RAM stack, OAM buffer ($0200), grid map ($0300), traversal table ($0400), and terminal list ($0500) allocations.


