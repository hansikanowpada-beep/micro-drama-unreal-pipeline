# Tutorial notes: UE5 environment building basics

Source: YouTube tutorial by **Amit** (channel: **Magnet**), captured from the
video transcript (shared as screenshots, not watched directly — so exact
button positions/labels should be double-checked against the live video,
but the sequence of operations below is accurate to the transcript).

Status: **partial capture** — covers through the start of keyframing
character movement in Sequencer (chapter 13, cut off mid-explanation).
More chapters to be added as further transcript/screenshots are shared.

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

- Foliage also catches on cliff/rock Megascan surfaces — these models are
  pre-programmed so that only their "foliage-enabled" (green-marked)
  faces catch painted foliage, not every surface (e.g. not bare rock
  faces) — this is automatic, nothing extra to configure.
- Keep filling empty-looking areas with duplicated rock models as needed.

## Chapter 9: Final lighting adjustments

- Hold **Ctrl+L** and move the mouse to reposition the sun to a more
  deliberate angle (the tutorial aims for a dusk-like look) now that the
  full environment is in place — same control introduced in Chapter 3,
  now used for creative framing rather than just brightness.

## Chapter 10: Cinematic camera setup

1. Place Actors panel → **Cinematics** category → **Cine Camera Actor**.
2. Select the camera and switch the viewport to look through its lens
   (the viewport's camera/perspective dropdown lets you pick a placed
   camera to preview through — i.e. "pilot" that camera).
3. **Framing**:
   - Camera's **Film Back** setting → set to **16:9 DSLR** (aspect-ratio
     preset) if the default crop looks off.
   - If still too zoomed in, change the **Lens** to a wider prime —
     tutorial uses a **12mm prime lens** for a wide-angle look.
4. **Camera lens effects** (Details panel → Lens/Post Process section,
   same camera actor):
   - **Bloom** — enable, set method to **Standard/Conventional**, adjust
     **Intensity** to taste.
   - **Chromatic Aberration** — enable, set **Intensity**; also raise
     **Start Offset** so the aberration only shows near the frame edges,
     not across the whole image (closer to a real lens).
   - **Lens Flare** — enable, set **Intensity** (tutorial lowers it to
     ~0.5 when too strong). This reacts dynamically to the sun's
     position — moving the Directional Light moves the flare too.

## Chapter 11: Adding the character

1. In the Content Drawer, navigate to the character asset's folder (the
   tutorial's example path is a Characters/Heroes folder from a
   marketplace pack) and find its mesh.
2. **Important**: a character is a **Skeletal Mesh**, not a Static Mesh —
   if you had the Chapter 8 "Static Meshes" filter still active in the
   Content Browser, uncheck it, or the character won't show up in search
   results.
3. Drag the character into the level.
4. Expect a shader-compile delay after first dragging a new character in
   (the tutorial notes ~10 minutes) — the viewport stays navigable but
   the character may render untextured/laggy until shaders finish
   compiling. This is normal, not an error.
5. At this point the character is just placed in the level with no
   animation yet — animation is set up next, via Sequencer.

## Chapter 12: Character animation setup (Level Sequencer basics)

1. Place Actors panel → **Cinematics** → **Add Level Sequence**. You'll
   be prompted to save the project first.
2. This opens the **Sequencer** panel. Drag actors from the viewport/
   outliner into it to add them as tracks — first the **Cine Camera
   Actor**.
3. **Frame rate**: for a 24fps-style video, set the sequence's frame
   rate to **23.976** (the standard NTSC film rate) via the Sequencer's
   frame-rate control.
4. **Sequence length**: compute from your target duration — e.g. 10
   seconds at 24fps ≈ **240 frames**. Drag the red playback-range end
   marker out to that frame.
   - Gotcha called out in the tutorial: extending the overall sequence
     range does **not** automatically extend each track's own clip bar
     (e.g. the camera's "camera cut" clip) — you have to separately drag
     each track's clip to match the new sequence length, easy to miss.
5. The **Camera's Transform track** lets you keyframe the camera's
   location/rotation directly over time in Sequencer, for camera moves.
6. Drag the **character actor** into Sequencer as well.
7. Add an **Animation track** to the character (Track button →
   Animation) and pick a clip from the available animation library (the
   example skeleton ships with many, e.g. "Idle" variants).
   - Adding a clip inserts it starting at the current playhead position;
     drag the clip left/right to change when it starts.
   - Troubleshooting note from the tutorial: the default "Idle" clip
     held the character's weapon prop at an odd angle — fixed by
     deleting that clip and trying a different idle variant ("Idle
     Relaxed") that held the prop correctly. If a stock animation looks
     wrong on your character/prop combo, just try a different preset
     clip rather than assuming something is broken.
8. For movement, search the Animation track's clip picker for a term
   like "jogging" — large asset packs ship many jogging/running preset
   clips (e.g. "Jog Forward").
   - **Key concept**: a looping locomotion clip like "Jog Forward" is an
     **in-place** animation — it plays the running motion but does
     **not** move the character through the level on its own. Making
     the character actually travel along the ground requires separately
     animating its **Transform** (position) over time — see Chapter 13.

## Chapter 13: Animating character movement (partial — transcript cuts off here)

1. Switch the main editor viewport back to free **Viewport** navigation
   (un-pilot the Sequencer camera) so you can move around independently
   while setting up the character's path, without disturbing the
   camera's own keyframed motion.
2. Re-adjust the free-fly camera speed as needed for this finer
   positioning work (same speed control from Chapter 5).
3. Select the character, use **E** (rotate) to set its initial facing
   direction.
4. Position the character at the scene's intended starting point for
   the shot.
5. Extend the character's **Animation** clip in Sequencer (drag its
   right edge) to cover the full shot duration, so the loop keeps
   playing for the whole sequence.
6. Move the Sequencer playhead to the very start of the timeline
   (frame 0).
7. Add a keyframe on the character's **Transform** (location) at this
   starting position — this is the mechanism for animating movement:
   keyframe the start position at frame 0, then later move the playhead
   forward in time and keyframe a new (moved) position; Sequencer
   interpolates the character smoothly between the two, producing
   actual on-screen movement to go with the in-place run/walk cycle.

*The transcript ends here mid-explanation of the second keyframe — next
batch should pick up with keyframing the end position and likely
rendering/exporting the final shot via Movie Render Queue.*

---

*To extend: send more transcript/screenshots from later chapters of this
video (finishing the movement keyframes, lighting polish, rendering/
export) and this file will be updated to cover the full workflow.*
