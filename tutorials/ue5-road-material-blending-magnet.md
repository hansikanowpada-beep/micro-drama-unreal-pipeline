# Tutorial notes: UE5 road creation and multi-layer blend materials

Source: a different YouTube tutorial, same channel as
`ue5-environment-basics-magnet.md` (creator name transcribed as "Omitage"
this time — likely the same "Amit"/Magnet channel, speech-to-text just
rendered the name differently). Captured from the video transcript
(screenshots, not watched directly) — double-check exact button labels
against the live video, but the operation sequence below is accurate to
the transcript.

This is a **separate** video from the character/cinematics one — this
one is specifically about building a custom road/ground surface using a
multi-layer blend material system, not character animation or Sequencer
work. Kept as its own file per the note at the end of the other one.

Status: **partial capture** — covers through building a debris pile
near ruined buildings (chapter 8, cut off mid-sentence). More to be
added as further transcript/screenshots are shared.

## Chapter 1: Introduction

- Creating an environment/ground scene in **Unreal Engine 5.8**.
- The finished map is available free via the creator's Patreon link (in
  the original video's description).

## Chapter 2: Scene setup and foundation

1. Launch Unreal Engine → **New Project** → **Games** category → select
   the **Third Person** template → name the project → **Create**.
2. **File → New Level → Empty Level → Create**.
3. Quick environment lighting setup via **Window → Environment Light
   Mixer** — this panel has one-click buttons to add each of:
   - **Create Skylight**
   - **Create Directional Light**
   - **Create Sky Atmosphere**
   - **Create Volumetric Cloud**
   - **Create Height Fog**

   (This is a faster path to the same base environment actors built
   manually one-by-one in the other tutorial's Chapter 3.)
4. In the Height Fog's settings (still in the Light Mixer or via its
   Details panel), enable **Volumetric Fog**, then close the Environment
   Light Mixer window.
5. **Landscape**: Selection Mode dropdown → **Landscape** → leave default
   settings → **Create** → switch back to **Select** mode.
6. **Scale reference**: Content Drawer → Characters folder → Manikins →
   Mesh folder → drag a mannequin mesh into the scene, to judge scale
   while building.
7. Move on to building a custom road (modeled directly, not an imported
   asset) — see Chapter 3.

## Chapter 3: Road creation and texturing

1. Selection Mode → **Modeling** → create a **Rectangle** primitive.
2. Increase its subdivisions for a denser, more deformable mesh:
   **Width Subdivisions = 200**, **Depth Subdivisions = 200** → **Accept**.
3. Back in Select mode, select the rectangle, right-click → **Browse to
   Asset** (locates/selects it in the Content Drawer).
4. **Enable Nanite** on it: right-click the asset → **Nanite** → **Enable
   Nanite**.
5. Press **R** (scale gizmo) to scale the rectangle up to road size,
   reposition (raise slightly off the landscape).
6. **Apply a blend master material** — the tutorial uses a free material
   called **"Unreal Senzi"**:
   - Download from **andrealengi.com → Resources** section → find the
     Unreal Senzi master material → enter name/email → a download link
     is emailed.
   - Open the downloaded content, copy all its folders.
   - In your Unreal project: Content Drawer → right-click the Content
     folder → **Show in Explorer** → paste the copied folders in.
   - Back in the project's **Materials** folder, you'll find 4 blend
     materials shipped with it. Right-click one → **Create Material
     Instance** (the tutorial calls this instance a "metal instance" —
     it's the Nanite-compatible instance of the blend master material).
   - Drag that material instance onto the road rectangle.
7. **Source road textures** from the **Fab marketplace** — the tutorial
   searches for and adds a material called **"Droid American Road"**
   (quality: High) → **Add to Project**.
8. Don't apply that downloaded road material directly — instead, open
   its own **Textures** folder and feed its individual texture maps into
   the Unreal Senzi blend material's **Material A** slot set:
   - Open the Unreal Senzi material, in the Details panel for **Material
     A**, enable the **Albido color**, **Roughness**, **Height**, and
     **Normal** texture-slot toggles.
   - Drag in: the Albido map → Albido slot, the Height map → Height
     slot, the Normal map → Normal slot, and the **OM map** (combined
     Occlusion/Roughness/Metallic) → the Roughness slot.
9. Save and close the material — Material A (the base road surface) is
   done.
10. **Save the level**: File → Save All → name it (e.g. "tutorial") →
    Save.
11. **Troubleshooting — displacement too strong**: the parallax/
    tessellation displacement effect looked too extreme on the finished
    road.
    - Fix: reopen the material asset, find the **Displacement Amount**
      parameter under the Material A settings, enable it, and lower the
      value (tutorial tries **0.5**).
    - This introduced a visible rendering artifact — fixed by nudging
      the Directional Light's position slightly (**Ctrl+L**, then move
      the mouse) — same control from the other tutorial's Chapter 3/9.
    - Displacement was then tuned back up a bit (to roughly **2–3**) for
      a better-looking result, and saved.

