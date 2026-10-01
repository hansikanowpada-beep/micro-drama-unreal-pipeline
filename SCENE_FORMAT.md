# Scene content format

This repository was documentation-only until the `the_ocean_of_time`
episode was added. That episode's `scenes/*.json` files establish a
**new, proposed scene-definition format** for this pipeline — modeled
loosely on the working format already used by the Blender pipeline
(`micro-drama-3d-pipeline/scenes/*.json`, e.g. shared `camera` preset
names: `close_up` / `medium_shot` / `wide_shot`) for consistency across
the two parallel pipelines.

**Important — this format is not yet backed by any automation.** Unlike
the Blender pipeline's `render_scene.py` (which actually reads scene
JSON and drives Blender), nothing in this repo currently reads these
files or drives Unreal from them. They're a structured content
breakdown — useful for planning shots, casting, and asset needs — not
a working pipeline yet. Building the actual Unreal-side automation
(Python API / Sequencer scripting per `PIPELINE.md`) is still open work.

## Layout

- `scripts/<episode_id>/script.md` — the original screenplay/script, kept
  as the source of truth the scene breakdown was derived from.
- `scenes/<episode_id>/<scene_id>.json` — one file per scene (see schema
  below).
- `episodes/<episode_id>.json` — ordered list of scene files, plus the
  episode's character and location roster.

## Scene JSON schema

| Field | Type | Notes |
|---|---|---|
| `scene_id` | string | `<episode_prefix>_sc<NN>_<slug>` |
| `episode` | string | matches the episode's `episode_id` |
| `int_ext` | string | `"INT"` or `"EXT"` |
| `location` | string | as written in the script's slugline |
| `time_of_day` | string | `DAY` / `NIGHT` / `DAWN` / `CONTINUOUS` / etc. |
| `characters` | array | `{cast_id, role, age}` — `cast_id` is a placeholder until a real character asset exists for them (see "Open work" below) |
| `camera` | string | primary camera preset for the scene: `close_up` / `medium_shot` / `wide_shot` (same names as the Blender pipeline) |
| `lighting_notes` | string | free-text guidance tying the scene's mood to actual Unreal lighting controls documented in `tutorials/` (Directional Light intensity/Source Angle, Post Process exposure/grading, etc.) |
| `action` | string | stage direction / blocking, condensed from the script |
| `dialogue` | array | `{character, parenthetical, line}` in script order |
| `narration` | array | `{line}` — for V.O. narration scenes |
| `duration_estimate_seconds` | number | rough pacing estimate, not a hard target |
| `shot_list` | array (optional) | `{camera, description}` — used when a scene needs more than one camera setup/coverage |
| `continuity_notes` | string | callbacks, reused locations, props that need to read clearly, sensitive-content handling notes, etc. |

## Open work before any of this can actually be produced

1. **No character assets exist yet** for any of the six `cast_id`
   placeholders (`ananya`, `rohit`, `mr_sharma`, `mrs_sharma`, `doctor`,
   `priya`). Per `PIPELINE.md`, the planned route is Headshot 3 +
   Character Creator 5 (if a specific likeness is wanted) or MetaHuman
   Creator (per the workflow partially documented in
   `tutorials/ue5-metahuman-performance-capture-magnet.md`) for
   original characters with no specific real-world likeness.
2. **No environment assets sourced yet** for the six locations (Sharma
   Estate exterior/living room/study, Wedding Mandap, the apartment, the
   downtown cafe, the clinic, the barren coastline). These would need
   Fab/Megascans asset packs per the techniques already documented in
   `tutorials/ue5-road-material-blending-magnet.md` and
   `tutorials/ue5-starter-course-unrealsensei.md`.
3. **No automation reads these scene files yet** — no Sequencer-building
   script, no TTS/audio pipeline wired up, no render/export step. This
   is planning content only.
