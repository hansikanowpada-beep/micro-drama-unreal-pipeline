# Plugin/tool installation roadmap

Tools identified as needed across the Blender and Unreal pipelines for
"The Ocean of Time" and beyond, tracked here so they can be installed
one by one rather than losing track of what's pending. Each entry notes
which pipeline/application it actually belongs to — several tools
discussed in this project only run in one engine, not the other.

## Pending

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
