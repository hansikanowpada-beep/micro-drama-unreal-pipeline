# Tutorial notes: UE5 environment building basics

Source: YouTube tutorial by **Amit** (channel: **Magnet**), captured from the
video transcript (shared as screenshots, not watched directly — so exact
button positions/labels should be double-checked against the live video,
but the sequence of operations below is accurate to the transcript).

Status: **partial capture** — covers through foliage painting (chapter 8
of 8+). More chapters to be added as further transcript/screenshots are
shared.

## Chapter 1: Introduction

- Creator's first Unreal Engine tutorial (their other content is mostly
  Element 3D).

## Chapter 2: Acquiring project assets (all free)

Two free asset sources used:

**A. Megascans via Quixel Bridge**
1. In the Content Drawer, select the Content folder, right-click →
   "Add Quixel Content" (requires the Quixel Bridge plugin/bridge to be
   installed — shows up as an option if installed).
2. This opens the Quixel Bridge. Pick an asset category (the example uses
   tundra/ground-plane assets).
3. Choose quality — the tutorial picks **Nanite**.
4. Click Download, wait for it to finish, then click **Add** to import
   into the open Unreal project.
5. A confirmation window appears once the model is successfully imported.

**B. Epic Marketplace free content**
1. In the Epic Games Launcher → Unreal Engine tab → Marketplace.
2. Browse → filter to Epic/free content.
3. Pick an asset (the tutorial uses a free character model, a
   "photorealistic background" landscape asset, and a house-models pack
   that was free-for-the-month at time of recording — free-for-the-month
   items won't always be available, check current Marketplace/Fab free
   offers).
4. Click the asset → **Add to Project** → select the target project →
   confirm.

## Chapter 3: Building the environment

Starting from a fresh empty level (File → New Level → Empty Level →
Create):

1. **Directional Light** (the sun)
   - Add via the Place Actors panel (+ icon).
   - Select it, open the Details panel, set **Mobility: Movable**.
   - In the Details panel search box, type "atmos" and enable
     **Atmosphere Sun Light**.

2. **Sky Light**
   - Add a Sky Light (Light category) — provides indirect/bounce light
     from the sky.
   - Set **Mobility: Movable**.
   - Enable **Real Time Capture**.

3. **Sky Atmosphere**
   - Add via Visual Effects → Sky Atmosphere. Renders the sky/sun visibly.

4. **Volumetric Cloud**
   - Add via Visual Effects → Volumetric Cloud. Generates cloud cover.

5. **Exponential Height Fog**
   - Add via Visual Effects → Exponential Height Fog.
   - In its Details panel, scroll to the Volumetric Fog section and
     enable it.

6. **Post Process Volume** (controls exposure globally)
   - Add via Visual Effects → Post Process Volume.
   - By default a post-process volume only affects the inside of its own
     bounding box — search the Details panel for "infinite" and enable
     **Infinite Extent (Unbound)** so it affects the whole level.
   - Search for "exposure" → check the box to enable manual exposure
     control → set **Min Brightness** and **Max Brightness** both to the
     same value (the tutorial uses 1) to lock exposure instead of letting
     it auto-adjust.

7. **Fine-tune the sun**
   - Select the Directional Light → lower **Intensity** if too bright
     (tutorial sets it to 5).
   - Increase **Source Angle** to make the sun's visible disc larger.
   - Tip: hold **Ctrl+L** and move the mouse to interactively
     rotate/reposition the directional light (time-of-day style control).

## Chapter 4: Creating the landscape

1. Switch the Select Mode dropdown (top-left of viewport) to
   **Landscape** mode.
2. Use the default flat-plane settings (no sculpting yet) and click
   **Create** to generate a flat landscape surface.
3. Switch back to the normal Select mode.

Recap at this point in the tutorial: Directional Light (sun) →
Exponential Height Fog → Post Process Volume (exposure + fog interaction)
→ Sky Atmosphere (visible sky) → Volumetric Cloud → Sky Light (indirect
sky light) → flat Landscape. That's the full base environment before any
set-dressing.

## Chapter 5: Placing environmental assets