## Chapter 4: Material refinement and painting (partial — cuts off mid-sentence)

Goal: blend in "imperfection" layers (moss, concrete debris) on top of
the base road material, using the blend material's additional layer
slots plus vertex-color mesh painting to control where each shows.

1. Download two more Fab materials and **Add to Project**:
   - **"Mossy Concrete Wall"**
   - **"Military Trench Ground [Dirt]"** (transcript says "dart," almost
     certainly a mis-transcription of "dirt")
2. **Material B** (mix in the Mossy Concrete Wall textures):
   - Open the Mossy Concrete Wall asset's own folder → its High-quality
     subfolder → Material/Textures folder to find its maps.
   - Open the Unreal Senzi blend material, scroll up to find **"Second
     Metal Layer"**, enable it — this reveals the **Material B** slot
     set.
   - Enable all of Material B's texture-slot toggles (Albido, Height,
     Normal, Roughness).
   - Drag in: Albido map → Albido slot, Height map → Height slot, Normal
     map → Normal slot, OM map → Roughness slot (same pattern as
     Material A).
3. **Material C** (mix in the Military Trench Ground textures) — repeat
   the identical process:
   - Scroll up in the material, enable **"Third Material Layer"**.
   - From the Military Trench asset's High/textures folder, enable all
     Material C texture slots and drag in each map the same way.
4. Save and close the material.
5. **Paint the extra layers onto the road** using Unreal's built-in
   **Mesh Paint** mode (this is how you control *where* Material B/C
   show, versus the base Material A):
   - Select the road mesh, switch to **Mesh Paint** mode.
   - Under its options, go to **Texture Color** (vertex-color paint
     target), select the road asset, click the **+ / switch** button to
     add a paintable layer.
   - Open the **Paint** tool options.
   - **Deselect the Blue and Green color channels**, leaving only the
     **Red channel** active — the blend material reads the vertex
     color's channels to decide how much of each extra layer (B/C)
     shows at a given point, so painting in a specific channel targets a
     specific blend layer.
   - Set **Strength** to maximum (**1**).
   - Paint directly on the road mesh in the viewport to reveal the moss
     layer in chosen spots.
6. **Troubleshooting — displacement on the painted layer**: after
   painting, the layer's displacement looked too strong again. Fix,
   confirmed in the next batch:
   - Open the material, go down to the **B slot** (holds this "moss"
     layer — transcript renders it "MOS"), find **Displacement Amount**
     for B, enable it, decrease the value, save.
   - Nudge the Directional Light position again (**Ctrl+L**) to clear
     any resulting artifact, save.
7. **Painting the second extra layer (C / dirt)**: in Mesh Paint, select
   the **Green channel** and disable Red — painting now targets the
   other blended layer (Material C) instead of B. Paint it into
   different areas than the moss layer.
   - Same displacement issue showed up here too, plus the layer's tiling
     **size** looked too large: go to the **C material** section, enable
     **Displacement Amount C** and decrease it; enable **Size C** and
     increase it; fine-tune displacement again; save.
