# Lan Master NES - OKF Specification

This document defines the strict application of the **Open Knowledge Format (OKF) v0.1** for the Lan Master NES knowledge base. Agents MUST adhere to these definitions when creating or updating concepts.

## 2. Bundle Structure & Organization
- **Data Organization**: Concepts MUST be grouped into one or more directories based on relevancy (e.g., `/audio`, `/graphics`, `/logic`).
- **Reserved Filenames**:
    - `index.md`: MUST appear in every directory under `knowledge_base/` to enumerate contents and support progressive disclosure.
    - `log.md`: MAY appear at any level to record the history of changes as a flat list of date-grouped entries (newest first).

## 3. Concept Types
To ensure consistency, agents MUST use the following `type` values for frontmatter:

| Type | Description | Example Resource |
| :--- | :--- | :--- |
| `Assembly Module` | A specific `.asm` file or a logical group of assembly routines. | `sources/Source/game.asm` |
| `Game Asset` | Graphics (`.rle`, `.chr`) or Audio (`.bin`) files. | `sources/Source/patterns.chr` |
| `Game Mechanic` | A high-level rule or behavior (e.g., "Collision Detection"). | N/A (Abstract) |
| `Memory Map` | Definitions of RAM, ROM, or Register usage. | N/A (Abstract) |
| `Build System` | Documentation regarding the compilation process. | `sources/Source/compile.bat` |
| `Reference` | External documentation or manual entries. | `sources/manual.md` |

## 3. Field Requirements
- **`type`**: REQUIRED. Must be one of the values above.
- **`title`**: REQUIRED. Descriptive name of the concept.
- **`description`**: REQUIRED. One-sentence summary.
- **`resource`**: REQUIRED for `Assembly Module`, `Game Asset`, and `Build System`. Use the path relative to the repository root.
- **`tags`**: RECOMMENDED. Use tags like `graphics`, `audio`, `logic`, `input`.
- **`timestamp`**: REQUIRED. Use ISO 8601 format.

## 4. Body Conventions
- Use `# Implementation` instead of `# Schema` for assembly modules to describe the logic.
- Use `# Asset Details` for `Game Asset` types to describe formats (e.g., "RLE compressed graphics").
- All links to other concepts MUST use the absolute format: `[Title](/path/to/concept.md)`.
- Cross-linking is mandatory: Every time a concept defined in the knowledge base is mentioned, it MUST be linked to its corresponding document.
- Use `# Citations` to link back to the original source file or the `manual.md`.

## 5. Example Concept: game.asm

```markdown
---
type: Assembly Module
title: Main Game Logic
description: Core game loop and primary state management.
resource: sources/Source/game.asm
tags: [logic, core]
timestamp: 2026-06-29T10:00:00Z
---

# Implementation
The main game loop handles the transition between different game states.

# Citations
[1] [Source Code: game.asm](sources/Source/game.asm)
```
