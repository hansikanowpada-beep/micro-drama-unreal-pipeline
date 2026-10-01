# Tutorial notes: UE5 environment building basics

Source: YouTube tutorial by **Amit** (channel: **Magnet**), captured from the
video transcript (shared as screenshots, not watched directly — so exact
button positions/labels should be double-checked against the live video,
but the sequence of operations below is accurate to the transcript).

Status: **partial capture** — covers through the start of placing
background assets. More chapters to be added as further transcript/screens
are shared.

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

## Placing background assets (partial — tutorial continues past this point)

- Drag a downloaded photorealistic background/mountain asset from the
  Content Drawer into the viewport.
- Select it, use the **red (X) axis** move handle to push it back into
  the distance behind the main scene.
- **Duplicate**: hold **Alt** and drag any axis handle to create a
  duplicate while moving it.
- Press **E** to switch to the Rotate tool, rotate duplicated copies for
  visual variation (avoids an obviously-repeated background).

---

*To extend: send more transcript/screenshots from later chapters of this
video (character placement, camera work, Sequencer, lighting polish,
rendering) and this file will be updated to cover the full workflow.*
