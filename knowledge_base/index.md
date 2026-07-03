# Lan Master NES Knowledge Base

## Core Architecture
* [High-Level Architecture](/knowledge_base/architecture.md) - Overview of the game loop, state management, and core objective.
* [Project Map](/knowledge_base/project_map.md) - Mapping of the source codebase to functional game components.

## System Components
* [System](/knowledge_base/system/) - Hardware interfaces and core system modules.
    - [Memory Map](/knowledge_base/system/memory_map.md) - Detailed RAM usage and variable locations.
    - [Input System](/knowledge_base/system/controller.md) - Gamepad polling and debouncing.
    - [Rendering](/knowledge_base/system/rendering.md) - PPU mapping and tile updates.
    - [Level Editor](/knowledge_base/system/level_editor.md) - Analysis of the design and export tool.
    - [Build System](/knowledge_base/system/build_system.md) - Assembly pipeline and ROM generation.
    - [Binary Layout](/knowledge_base/system/binary_layout.md) - ROM structure and bank mapping.
* [Logic](/knowledge_base/logic/) - Game rules and connectivity engines.
    - [Connectivity Engine](/knowledge_base/logic/tracemap.md) - The BFS algorithm for win condition.
    - [Level Definitions](/knowledge_base/logic/levels.md) - Level layout and generation logic.
    - [Level Generation](/knowledge_base/logic/level_generation.md) - Unpacking and randomization.
    - [Rotation Mechanics](/knowledge_base/logic/rotation.md) - Manual and automatic tile rotation.
    - [Connectivity Rules](/knowledge_base/logic/connectivity_rules.md) - The pinsTable connectivity matrix.
* [Audio](/knowledge_base/audio/) - Music and sound effect implementation.
    - [FamiTone Engine](/knowledge_base/audio/famitone.md) - Sequencer, envelopes, and DPCM playback.
    - [Audio Catalog](/knowledge_base/audio/audio_catalog.md) - Mapping of SFX and BGM to game events.
* [Assets](/knowledge_base/assets/) - Graphics, level data, and compression.
    - [RLE Decompression](/knowledge_base/assets/rle.md) - Background compression and unpacking.
    - [Palette System](/knowledge_base/assets/palette.md) - Color management and fade effects.
    - [Pattern Mapping](/knowledge_base/assets/pattern_mapping.md) - Logical tile to PPU index mapping.
* [UI](/knowledge_base/ui/) - Menu systems and visual interfaces.
    - [Menus](/knowledge_base/ui/menus.md) - Main, Game, and Win screen logic.
