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
the start of a wind-enabled tree Blueprint (chapter 10, cut off
mid-setup). The MetaHuman-specific work (the video's actual stated goal)
hasn't been reached yet in the transcript. Chapters 3-4 (landscape
sculpting and the initial landscape material) are only partially
captured — picked up already in progress — note the gap below. More to
be added as further transcript/screenshots are shared.

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
   - Fix in progress: delete the placed tree instance. Instead of
     placing the mesh directly, create a reusable wrapper: Content
     Browser → right-click → **Blueprint Class → Actor**, name it (e.g.
     **"TreeOne"**).
   - Open the new Blueprint, make room in its graph/viewport area, click
     the **+ Add** button (to add a component) — the transcript cuts off
     here mid-setup of this Actor Blueprint wrapper, presumably about to
     add the tree's skeletal mesh component plus whatever drives its
     wind animation.

*Transcript cuts off mid-sentence here, inside the Blueprint editor
right after clicking "+ Add" — likely continues configuring the tree's
wind-animated Blueprint, then (per the video's stated goal) eventually
moves into actual MetaHuman creation.*

---

*To extend: send more transcript/screenshots from later parts of this
video (finishing the wind-tree Blueprint, and — the video's actual
title topic — creating/importing a MetaHuman, rigging, and animating
it) and this file will be updated.*
