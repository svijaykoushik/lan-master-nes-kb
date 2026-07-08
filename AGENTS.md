# Agent Guidelines - Lan Master NES

# Project Context

- **Project**: Lan Master (NES)
- **Language**: 6502 Assembly
- **Source Root**: `sources/Source/`
- **Build System**: sources/Source/compile.bat
- **Reference Documentation**: sources/manual.md

---

# Knowledge Base Philosophy

> **The source code is evidence; the knowledge base is an explanation.**

The objective is not to document assembly code. The objective is to reconstruct and explain the software architecture, systems, algorithms, and design decisions embedded within the source code.

---

# Knowledge Base Goal

The knowledge base shall:

- Reconstruct the architecture, systems, algorithms, execution flow, and design decisions of the game from the source code.
- Enable an experienced software engineer to understand the complete workings of the game without requiring knowledge of 6502 assembly or NES hardware.
- Preserve implementation details while explaining concepts in a manner transferable to modern software and game development.
- Clearly distinguish verified facts, deductions, hypotheses, and unknowns.
- Strictly follow the **[Open Knowledge Format (OKF) v0.1 specification](OKF_SPEC)**.
- Store all documentation under the `docs/` directory.

---

# Technical Constraints

- Source code is split across multiple `.asm` files.
- Graphics and data use `.chr` and `.rle` assets.
- Audio uses DPCM `.bin` assets.
- The game manual provides high-level context, but the source code remains the authoritative source.

---

# Style Guidelines

- Prefer clear, concise technical writing over verbose explanations.
- Use Mermaid diagrams whenever they communicate structure or flow more effectively than plain text.    
- Explain concepts using modern software engineering terminology where appropriate.
- Preserve original terminology when required for accuracy.

---

# Knowledge Extraction Principles

1. Source code is the ground truth.
2. Every claim must be supported by evidence.
3. Separate observations from interpretations
4. Clearly distinguish verified facts, deductions, hypotheses, and unknowns.
5. Unknowns are valuable and must be documented.
6. Prefer refining existing knowledge over creating duplicate concepts.
7. Cross-reference related concepts instead of duplicating explanations.
8. Document relationships between code, data, memory, and runtime behavior.
9. Explain **why** a system exists, not only **how** it is implemented.
10. Focus on extracting transferable software engineering knowledge rather than assembly-specific details.


---

# Knowledge Hierarchy

Knowledge should generally progress from high-level concepts to implementation details.

```text
Architecture
    ↓
Systems
    ↓
Subsystems
    ↓
Modules
    ↓
Files
    ↓
Routines
    ↓
Data Structures
    ↓
Instruction-level Analysis
```

---

# Ingestion Workflow

1. Analyze the project structure.
2. Create or update the [project_map](docs/project_map).
3. Build sufficient understanding before documenting any concept.
4. Identify relationships between systems, modules, files, data, memory, and execution flow.
5. Create or update concept folders according to the OKF specification.
6. Create or update concept documents.
7. Update the [project_map](docs/project_map) with visited files, discovered concepts, and documentation status.
8. Update the knowledge base index.
9. Append an entry to the project log (newest entry first) containing:
    - Date
    - Files updated
    - Concepts added or modified
    - Summary of changes.

---

# Scope

## Include

The knowledge base should document:
- Overall software architecture
- Execution flow
- Game systems
- Memory organization
- Data structures
- Algorithms
- Graphics pipeline
- Audio pipeline
- Asset organization    
- Game mechanics
- Design patterns
- Hardware-specific implementation details where necessary to explain the software    

The objective is to explain how the game functions, not merely describe the source code.

## Exclude

The knowledge base should not focus on:
- Line-by-line assembly commentary unless required.
- Exhaustive opcode explanations.
- Repeating information already documented elsewhere.

---

# Documentation Priorities

1. Overall architecture
2. Execution flow
3. Memory map
4. Major systems
5. Data tables
6. Individual routines
7. Instruction-level analysis

---

# Document Versioning

- Every document shall specify the OKF version it follows.
- When the OKF specification changes, migrate existing documents to the new version rather than mixing document formats.

---

# Quality Checklist

Before completing any documentation update, verify that:

- No duplicate concepts have been created.
- Every significant claim has supporting evidence.
- Cross-references are valid.
- Mermaid diagrams render correctly.
- OKF metadata is complete.
- The project map has been updated.
- The knowledge index has been updated.
- The project log has been updated.
- Every new page is linked from at least one existing page.

---

# Knowledge Retrieval

When the user asks a question:

1. Read the [knowledge base index](docs/index) to locate relevant pages.
2. Read the relevant pages and synthesize an answer.
3. Cite the specific knowledge base pages used.
4. If the answer is not present in the knowledge base:
    - Clearly state that the knowledge base does not currently contain the answer.
    - If appropriate, analyze the source code to answer the question.
5. If the answer results in valuable new knowledge that is not already documented, offer to persist it as one or more OKF documents.

---

# Knowledge Base Maintenance

When the user asks to lint or audit the knowledge base:

- Check for contradictions between pages.
- Find orphan pages (pages with no inbound links).
- Identify concepts that are referenced but lack their own page.
- Flag claims that may be outdated based on newer evidence.
- Verify that every page conforms to the OKF specification.
- Report findings as a numbered list with suggested fixes.

---

# Documentation Rules

- Prefer creating or updating conceptual documentation before documenting implementation details.
- Implementation documents should support conceptual documents, not replace them.
- Avoid duplicating concepts. Prefer cross-references to existing documentation.
- When two concepts overlap, refine the existing documentation rather than creating parallel pages.

---

# Decision Priority

When multiple instructions conflict, resolve them in the following order:

1. Preserve factual accuracy.
2. Preserve evidence and traceability.
3. Follow the OKF specification.
4. Avoid duplication.
5. Improve readability.

---

# Target Audience

The knowledge base is intended for experienced software engineers who may have little or no knowledge of NES development or 6502 assembly.

Documents should assume familiarity with software architecture, algorithms, data structures, and game programming concepts while explaining hardware-specific behavior only when necessary to understand the implementation.