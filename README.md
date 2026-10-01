# Micro Drama Unreal Pipeline

A planning and design repository exploring an Unreal Engine workflow for
generating AI character animation videos. This is a companion to the
[Blender-based micro-drama pipeline](https://github.com/hansikanowpada-beep/micro-drama-3d-pipeline).
The two repositories are separate, parallel tracks—not replacements for each
other.

See [PIPELINE.md](PIPELINE.md) for the proposed tool-by-tool mapping.

## Contents

- `tutorials/` — step-by-step notes captured from UE5 tutorial videos
  (environment building, road/material blending, landscape/water/foliage,
  MetaHuman performance capture, and FPS game creation with Blueprints).
- `scripts/`, `scenes/`, `episodes/` — screenplay content broken down into
  the pipeline's scene format. See [SCENE_FORMAT.md](SCENE_FORMAT.md) for
  the schema and what's still open before any of it can actually be
  produced. First episode: "The Ocean of Time."

## Status

No Unreal-side automation has been built or tested yet — the engine
install/tool setup is in progress (see `tutorials/`). This repository
started as documentation only; scene-content planning has since begun
(see `SCENE_FORMAT.md`), and scripts will be added incrementally as each
tool is installed and verified, following the same approach used for the
Blender repository.