8. Resume painting the moss layer (reselect it) as needed to build up
   coverage.
9. **Erasing a mis-painted layer**: hold **Shift** while painting to
   erase/remove vertex-color paint instead of adding it.
10. Save settings, close the Mesh Paint window.

## Chapter 5: Detailing the road and pathways

1. **Extend the road**: go back to Select mode, select the road
   asset(s), increase their scale — use the mannequin (placed in Chapter
   2) as a visual scale reference, disabling snapping as needed while
   repositioning it to check proportions.
2. **Duplicate the road**: hold **Alt** and drag an axis handle, same
   duplicate pattern used throughout these tutorials.
3. Select both road pieces together for the next step.
4. **Troubleshooting — visibly repetitive tiling**: with the road
   extended, the same texture pattern was noticeably repeating. Fix via
   more Mesh Paint randomization:
   - Mesh Paint mode → select the road asset(s) → Paint tab → select the
     **Red channel** → paint some variation across the surface.
   - To paint a second asset/layer at the same time: click **Select**,
     choose the asset (double-click to select it), then also select an
     additional asset, and paint again — note that selecting multiple
     assets at once significantly increases the default brush size, so
     reduce brush size manually afterward.
5. **Puddles**: the blend material has a dedicated **Puddle Layer**
   feature:
   - Open the material, find **Puddle Layer**, enable and activate it.
   - Puddles are painted using the **Blue channel** in Mesh Paint (so
     between this and the earlier steps, the convention is: **Red** =
     primary variation/moss, **Green** = dirt/trench layer, **Blue** =
     puddles — each vertex-color channel drives a different blended
     feature).
   - Reduce brush size, then paint over low points/cracks to create
     wet-looking patches.
   - **Puddle properties** (back in the material, under the Puddle Layer
     group): **Liquid Opacity** controls how opaque/visible the water
     looks (increase for murkier water — the tutorial keeps it low for
     clear water); **Water Height** controls the puddle surface's
     height.
   - Save, close.
6. Switch back to Select mode — the road itself is finished. Next: foot
   paths alongside it.
7. **Foot paths**: sourced from a free **Quixel/Megascans** asset
   (transcript renders the brand name as "Quicksell," almost certainly a
   mis-transcription of "Quixel").
   - Add to Project.
   - In the Content Browser, enable the **Static Mesh** filter to narrow
     results (if no filter controls are visible, click the hamburger/
     three-line icon to reveal filter options first).
   - Drag a footpath piece into the scene.
   - Before rotating, enable **rotation snapping** and set the snap
     angle to **5°**, then rotate the piece to **90°**.
   - Increase its height as needed to sit correctly on the terrain.
   - **Re-material it**: go to the Fab-downloaded materials (Surfaces
     category — deselect the Static Mesh filter to see materials again)
     and apply the **Mossy Concrete** material (from Chapter 4) onto the
     footpath piece — blends it visually with the rest of the scene.
   - Duplicate footpath pieces (Alt+drag) to extend the path's length.

## Chapter 6: Building design and ruins

1. For building assets, the tutorial's preferred pack ("Ruin Modern
   Buildings") is explicitly **not a free asset** — noted as usable only
   if you already own it.
   - Free alternative: on Fab's home page, search **"broken buildings"**
     in the search bar — turns up a free broken-building asset pack.
     **Add to Project**.
2. After download: open the downloaded "Ruined Modern Buildings" folder,
   go to its **Assets → Mesh** subfolder, enable the **Static Mesh**
   filter to see just the building meshes.
3. Drag a building into the scene, rotate and reposition it to place it
   as a ruined structure within the environment.
4. Plan (stated, not yet executed at this point in the transcript): add
   ivy/climbing-plant assets and the same mossy textures onto the
   buildings for a more weathered/ruined look.
