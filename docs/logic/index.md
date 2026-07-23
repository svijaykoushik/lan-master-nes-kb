# Game Logic Subsystem

The **Game Logic Subsystem** encompasses the core puzzle mechanics of *Lan Master*. It governs level layout unpacking, tile orientation and rotation algorithms, passcode generation/validation for stage select, and the Breadth-First Search (BFS) connectivity engine that checks network integrity.

---

## Assembly Modules
* [Connectivity Engine](tracemap.md) - Graph traversal logic (`traceMap`) with dual-wire crossing support and 2-bit `GAME_CHECK` visited bitmasks.
* [Level Definitions](levels.md) - 60-byte stage definition layouts, fixed-point score scaling (`GAME_TERM_FP`), and 3-bit packed grid data.
* [Level Unpacking & Initialization](level_generation.md) - Logic for unpacking level data into RAM, applying initial tile scrambling, and initializing terminal counts.
* [Password System](passwords.md) - 4-digit BCD passcode verification table mapping.

## Game Mechanics & Cheats
* [Hidden Main Menu Diagnostics & Secret Passcodes](cheats_diagnostics.md) - Secret `68xx` passcode entry mode for sound effect testing and level cheats.
* [Random Network Degradation Engine](network_degradation.md) - Active level $\ge 10$ tile rotation degradation mechanics over time.
* [Rotation Mechanics](rotation.md) - State rules for manual player tile rotations and random background tile rotations.

## References
* [Connectivity Rules](connectivity_rules.md) - Formal specification of tile pin bitmasks (`pinsTable`) and bidirectional connection validation.


