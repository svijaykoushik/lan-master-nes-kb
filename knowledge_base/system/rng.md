---
type: Assembly Module
title: Random Number Generation (rand)
description: Implementation of a Galois Linear Feedback Shift Register (LFSR) for pseudo-random number generation.
resource: sources/Source/game.asm
tags: [system, logic, math, rng]
timestamp: 2026-07-03T11:45:00Z
---

# Random Number Generation

Lan Master uses a pseudo-random number generator (PRNG) to introduce variety into the game, specifically for level randomization and automatic tile rotations.

## The `rand` Routine

The game implements a simple 8-bit **Galois Linear Feedback Shift Register (LFSR)**. This is a common choice for 8-bit systems because it is extremely efficient to implement in assembly and provides a sufficiently uniform distribution for gameplay purposes.

### Implementation Logic

The `rand` routine operates on a single byte of state stored in `RAND_SEED` (`$fd` in Zero Page).

1. **Shift**: The current seed is shifted left by one bit (`asl a`).
2. **Feedback**:
   - If the shift resulted in a carry (meaning the most significant bit was 1), the seed is XORed with a fixed polynomial: `$cf` (`1100 1111` in binary).
   - If no carry occurred, the shifted value is kept as is.
3. **Update**: The new value is stored back into `RAND_SEED`.
4. **Output**: The resulting byte is returned in the accumulator.

### Properties
- **Period**: The generator has a period of $2^8 - 1 = 255$. It will cycle through all possible values from $1$ to $255$ before repeating.
- **Zero State**: If `RAND_SEED` ever becomes $0$, the generator will remain stuck at $0$ indefinitely. To prevent this, the game initializes `RAND_SEED` to $1$ during `initGame`.

## Use Cases in Lan Master

The RNG is used in several critical areas:
- **Level Unpacking**: During `unpackLevel`, the RNG determines the initial rotation of tiles to ensure every playthrough starts with a different configuration.
- **Random Rotations**: The `setRandomRotate` routine uses the RNG to pick a random tile and a random rotation amount to simulate network degradation.
- **Menu Animation**: The `mainMenuAnim` routine uses the RNG to toggle the display settings for visual dynamism.

# Citations
[1] [Source Code: game.asm](/sources/Source/game.asm)
