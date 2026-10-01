# Tutorial notes: UE5 environment building basics

Source: YouTube tutorial by **Amit** (channel: **Magnet**), captured from the
video transcript (shared as screenshots, not watched directly — so exact
button positions/labels should be double-checked against the live video,
but the sequence of operations below is accurate to the transcript).

Status: **complete capture** — covers the full video, start to finish:
asset sourcing through environment building, set dressing, cinematic
camera, character/Sequencer animation, camera shake, and Movie Render
Queue export.

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

## Chapter 13: Animating character movement

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
   starting position:
   - Keyframing the parent **Transform** track keys rotation + all
     location axes together in one keyframe.
   - To keyframe just one component (e.g. only rotation), expand
     Transform into its sub-tracks and key that sub-track individually.
   - **Auto Keyframe** (a toggle in the Sequencer toolbar) automatically
     creates a keyframe any time you move/rotate the actor, so you don't
     have to manually click "add key" every time — handy once you're
     doing a lot of these.
   - **Keyframe interpolation**: new keyframes default to an eased
     (non-linear) curve. For constant-speed movement, right-click a
     keyframe → set it to **Linear**; you can also set Linear as the new
     default interpolation so later keyframes are created linear
     automatically.
8. Move the playhead to the end of the shot and reposition the character
   to its ending location — this creates the second keyframe (manually,
   or automatically if Auto Keyframe is on) and Sequencer interpolates
   the character's movement between the two positions.
9. **Troubleshooting — character runs backward**: if the character moves
   in the wrong direction relative to its facing, select it and use
   **E** (rotate) to correct its orientation, then re-check.
   - Tip: selecting the **Sky** actor in the Outliner clears the
     yellow/orange selection-outline highlight from other objects,
     making it easier to visually judge the character's motion without
     a distracting outline in the way.
10. Play back the animation to check it — movement looks right
    directionally, but may still look too slow, and the character's
    **feet may not actually contact the ground correctly** (foot
    sliding) — addressed next in Chapter 14.

## Chapter 14: Correcting foot placement (fixing foot sliding)

1. First-pass fix: go to the start of the clip, press **W** (move) and
   nudge the character's start position slightly to better align the
   stride length with the distance it needs to cover — zoom in and
   check visually whether the feet now roughly match ground contact.