**Transform tool hotkeys** (standard Unreal defaults, confirmed in this
tutorial):
- **W** — Move/Translate gizmo
- **E** — Rotate gizmo
- **R** — Scale gizmo
- **Alt + drag** an axis handle — duplicate the selected object while
  moving it

**Background mountain asset**:
- Drag the downloaded photorealistic background/mountain asset from the
  Content Drawer into the viewport.
- Select it, use the **red (X) axis** move handle to push it back into
  the distance behind the main scene.
- Alt+drag to duplicate, rotate (E) each duplicate for visual variation,
  nudge copies closer/further to vary the silhouette and avoid an
  obviously-repeated background.

**Viewport fly-camera navigation** (for moving around the large
imported ground-surface model to position it):
- Hold the **right mouse button** to enable fly-camera look, then:
  - **W / A / S / D** — move forward / left / back / right (same scheme
    as a standard first-person game)
  - **E** — move up (while right-click is held)
  - **Q** — move down (while right-click is held)
- Camera fly speed is adjustable via the speed control in the viewport
  toolbar — click it and set a value (the tutorial settles on ~4, after
  trying 6 as too fast).
- Use the **blue (Z) axis** handle to drop a large ground-surface model
  down onto the landscape. Once this large Megascan surface is placed,
  no further landscape sculpting is needed — it visually covers the flat
  landscape created in Chapter 4.

## Chapter 6: Designing the scene layout

- Drag Megascan/marketplace models into the scene, rotate (E) and
  Alt+drag-duplicate to build up a layout — the tutorial stresses this
  step has no fixed formula, just iterative placement to taste.
- Adjust camera fly speed as needed per the navigation controls above
  (lower = finer control while placing objects close together).
- Keep adding background-filling objects (e.g. stone models) to avoid
  empty gaps.
- **Uniform scaling**: in the Details panel's Scale XYZ fields there's a
  lock toggle next to the scale values — enable it so increasing one
  axis scales all three proportionally, instead of stretching the mesh.

## Chapter 7: Refining the ground surface

- A single large ground-surface mesh can look low-resolution/blurry up
  close — fix by layering additional smaller surface/ground-plane meshes
  on top to add visual detail where the camera gets close.
- Scale these surface pieces up only modestly — over-scaling drops
  texture resolution visibly (textures stretch and blur).
- Rotate (E) and Alt+drag-duplicate multiple ground-plane pieces to
  fully cover the field, raising pieces slightly where needed so they
  blend with the terrain's bends/slopes, and filling any visible gaps
  between pieces.

## Chapter 8: Adding foliage and details

- Place small rock models at the seams between ground-plane pieces to
  help blend them together visually.
- **Foliage painting** (Unreal's built-in Foliage mode):
  1. Switch to **Foliage** mode (Modes panel).
  2. Find foliage meshes (e.g. grass) in the Content Browser — tip: use
     the Content Browser's **Filters → Static Meshes** filter to narrow
     a large asset-pack folder down to just static meshes, since
     foliage instances need a static mesh, not a Blueprint.
  3. Drag the chosen mesh(es) (e.g. two grass variants) into the Foliage
     mode's mesh list — multiple meshes can be active at once for
     variety when painting.
  4. Per-mesh paint settings (selected in the Foliage mesh list):
     - **Brush size** — radius of the paint brush (set via the Paint/Pen
       tool's brush-size control).
     - **Density** — a per-instance density value (default in the
       tutorial's example was 100); increasing it (e.g. to 500)
       produces much denser foliage coverage per paint stroke. Note:
       there's also a separate 0–1 "density" slider for how much of a
       single click fills in — the tutorial raises the per-mesh density
       count (100 → 500) rather than relying on that slider alone when
       stroke coverage looked too sparse.
  5. Hold the paint/brush mouse button and drag over the ground to paint
     foliage instances; use the same right-click fly-camera navigation
     from Chapter 5 to reposition the view while painting larger areas.

---

*To extend: send more transcript/screenshots from later chapters of this
video (character placement, camera work, Sequencer, lighting polish,
rendering) and this file will be updated to cover the full workflow.*
