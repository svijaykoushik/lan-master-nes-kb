# Lan Master NES - Knowledge Base

Welcome to the **Lan Master (NES)** knowledge base. *Lan Master* is an original puzzle game for the Nintendo Entertainment System written in 6502 assembly. The player's objective is to rotate network cables and components on a $16 \times 16$ tile grid to form a fully connected network connecting all terminal computers before time runs out.

This knowledge base reconstructs and explains the game's software architecture, memory organization, rendering pipeline, sound engine, level data, and connectivity algorithms using modern software engineering terminology. It is designed to allow developers to understand, analyze, or reproduce the game without needing prior assembly or NES hardware experience.

---

## Core Game Documentation
* [Architecture](architecture.md) - Overview of execution flow, NMI-driven timing, and system state machine.
* [Project Map](project_map.md) - Comprehensive mapping of source assembly files to functional game concepts.
* [Project Log](log.md) - Chronological history of knowledge base updates and modifications.

---

## Subsystem Navigation

* [Assets & Graphics](assets/index.md) - NES color palettes, tile pattern mappings, and RLE decompressor.
* [Audio Engine](audio/index.md) - FamiTone sound engine integration, BGM tracks, and SFX catalogs.
* [Game Logic](logic/index.md) - Tile rotation mechanics, level layouts, passcode verification, and BFS connectivity engine.
* [System Subsystems](system/index.md) - Memory map, input system, rendering pipeline, LFSR RNG, OAM management, and build system.
* [User Interface](ui/index.md) - Main menu, pause menu, stage victory screens, and PPU text formatting.

