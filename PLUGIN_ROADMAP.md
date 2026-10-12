# Plugin/tool installation roadmap

Tools identified as needed across the Blender and Unreal pipelines for
"The Ocean of Time" and beyond, tracked here so they can be installed
one by one rather than losing track of what's pending. Each entry notes
which pipeline/application it actually belongs to — several tools
discussed in this project only run in one engine, not the other.

## Pending

### iClone 8 (Reallusion — animation/sequencing app)

- **Status**: purchased. Not yet installed.
- **What it is**: Reallusion's character animation/scene-sequencing
  application, the companion to Character Creator 5 in Reallusion's
  own "Avatar" pipeline — CC5 builds/sculpts the character, iClone
  animates and stages it. Has its own Unreal export path ("iClone Auto
  Setup," parallel to CC5's own Auto Setup plugin mentioned in
  `PIPELINE.md`) — not yet verified which one this project will
  actually use, or whether both get used for different purposes.
- **Open question**: exact division of labor between CC5's Auto Setup
  and iClone's own export/USD path once Omniverse is in the mix (see
  next entry) — don't assume one replaces the other until tested.

### NVIDIA Omniverse — USD Composer + Nucleus Workstation

- **Status**: downloaded (offline/Launcher-free package, extracted to
  a local `Composer` folder containing `create-2023.2.5`,
  `nucleus-workstation-2023.2.3`, a `launchComposerNucleus_run_on_...`
  batch file, and a `README`). Not yet installed/run.
- **Install step**: **follow that package's own `README` first** — it's
  the authoritative source for this specific offline installer, not
  guessed instructions. The batch file name suggests it sets up both
  Nucleus (the local asset-server/collaboration backend Omniverse apps
  sync through) and Composer (the USD scene-composition app) together.
- **What it's for in this project** (both confirmed goals):
  1. **NVIDIA Audio2Face for lip-sync** — runs as an Omniverse app/
     extension, generates facial animation from audio input. This is
     now the leading lip-sync candidate in `PIPELINE.md`, pending
     hands-on validation (including whether it needs retargeting setup
     for a custom CC5/iClone face vs. only working well on its stock
     example heads — unverified, needs testing).
  2. **USD hub connecting iClone/CC5 to Unreal** — using Omniverse's
     USD Connectors (Reallusion/Omniverse and Unreal both have them)
     as a higher-fidelity alternative to plain FBX export. Exact
     Connector names/versions needed, and whether they're separate
     downloads from Composer itself, are **not yet confirmed** —
     verify against NVIDIA's current Omniverse Exchange/app catalog
     once Composer is actually installed and running.
- **Caution**: this is a genuinely new, unverified part of the stack
  for this project — don't assume exact menu paths or Connector names
  without checking them live. Report back what the README/installer
  actually shows so these notes can be corrected against real behavior
  instead of guessed ahead of time.

### Buildify (Blender — Geometry Nodes add-on)

- **What it is**: a modular-building generator built on Blender's
  Geometry Nodes. Give it a flat base shape + a module kit (wall,
  pillar, roof, prop collections) and it procedurally instances modules
  to build a complete building — walls stretch/tile to fit the shape,
  pillars auto-place at corners (flat/concave/convex variants), roof
  props scatter via recursive subdivision, and floor count can be set
  per-building via a vertex group (`building:levels`, weight =
  floor-count ÷ 100).
- **Not an Unreal plugin** — it only runs inside Blender. Getting a
  Buildify building into Unreal needs an export step (below).
- **Companion add-on — BLOSM (Blender-OSM)**: a free third-party add-on
  by prochitecture that pulls real-world city layouts (building
  footprints, road data) from OpenStreetMap directly into Blender as
  base geometry for Buildify to build on — lets you snapshot a real
  city block instead of hand-modeling a footprint.
- **Requirements**: Blender **3.2.0+** (hard minimum — older versions
  lack required GN nodes); 3.3 "can be buggy sometimes" per the
  author's own docs.
- **Pricing**: not stated in the version-1.0 guide itself (BLOSM is
  confirmed free; Buildify's own price/source wasn't in this document —
  verify on whatever marketplace it's distributed through, e.g. Blender
  Market/Gumroad, before assuming it's free).
- **Relevance to this project**: directly solves several gaps flagged
  in `scenes/the_ocean_of_time/ASSET_SOURCING.md` — the Sharma Estate's
  exterior facade, the clinic building's exterior, and apartment
  building exteriors can all be generated procedurally instead of
  needing a purchased pack per location, once modular wall/pillar/roof
  kits are sourced (the tool ships temporary greybox modules; real
  modules — e.g. from Quixel Megascans — need to be dropped into
  matching collections per the "Replacing models" section of its docs).
- **Known limitations** (from the v1.0 docs): flat roofs only; one wall
  module size per building (no mixing e.g. a 4m and a 6m wall module in
  the same building yet); requires a perfectly flat base surface
  (tilted surfaces break it); overlapping edges in the base geometry
  flip wall orientation (workaround: offset the edges by ~0.00001m).

**Exporting a Buildify building into Unreal** (documented workaround,
not a direct pipeline — the author notes dedicated Altermesh/Meshsync
plugin support is still being tested as of this doc's writing):

1. Add a **Realize Instances** node at the end of the Buildify node
   tree (can take a while on large BLOSM-generated scenes).
2. With the mouse in the 3D viewport, **Ctrl+A → Visual Geometry to
   Mesh** — bakes the procedural result into a real, static mesh.
3. **UVs disappear after this conversion** (a current Blender
   limitation with Geometry Nodes). To restore them: Mesh Properties →
   **Attributes** → find the UV attribute (named `UVMap` by default,
   or whatever your source models used) → its dropdown → **Convert
   Attribute** → Mode: **UV Map**.
4. Export the resulting mesh as FBX, same as any other Blender-built
   asset in this project's pipeline (see
   `micro-drama-3d-pipeline/scripts_py/import_character.py` for the
   existing FBX-import pattern on the Unreal/Blender boundary, though
   that script is for characters specifically, not environment meshes).

## Already installed / in progress (cross-reference)

See the live step-by-step install history in this repo's `tutorials/`
files and the earlier conversation for Unreal Engine itself, the
Claude Code CLI + Nwiro Integration Kit connection, and the various
UE5 plugins enabled along the way (Movie Render Queue, Water, PCG,
Procedural Vegetation Editor — see
`tutorials/ue5-starter-course-unrealsensei.md` Chapter 6 for that
batch).

---

*Add new tools to the "Pending" section above as they come up, and
move an entry down once it's actually confirmed installed/working —
don't mark something installed from a plan alone.*