5. **Sourcing ivy/plant assets** — from a large asset pack the tutorial
   calls "Electric Dim Environment" (transcript's rendering of the name
   — treat as approximate, verify the actual pack title when sourcing
   it yourself). Notable because of the asset-transfer technique it
   demonstrates:
   - This pack downloads as its **own separate Unreal project**, not
     directly into your working project.
   - Open that separate downloaded project.
   - Inside it, navigate to an **"Assembly"** folder, enable the
     **Blueprint Class** filter to show just its Blueprint assets.
   - Select all of them.
   - Right-click → **Asset Actions → Migrate** — this is Unreal's
     built-in way to copy assets (with their dependencies) from one
     project into another.
   - When prompted, specify the destination: browse to your **actual
     working project's Content folder** and select it as the migration
     target.

6. After migrating, the **Assembly** folder appears in your actual
   project's Content Browser — enable the **Blueprint Class** filter
   there to see the migrated assets.
7. **Adding ivy to the building**: disable the Blueprint Class filter,
   browse down to a (also-migrated) **Mega Scans** folder, enable the
   **Static Mesh** filter — this shows all the Megascans-style meshes
   that came with the pack, including the ivy plants.
8. **Foliage-paint the ivy onto the building** (Unreal's Foliage system,
   same tool as the environment tutorial's Chapter 8, but here painting
   onto a building's walls rather than ground):
   - Switch to **Selection mode → Foliage**.
   - Select the ivy plant mesh(es), add to the foliage palette.
   - **Paint Density**: increase to maximum (**1**).
   - Brush size defaults too large when multiple assets are selected —
     decrease it.
   - With the ivy assets selected in the palette, go to their
     **Density** setting and increase it (tutorial sets **500**).
   - To allow painting on **vertical surfaces** (building walls, not
     just flat ground) find the **slope angle** setting and increase it
     to **180** — this is what permits foliage to also stick to steep/
     vertical faces instead of only near-flat ground.
   - Paint the ivy directly onto the building. If more density is
     wanted, increase it further (tutorial bumps it from 500 to **800**
     for denser coverage).
9. **Root assets**: back to Select mode, disable the Static Mesh filter,
   return to the **Assembly** folder, re-enable the **Blueprint Class**
   filter to find additional blueprint assets (root-system props) from
   the same migrated pack, to place around/under the building.
   - Place a root asset, increase its scale, then **Alt+drag duplicate**
     it randomly around the building a few times for natural variation.
10. Some pack assets are large, complex prefabs (lots of sub-meshes at
    once) — if one includes unwanted pieces (e.g. rocks, tree trunks,
    extra plants you don't want), **edit it directly**:
    - Select the asset → **Edit Blueprint** (double-click or the
      Details-panel button) → opens the Blueprint's Viewport tab.
    - Select and delete the unwanted sub-assets inside it (the tutorial
      removes rocks, trunks, and some plants, keeping just one piece).
    - **Compile**, close the blueprint — the placed instance in your
      level now reflects the trimmed-down version.
    - Reposition/rotate (90°) and place it, then Alt+drag-duplicate it
      multiple times to build up the design around the building.
11. **Re-material the building**: disable the Blueprint Class filter,
    go to the Fab-downloaded **Mega Scans → Surfaces** folder, apply the
    same **Mossy Concrete** material onto the building(s) by dragging it
    on — ties the building visually to the rest of the scene's materials.
12. **Package the whole set as a reusable Level Instance** — this is the
    key technique for not having to redo all the ivy/root/rubble
    dressing for every building:
    - Select the building together with its Foliage system: hold
      **Shift** and click the Foliage System entry in the Outliner to
      add it to the selection.
    - To select every related asset at once: in the **Outliner**, widen/
      expand the relevant area (drag its panel larger from the bottom),
      then **Ctrl+click** each individual asset to multi-select them all
      together (building, ivy foliage, roots, etc.).
    - With everything selected, right-click → **Level → Create Level
      Instance**, confirm.
    - Choose where to save it: create a new folder (e.g. **Levels**),
      and inside it a file for this specific building (e.g.
      **"BuildingOne"**).
    - The result is a single **Level Instance** asset in your Content
      Browser's Levels folder — dragging it into the scene drops in an
      exact copy of the whole dressed building (mesh + ivy + roots)
      in one step, instead of rebuilding the whole stack from scratch
      each time.

## Chapter 7: Scene assembly

1. For visual variety, build a few more **distinct** buildings (not just
   copies of the first) using the same full process from Chapter 6: pick
   a different building mesh from the Ruined Modern Buildings folder,
   foliage-paint ivy onto it, add roots/rubble, re-material it, then
   package it as its own Level Instance (e.g. saved as **"Building 2"**
   in the same Levels folder). Repeat for additional unique buildings —
   the tutorial ends up with **8 unique building Level Instances** built
   this way.
2. **Before** mass-duplicating buildings to fill the whole area, set up
   the main overview camera and a Level Sequence, so later framing can
   be checked against the actual laid-out scene:
   - Place Actors panel → **Cinematics** → **Cine Camera Actor**.
   - Sequencer tab → **Create Level Sequence**, name it (e.g. "tutorial
     sequence"), save.
   - Find the camera in the **Outliner**, drag it into the sequence.
   - Reposition the camera, then adjust:
     - **Focal Length**: decreased to **15** for a wide view covering
       the whole scene.
     - **Camera Component → Film Back**: preset changed to **16:9
       DSLR**.
     - **Exposure**: search "exposure" in the Details panel, find
       **Metering Mode** (under the Exposure group) and set it to
       **Manual**; increase **Exposure Compensation** (tutorial sets
       **10**) for a brighter overview shot.
     - Nudge the Directional Light position again (**Ctrl+L**) to taste.
     - Select the **Skylight** (via Outliner search), find **Intensity
       Scale**, increase it (tutorial sets **5**) for more ambient
       fill light across the whole scene.
     - Increase the camera's **Aperture** slightly as a baseline setting
       for this wide establishing shot.
3. **Fill out the scene** using the handful of unique Level Instance
   buildings: select one, **Alt+drag duplicate**, reposition and rotate
   each copy so repeated buildings don't look identical/uniformly
   aligned — repeat across the whole area, mixing which of the 8 unique
   buildings gets reused where.

## Chapter 8: Environmental debris (partial — cuts off mid-sentence)

1. **Rubble/debris props**: Content Browser → Ruined Modern Buildings
   folder → enable the **Static Mesh** filter → find rubble/debris
   meshes (shipped alongside the building meshes).
   - Place a rubble piece, press **R** (scale) and scale it down.
   - Re-material it to match: disable the Static Mesh filter, go back to
     **Fab folder → Mega Scans → Surfaces**, apply the same **Mossy**
     material used on the buildings, for visual consistency.
2. Pull additional rubble variety from the other building Level
   Instances already built: open one, enable the Static Mesh filter,
   pick another rubble piece from inside it, rotate and duplicate it out
   in the main scene.
3. Scale some rubble pieces down very small so they read as fine,
   scattered debris/"small particles" rather than large chunks.
4. Also bring in pieces from the separate **free "broken buildings"**
   pack downloaded earlier (Chapter 6) — scale down slightly, duplicate
   multiple times to scatter around.
5. **Building debris piles**: duplicate a building piece to reuse as
   rubble, rotate it to a broken-looking angle, duplicate again at a
   different rotation, and keep stacking/duplicating pieces near the
   base of buildings to build up a convincing debris pile, scaling
   individual pieces down as needed for the smaller fragments.

*Transcript cuts off mid-sentence here ("...so we can use this one. And
then we're going to decrease its scale. So...") — likely continues the
debris-piling process.*

---

*To extend: send more transcript/screenshots from later parts of this
video (finishing environmental debris, any further lighting, or final
export) and this file will be updated.*
