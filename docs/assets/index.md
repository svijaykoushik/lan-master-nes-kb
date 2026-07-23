# Assets & Graphics Subsystem

The **Assets & Graphics** subsystem handles the visual representation of *Lan Master* on the NES Picture Processing Unit (PPU). It includes compressed full-screen background graphics, NES hardware palette management (including color cycles and fade-in/fade-out transitions), and tile pattern indexing for network segments and UI text.

---

## Assembly Modules
* [Palette Management](palette.md) - Logic for managing NES color palettes, brightness tables, and screen transition fade effects.
* [RLE Decompressor](rle.md) - Decompression logic for expanding Run-Length Encoded background screens into PPU VRAM.

## References & Mappings
* [Pattern Mapping](pattern_mapping.md) - Mapping of internal logical tile IDs to PPU character pattern tile indices (`patterns.chr`).

