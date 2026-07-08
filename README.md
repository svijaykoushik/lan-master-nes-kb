# Lan Master NES - Knowledge Reconstruction

This repository contains a complete technical reconstruction of the **Lan Master** NES project. Rather than a software development project, this is a **knowledge-first archive** designed to extract, analyze, and preserve the software engineering and design decisions embedded in the original 6502 Assembly source code.

<p align="center">
  <img src="/assets/label.png" alt="Lan Master Poster">
</p>

## 📜 Context & Origin

### The Original Game
**Lan Master** is a homebrew puzzle game for the Nintendo Entertainment System (NES), developed by indie developer Shiru and released on June 9, 2011. It marked Shiru's debut game on the NES platform, with a classic chiptune soundtrack composed by Alex Semenov. Heavily inspired by the network-routing puzzle game *NetWalk*, it tasks the player with rotating randomized grid tiles to connect scattered computers to a central server before a countdown timer expires. The game features 50 levels of increasing difficulty and a built-in password system. 

Shiru entered the game into the 2011 NintendoAge NES Coding Competition, where it earned 2nd place. True to his frequent support for the open-source community, Shiru released the game entirely for free into the **Public Domain**, publishing its full source code.

### The Reconstruction Project
As someone who loved playing this homebrew classic, discovering that its full assembly source code was public domain sparked a unique preservation idea. 

The goal of this project is to take that raw, open-source 6502 assembly and transform it into a "Karpathy-style" LLM wiki: a concept-first, deeply interconnected knowledge base. This allows any software engineer to understand the game's inner workings without needing specialized vintage hardware knowledge.

To accomplish this massive technical mapping and translation effort, the wiki was meticulously generated using local AI orchestration—leveraging the **Gemma 4 (31B)** model running entirely on device via **Ollama**.

## 📖 The Knowledge Base (KB)

The heart of this repository is the `knowledge_base/` directory, which follows the **Open Knowledge Format (OKF) v0.1**.

### Navigation
The best way to explore the project is by starting at the **[Knowledge Base Index](knowledge_base/index.md)**. From there, you can dive into:

- **Core Architecture**: High-level execution flow, the NMI-driven game loop, and the project mapping.
- **System Components**:
    - **Hardware Interfaces**: Input polling, Timing & Synchronization, and OAM/Sprite management.
    - **Graphics Pipeline**: PPU rendering, Palette management, and RLE decompression.
    - **Tooling**: Analysis of the original C++ level editor and the NESASM build pipeline.
- **Game Logic**:
    - **Connectivity Engine**: The BFS algorithm used for win-condition verification.
    - **Level Mechanics**: Generation, randomization, and tile rotation.
    - **Security**: The nibble-based password verification system.
- **Audio System**: Detailed analysis of the FamiTone engine, DPCM samples, and the audio catalog.
- **Assets**: Logical-to-physical pattern mapping and graphics data.
- **User Interface**: Menu state machines and visual formatting primitives.

## 🛠 Technical Foundation

### The Source Code as Evidence
The original source code (located in `sources/`) is treated as **ground truth evidence**. Every claim in the knowledge base is cited back to specific assembly routines or data tables.

### Open Knowledge Format (OKF)
All documentation is structured using OKF, which ensures:
- **Strict Metadata**: Every concept has a type, title, resource link, and timestamp.
- **Traceability**: Direct citations from conceptual explanations to implementation details.
- **Modularity**: Knowledge is broken down into atomic concepts to avoid duplication and ensure maintainability.

## 📂 Repository Structure

- `knowledge_base/`: The reconstructed documentation (OKF format).
- `sources/`: Original 6502 Assembly source code and raw assets.
- `OKF_SPEC.md`: The formal specification for the knowledge base format.
- `AGENTS.md`: Guidelines for AI agents performing reconstruction tasks.

---
*This archive preserves the technical legacy of Lan Master, transforming raw assembly into transferable software engineering knowledge.*