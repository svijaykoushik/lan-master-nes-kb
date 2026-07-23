# Audio Subsystem

The **Audio Subsystem** manages music playback and sound effects during gameplay, menus, timeouts, and victory screens. It uses a customized version of the **FamiTone** audio engine, supporting standard NES APU pulse/triangle/noise channels as well as DPCM sampled percussion effects.

---

## Assembly Modules
* [Dual-Channel SFX Priority Scheme](sfx_priority.md) - Channel assignment logic isolating `SFX_TIME` countdown ticks on `FT_SFX_CH1`.
* [FamiTone Engine](famitone.md) - Implementation of the FamiTone audio driver used for BGM playback and sound effect dispatching.

## Catalogs & References
* [Audio Catalog](audio_catalog.md) - Catalog mapping sound effect IDs and background music tracks (`bgm_title`, `bgm_game`, `bgm_done`, `bgm_timeout`) to game events.


