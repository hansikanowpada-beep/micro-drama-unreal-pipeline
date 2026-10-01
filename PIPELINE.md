# Unreal Pipeline Plan

This table describes a design plan. Most of the Unreal-specific
integrations and automation have not yet been verified through hands-on
testing — the one exception is noted below.

| Stage | Tool |
|---|---|
| Principal cast (photo→exact-likeness rigged character) | Headshot 3 + Character Creator 5, exported via CC5's built-in "Auto Setup" plugin, which transfers the character directly into Unreal with rig/materials intact |
| Motion | Mixamo FBX motion clips, retargeted via Unreal's built-in IK Retargeter |
| Environment/buildings | Native Unreal/Fab marketplace asset packs, dropped directly into a level; see `scenes/the_ocean_of_time/ASSET_SOURCING.md` for the first episode's candidate packs |
| Lip-sync | Not yet decided/tested — candidates are NVIDIA Audio2Face (free, audio→blendshape, exports to Unreal/MetaHuman) or Meta's OVRLipSync plugin (free, audio-driven viseme generation) — needs hands-on validation before committing to either |
| TTS/audio | Same as the Blender pipeline — Piper or Coqui TTS, engine-agnostic, produces a `.wav` file |
| Render | Unreal's Sequencer + Movie Render Queue, which supports command-line/headless batch rendering |
| Final assembly | ffmpeg — same as the Blender pipeline, engine-agnostic |
| Automation | Unreal's own Python API (`unreal` module, via Editor Scripting Utilities) + Movie Render Queue's command-line rendering. **`scripts_python/build_clinic_blockout.py` is the first script written against this API** (spawns a basic whitebox clinic room pair using Unreal's built-in Cube primitive) — still unverified hands-on, written from documented API only; update this note once it's actually been run successfully. |
