# Tutorial notes: UE5.8 Starter Course (landscape/water/trees → MetaHuman)

Source: **"Unreal Engine 5.8 Beginner Tutorial - UE5 Starter Course
2026"** by **Magnet VFX** (creator credited as "Amit" in on-screen links
— Instagram/Facebook/YouTube handles `amit.gcts`/`amitdasfilms` — the
transcript's speech-to-text renders the spoken name as "Omit"; same
channel as the other two tutorial-notes files in this repo). Published
~1 month before capture, 22K+ views. Captured from the video transcript
(screenshots, not watched directly) — double-check exact button labels
against the live video.

This is a **third, separate** video from the same channel — a broader
"starter course" than the title first suggested: it builds a full
landscape/water/foliage environment from scratch (general UE5
fundamentals, distinct from both the environment-basics tutorial and the
road/material-blending one in this repo) before getting to its stated
goal of a MetaHuman character animation. Kept as its own file.

Status: **partial capture** — covers landscape/water/tree setup through
a full PCG-based procedural tree-scattering workflow (chapter 11). The
MetaHuman-specific work (the video's actual stated goal) hasn't been
reached yet in the transcript. Chapters 3-4 (landscape sculpting and the
initial landscape material) are only partially captured — picked up
already in progress — note the gap below. More to be added as further
transcript/screenshots are shared.

## Chapter 1: Project introduction

- Standard channel intro/sign-off boilerplate (subscribe plea, member
  shoutout) — no technical content.
- Goal stated: create a MetaHuman animation inside Unreal Engine 5.8.

## Chapter 2: MetaHuman setup

1. **Before launching the engine**: in the **Epic Games Launcher**, go to
   the installed Unreal Engine version's **Options**, and enable
   **"MetaHuman Creator (Code & Data)"**, then click **Apply**.
   - This downloads an additional **~33GB** of data required for
     MetaHuman support — expect a significant wait depending on
     connection speed, and make sure there's enough free disk space
     before starting it.
2. Launch Unreal Engine.
3. **New Project** → **Games** category → select the **Third Person**
   template → name the project (tutorial uses "tutorial").

## Chapters 3-4: Landscape creation and base material (gap — picked up in progress)

Not captured in detail — these chapters (between project creation and
the visible Chapter 5 heading) covered creating the base landscape and
downloading/applying its first material, based on what's visible right
as Chapter 4 ends:

- Downloaded a landscape material called **"Mossy Rocky Ground"** from
  Fab (High quality), Add to Project.
- After download: opened its Materials folder, found the material.
- Applied it to the landscape: select the landscape → Details panel →
  **Landscape Material** slot → drag the material in.
- Added a **mannequin** to the scene for scale reference: Content
  Browser → Characters → Mannequins → Mesh folder → drag into the scene
  (same scale-reference technique as the road/material tutorial).

## Chapter 5: Nanite and displacement

1. **Enable Nanite on the landscape**: select the landscape → Details
   panel → find **Nanite** → enable it → click **Rebuild Data**.
2. Open the landscape material (double-click).
3. **Tiling**: enable, decrease the value (tutorial sets **2**) so the
   landscape texture doesn't look obviously repetitive.
4. **Enable Tessellation**.
5. **Displacement Scaling**: decrease the magnitude — tutorial compares
   **1** (more pronounced) vs **0.5** (preferred, subtler) and settles
   on **0.5** for a natural-looking subtle displacement.
6. Save, close the material.

## Chapter 6: Plugin and project settings

1. **Enable the Water plugin**: Edit → Plugins → search "water" →
   enable **"Water"** (confirm the restart-required prompt with
   **Yes**), also enable **"Water Extras"** (confirm **Yes**).
2. **Enable PCG (Procedural Content Generation) plugins**: search "PCG"
   → enable **"Procedural Content Generation Framework"** (confirm
   **Yes**), then search and enable **"Procedural Vegetation Editor"**
   (confirm **Yes**).
3. **Enable Movie Render Queue** + **Movie Render Queue Additional
   Render Passes** (confirm **Yes**) — same rendering plugin used in the
   other two tutorials, enabled early here rather than at the end.
4. Close the Plugins window.
5. **Edit → Project Settings** → search "nanite" → enable **"Nanite
   Foliage"**.
6. **Restart the engine** — required after this batch of plugin/setting
   changes. Save your level/progress first.
7. After restart: close Project Settings, reopen your level (Content →
   open the level), and **re-enable Nanite for the landscape** (the
   restart appears to require re-confirming this setting).

## Chapter 7: River system construction

1. Place Actors panel (box icon) → search "water" → find **Water Body
   River**, drag it into the scene.
2. Click **Complete** to finish the initial spline placement.
3. **Shape the river's path** using its spline:
   - Select the spline/plan system, press **E** (rotate) to orient it.
   - Select an individual spline (line) point, press **W** (move) to
     reposition it; repeat for other points to carve the river's route.
   - **Extending the spline** with more points: select the last spline
     point, switch its coordinate option to **Local** coordinate space,
     then hold **Alt** and drag an axis handle — this adds a new spline
     point while dragging (the spline equivalent of Alt-drag object
     duplication used throughout these tutorials).
4. Rebuild Nanite data again after reshaping the landscape/river.
5. Bring the mannequin back into frame (via Outliner search) to check
   scale as the river takes shape.
6. **Narrowing the river**: select the Water Body River actor → select
   its spline system → use the "select all spline points" option →
   under its **Water** settings, find **River Width** → decrease it
   (tutorial sets roughly **1000**) — narrows the entire river's width
   in one step rather than adjusting each point individually.

## Chapter 8: Shallow water simulation

1. Add a **Shallow Water River** actor (search "water" in Place Actors)
   — a separate water-body type that drives realistic shallow-water
   interaction/reflection rather than the river's bulk water volume.
2. Select it → Details panel → **Water** section → **Source River Water
   Body** field → click **+** → choose your main Water Body River asset
   from the dropdown, linking the shallow-water effect to the actual
   river you built.
3. Click **Reset** to apply the settings cleanly.
4. **Bake the simulation**: via the relevant dropdown menu, select
   **Water Component → Bake Sim**.

## Chapter 9: Material refinement

1. Re-enable Nanite again (a recurring step after scene changes in this
   tutorial).
2. **Troubleshooting — rendering artifacts**: if visible, nudge the
   Directional Light position (**Ctrl+L**) to resolve them.
3. **Troubleshooting — specular highlight too strong on the landscape**:
   select the landscape → Details panel → open the landscape material
   (double-click) → find **Specular**, enable it, decrease the value
   (tutorial tries **2**, then settles on **0.1**) → save, close.

## Chapter 10: Tree asset setup (partial — cuts off mid-setup)

1. Download tree assets from Fab — the tutorial uses a pack called
   **"Mega Plant Black Elder"**, Add to Project.
2. After download: open its "Tree Black Elder" folder to find the tree
   meshes.
3. **Filter tip**: click the hamburger/three-line filter icon in the
   Content Browser and enable the **Skeletal Mesh** filter — these tree
   assets are skeletal meshes (not static), presumably so they can be
   vertex/bone-animated for wind sway.
4. Drag one tree onto the landscape.
5. **Troubleshooting — tree looks completely static, no wind movement**:
   - Fix: delete the placed tree instance. Instead of placing the mesh
     directly, create a reusable wrapper: Content Browser → right-click
     → **Blueprint Class → Actor**, name it (e.g. **"TreeOne"**).
   - Open the new Blueprint, make room in its graph/viewport area, click
     **+ Add** (to add a component), search **"skinned"**, select
     **Instance Skinned Mesh**.
   - In its Details panel, expand the **Skeletal Asset** panel and
     assign the tree's skeletal mesh.
   - Find the **Transform Provider** dropdown — empty by default, no
     options available yet.
   - To populate it: click the **Settings** icon (in the component
     picker/search area) and enable **"Engine Content"** (shows engine-
     internal content normally hidden from the project browser).
   - Now a **Wind Transform Provider** option appears in the dropdown —
     select it.
   - Scroll down to an **Instance** option, click **+** to add one.
   - **Compile**, close the Blueprint.
6. In the Content Browser, enable the **Blueprint Class** filter, find
   the new **Tree** blueprint ("TreeOne"), drag it into the scene, press
   **G** (Game View) to check — the wind effect is now visible, moving
   the tree naturally.
7. **Controlling wind speed globally**: this per-tree setup doesn't
   directly expose a wind-speed slider — instead:
   - Clear filters (disable Blueprint Class/Skeletal Mesh), enable
     **Engine Content** again (Settings icon), search **"global"**, find
     **Global Foliage Actor**, drag it into the scene.
   - Placing this actor **immediately stops the wind effect** on the
     tree (it appears to take over wind control from the per-instance
     provider).
   - To bring wind back and make it adjustable: select the **Global
     Foliage Actor** (via Outliner), Details panel → **Wind Speed** →
     increase the value (tutorial tries **10**, then **15**) — this is
     the actual control for overall wind strength across all
     wind-enabled trees in the level.
8. **Creating tree variety** (reusing the same wind-enabled wrapper for
   different tree meshes, rather than rebuilding the Blueprint each
   time):
   - Clear the search, browse back to the Mega Plant Black Elder tree
     folder, enable both Skeletal Mesh and Blueprint Class filters.
   - Select the **TreeOne** blueprint, **Ctrl+D** to duplicate it —
     auto-named "Tree 2". Open it.
   - Select its **Skinned Mesh** component, in the Details panel swap
     the **Skeletal Mesh** reference to a different tree variant from
     the pack. **Compile**.
   - Repeat (duplicate again, swap the mesh) for additional variants —
     tutorial ends up with **4 unique wind-enabled tree Blueprints**.
   - Scatter these varied blueprints around the scene manually at this
     stage.
9. **Troubleshooting — some tree trunks render transparent/with visual
   artifacts**: select the affected tree assets → right-click → **Asset
   Actions → Edit Selection in [a batch Nanite settings editor]** →
   **Mesh → Nanite settings** → find **Shape Preservation**, currently
   set to **Voxalize** → change it to **Preserve Area** instead → fixes
   the transparency artifact. Save, close.

## Chapter 11: PCG foliage scattering

A more scalable alternative to manually placing each tree: Unreal's
**Procedural Content Generation (PCG)** framework scatters the
wind-enabled tree Blueprints automatically across a hand-drawn area,
with built-in randomization — genuinely different from the Foliage-tool
painting approach used in the other two tutorials in this repo.

1. Deselect everything (click an empty area / collapse the level in the
   Outliner first to be safe).
2. Selection mode → **PCG** → **Draw Spline Surface** tool.
3. Draw a spline outlining the area where trees should scatter.
4. **Spawning settings**: since this scatters Blueprint actors (not
   plain static meshes), enable and activate **"Spawn Actor"**.
5. Under **Actor Classes**, click **+**, add the **TreeOne** blueprint
   as a class to spawn.
6. **Troubleshooting — density far too high**: under the **Sampling**
   tab, enable **"Points Per Square Meter"**, set it to **0.3** —
   brings the tree count down to something reasonable.
7. Add a second tree variant to the mix: Actor Classes → **+** → add
   another tree blueprint (e.g. "Tree 4").
8. Lower density further if needed (tutorial settles around **0.2**).
9. Click **Accept**, return to Selection mode.
10. **Troubleshooting — trees sit at odd angles, not aligned to the
    ground**: under the PCG component's **Parameter Overrides → Global
    Transform**, enable **"Absolute Global Rotation"** — fixes trees
    rotating to follow terrain slope unpredictably instead of standing
    upright.
11. Select the PCG actor, press **G** to preview the result in Game
    View.
12. **Extending the covered area**: select a spline point, switch its
    **Coordinate** setting to **World** coordinates, then reposition/add
    points to grow the area (same local-vs-world coordinate distinction
    used for the river spline in Chapter 7).
13. **Troubleshooting — trees floating above the ground in newly
    extended areas**: this needs an actual fix inside the **PCG graph**
    itself (not just the spline/component settings):
    - Select the PCG Tool component, open its **PCG Graph** (double-
      click).
    - In the **Projection** tab, right-click → search **"Get Landscape
      Data"** → add that node.
    - Connect its output to the **Projection Target** input. Save,
      close.
    - Back in the component's **Projection** settings (Details panel),
      expand **Projection**, enable **"Snap to Surface"** — trees now
      correctly snap onto the ground even in freshly extended spline
      areas, and live-update as the spline changes (moving a point
      re-snaps affected trees automatically; deleting a spline point
      shrinks the covered area).
14. **Adding placement randomization** (on the PCG Tool component,
    Details panel):
    - **"Edge Followup Scale Minimum"** — enable, decrease the value
      (reduces trees clustering right at the spline edge).
    - **Random Transform** section — enable all its sub-options:
      - **Random Position Offset** Min: X = **-100**, Y = **-100**; Max:
        X = **100**, Y = **100**.
      - **Random Rotation** (Z axis): Min = **-360**, Max = **360** —
        full random rotation around the vertical axis.
      - **Scale randomization**: Min = **0.8**, Max = **1.2** (read from
        a transcript line saying "8 to the minimum and 1.2 to the
        maximum" — almost certainly "0.8", since an 8x minimum scale
        alongside a 1.2x maximum wouldn't make sense; verify against the
        live video).
15. **Scattering a second area with the same settings**: select the PCG
    actor (renamed "PCG Tree" at this point), duplicate it (Ctrl+D or
    Edit → Duplicate) rather than configuring a new one from scratch —
    the duplicate carries over all the density/randomization settings
    already dialed in. Selection mode → **PCG → Draw Spline Surface**
    again (the duplicate, e.g. "PCG Tree 2", is auto-selected) → draw a
    new spline area elsewhere in the scene → Accept → back to Selection
    mode. Same tree variety and randomization now applies to this new
    area without re-entering any settings.

---

*To extend: send more transcript/screenshots from later parts of this
video (further scene dressing, and — the video's actual title topic —
creating/importing a MetaHuman, rigging, and animating it) and this file
will be updated.*
