# Unreal Pipeline Plan

This table describes a design plan. Most of the Unreal-specific
integrations and automation have not yet been verified through hands-on
testing — the one exception is noted below.

| Stage | Tool |
|---|---|
| Principal cast (photo→exact-likeness rigged character) | Headshot 3 + Character Creator 5, exported via CC5's built-in "Auto Setup" plugin, which transfers the character directly into Unreal with rig/materials intact. **iClone 8** (purchased, install pending) is being added alongside CC5 for animation/sequencing — CC5 builds the character, iClone animates it, per Reallusion's own CC↔iClone "Avatar" pipeline. |
| Motion | Mixamo FBX motion clips, retargeted via Unreal's built-in IK Retargeter, **or** iClone's own animation/motion tools once installed |
| Environment/buildings | Native Unreal/Fab marketplace asset packs, dropped directly into a level; see `scenes/the_ocean_of_time/ASSET_SOURCING.md` for the first episode's candidate packs. Buildify (Blender) is a procedural alternative — see `PLUGIN_ROADMAP.md`. |
| Lip-sync | **Leaning toward NVIDIA Audio2Face**, run inside NVIDIA Omniverse (USD Composer + Nucleus currently being installed) — still needs hands-on validation before being called final. Meta's OVRLipSync remains the fallback candidate if Audio2Face doesn't pan out. |
| USD hub (iClone/CC5 ↔ Unreal) | **New, unverified**: using NVIDIA Omniverse (USD Composer + Nucleus) as a USD-based exchange layer between iClone/CC5 and Unreal, instead of (or alongside) FBX export via CC5's Auto Setup. Goal: better fidelity for character/scene handoff. Exact workflow not yet established — see `PLUGIN_ROADMAP.md` for install status. |
| TTS/audio | Same as the Blender pipeline — Piper or Coqui TTS, engine-agnostic, produces a `.wav` file |
| Render | Unreal's Sequencer + Movie Render Queue, which supports command-line/headless batch rendering |
| Final assembly | ffmpeg — same as the Blender pipeline, engine-agnostic |
| Automation | Unreal's own Python API (`unreal` module, via Editor Scripting Utilities) + Movie Render Queue's command-line rendering. **`scripts_python/build_clinic_blockout.py` is the first script written against this API** (spawns a basic whitebox clinic room pair using Unreal's built-in Cube primitive) — still unverified hands-on, written from documented API only; update this note once it's actually been run successfully. |
