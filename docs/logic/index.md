# Game Logic Subsystem

The **Game Logic Subsystem** encompasses the core puzzle mechanics of *Lan Master*. It governs level layout unpacking, tile orientation and rotation algorithms, passcode generation/validation for stage select, and the Breadth-First Search (BFS) connectivity engine that checks network integrity.

---

## Assembly Modules
* [Connectivity Engine](tracemap.md) - Graph traversal logic (`traceMap`) for checking node-to-node network connectivity and level completion.
* [Level Definitions](levels.md) - Layout definitions, terminal lists, and target time parameters for all 50 game stages.
* [Level Unpacking & Initialization](level_generation.md) - Logic for unpacking level data into RAM, applying initial tile scrambling, and initializing terminal counts.
* [Password System](passwords.md) - Logic for verifying and encoding 4-digit stage select passcodes.

## Game Mechanics
* [Rotation Mechanics](rotation.md) - State rules for manual player tile rotations and random background tile rotations.

## References
* [Connectivity Rules](connectivity_rules.md) - Formal specification of tile pin bitmasks (`pinsTable`) and bidirectional connection validation.