2. Even after that, the character won't perfectly track **uneven ground
   / surface contours** — the real fix is manual, frame-by-frame
   keyframing:
   - Go to the start of the sequence, close to the character.
   - This is explicitly called out as **time-consuming**: step through
     frames one at a time and re-keyframe the character's position each
     time a foot should contact the ground, so it precisely matches the
     surface.
   - Select the character, press **W** (move gizmo).
   - Use the Sequencer transport's **next-frame** button to step forward
     one frame at a time.
   - At each frame where a foot visibly touches the ground, nudge the
     character's position to match the surface and create a keyframe.
   - If the default keyframe snapping isn't precise enough, go to the
     Sequencer's **Snapping** settings and set the snap interval to
     **1** (frame-accurate).
   - Repeat through the whole clip. Tedious, but produces noticeably
     more natural movement that respects the ground's actual shape
     (the tutorial demonstrates the technique rather than doing the
     full pass on camera, since it's repetitive).

## Chapter 15: Camera animation and focus

1. Switch focus to the **Camera** (rather than the character) to animate
   it following the action.
2. Select the camera, expand its **Transform**, create a starting
   keyframe (frame 0).
3. Move the playhead to a point closer to the character and reposition
   the camera (push in) — note the framing is now too wide.
4. Fix framing via the **Camera Component** settings (not the actor
   Transform) — adjust **Focal Length**.
   - Gotcha: changing Focal Length may appear to do nothing at first —
     that's because the camera's **Lens Type** is still set to a fixed
     **Prime** lens (the 12mm from Chapter 10), which by design has one
     unchangeable focal length.
   - Fix: change Lens Type to a **Zoom/Universal Zoom** lens, which
     unlocks the Focal Length slider. Tutorial sets it to **45mm**.
5. After zooming in, the character falls out of focus (depth-of-field
   blur) — fix by adjusting **Focus Distance** until the character is
   sharp again.
6. **Bokeh/depth-of-field control**: lowering the camera's **Aperture**
   (f-stop) value produces a stronger background-blur (bokeh) effect —
   tutorial sets it very low (~1) for a pronounced shallow-depth look.
7. Animate the camera over time: with the starting keyframe already set,
   move the playhead to the end of the shot and reposition the camera —
   with **Auto Keyframe** on, this automatically creates the matching
   end keyframe.
8. Keyframe the character's start/end position the same way, using
   **Linear** interpolation (set as default earlier) so camera and
   character motion read consistently rather than floaty/eased.
   - Tutorial notes the resulting camera motion now looks "a little too
     linear" / mechanical — motivating the camera shake added next.
9. Playback can look laggy while editing in the viewport — this is just
   real-time viewport + screen-recording overhead, not a problem with
   the actual render output.
10. Reinforces the Chapter 13/14 point: animating the character's
    Transform over time is also what makes it track the ground
    surface's contours correctly — it's not automatic from the
    animation clip alone.

## Chapter 16: Adding camera shake (custom Camera Shake Blueprint)

A fully custom camera-shake effect, built from scratch as a Blueprint:

1. In the Content Drawer, right-click → **Blueprint Class**.
2. Search the parent-class picker for **Camera Shake** and select it as
   the base class.
3. Name it (e.g. `CameraShake`) — **do not use a space in the name**,
   use an underscore instead if needed; spaces aren't supported here.
4. Double-click to open it. Minor editor quirk noted in the tutorial:
   you may need to close and reopen it once after creation for it to
   fully register/update.
5. Inside the blueprint, expand the **Camera Shake Pattern** / root
   shake-pattern category.
6. Set the pattern type to **Perlin Noise Camera Shake Pattern**.
7. Under **Timing**, set **Duration** to **0** — this makes the shake
   run continuously/looping rather than for a fixed length.
8. **Compile** and close the blueprint.
9. Back in the Level Sequence: select the **Camera** track, add a
   **Camera Shake** track (Track/+ button → Camera Shake), and assign
   your new Camera Shake blueprint to it.
10. Extend this track to cover whichever portion of the timeline should
    have the shake active.
11. If no visible shake appears yet, it's because the pattern's
    amplitude/frequency are still at (near-zero) defaults — reopen the
    Camera Shake blueprint and, under the Perlin Noise pattern's
    **Rotation** (Pitch/Yaw/Roll) settings:
    - Set **Rotation Amplitude Multiplier** (e.g. 2).
    - Set **Frequency** (e.g. 1, bumped to 2 for a more noticeable
      effect).
12. Recompile, return to Sequencer — the shake is now visible: a subtle,
    organic handheld-camera jitter, most noticeable when the camera is
    moving fast (reads as a natural "camera jerk"/micro-shake rather
    than a shaky-cam gimmick).
13. The same approach can be reused (additional Camera Shake tracks)
    for other camera moves elsewhere in the scene.

## Chapter 17: Refining camera and focus (final pass)

1. For a separate/additional camera movement, this time **uncheck Auto
   Keyframe** on the camera (manual control instead, for precision).
2. Delete and redo any problematic auto-created keyframes as needed
   (select a keyframe → delete, then re-add the correct one).
3. Adjust **Focal Length** (Camera Component) again to properly reframe
   the character.
4. Reposition the camera and set the correct **Focus Distance** so the
   character is sharp again at this point in the timeline.
5. Keyframe this framed/in-focus state.
6. To build a continuous camera-follow path: keyframe at one time, move
   forward in the timeline, reposition the camera to track the
   character's new location, and keyframe again — repeat to build up a
   smooth follow.
   - **Common mistake called out explicitly**: if you keyframe the
     camera's position at a given time but don't also re-keyframe the
     **character's** position (or vice versa) at that same time, one of
     them visually "floats" out of place relative to the other. Fix:
     keep camera Transform, character Transform, **and** Focus Distance
     keyframed together at each key moment — Focus Distance needs its
     own update too, since the correct focus value changes as the
     camera-to-character distance changes.
7. End result: camera movement, focus/depth-of-field, and character
   tracking all working together — character stays framed and in focus
   throughout. This is effectively the finished shot, ready for export.
8. Tutorial's framing of why this matters: a moving ("camera stick")
   shot versus a static locked-off one is what gives the whole scene a
   sense of life.

## Chapter 18: Rendering and export (Movie Render Queue)

1. For high-quality output with proper anti-aliasing, enable a plugin
   first: **Edit → Plugins**, search "Movie", enable **Movie Render
   Queue** (and the additional-render-passes plugin suggested alongside
   it).
2. This requires an editor restart — **save your project first**, then
   restart.
3. After restarting: **Windows → Cinematics → Movie Render Queue**.
4. In the Movie Render Queue panel:
   - Click **Render** (or **+ Render**) and select your Level Sequence
     as the job.
   - Open the job's settings/config.
   - Default output is a **JPEG** image sequence — remove that and add
     **PNG Sequence [8bit]** instead, for lossless frames.
   - Under **Anti-Aliasing**: set the sample count — tutorial uses
     **32** (good quality/speed balance; 64 looks even cleaner but
     renders slower).
   - Check **Overwrite** (existing files) so re-renders don't fail.
   - Set **Anti-Aliasing Method** to **MSAA**.
   - Under **Output**: set the output path/directory.
   - Set a custom **Output Frame Rate** matching your sequence —
     tutorial uses **23.976** (or pick e.g. 60fps if your project target
     is different).
   - Set **Resolution** — tutorial uses **1080p** (4K is an option, at a
     render-time cost).
5. Click **Accept** to confirm the job config, then **Render** to start.
6. Output is a **PNG image sequence**, not a finished video file.
7. **Final step — compositing**: import the PNG sequence into a video
   editor/compositor (the tutorial uses **Adobe After Effects**) to
   assemble it into the final video file (this is outside Unreal — add
   music, color grade, export to mp4, etc. there).

---

**This completes the full tutorial workflow** captured from this video:
free asset sourcing → base environment (lighting/sky/fog) → landscape →
set dressing/foliage → cinematic camera → character import → Sequencer
animation (locomotion + manual foot-placement correction) → camera
animation/focus pulls → custom camera shake → Movie Render Queue export.

*To extend: if a different tutorial or additional techniques get added
later, start a new file rather than appending unrelated content here.*
