# Tutorial notes: MetaHuman performance capture from video (UE5.8)

**Attribution now uncertain (see correction note)**: this file originally
claimed the same channel as the other tutorial-notes files in this repo
(Magnet VFX / "Amit"), reasoning by analogy with the landscape/water/
PCG-tree video it was sent alongside. That landscape video was since
confirmed, from an actual screenshot of its YouTube page, to really be
by a *different* channel — **Unreal Sensei** — not Magnet/Amit (see the
correction note at the top of `ue5-starter-course-unrealsensei.md`,
the renamed file formerly called `ue5-metahuman-animation-magnet.md`).
That breaks the original reasoning for this file's attribution too:
this video's actual source channel is now **unverified** — it could be
Unreal Sensei, Magnet/Amit, or a third channel entirely. Treat the
"Magnet VFX" credit below as unconfirmed until a screenshot of this
specific video's own YouTube page is seen.

Source (as originally assumed, now unverified): a YouTube video,
captured mid-stream — **chapters 1-9 were not captured**, so this picks
up partway through. Captured from the video transcript (screenshots,
not watched directly).

**Separate video, not a continuation of the landscape/PCG-tree one**:
this content was sent right after the landscape/water/PCG-tree video,
but the two don't fit together: this one reuses chapter numbers already
used there ("Chapter 10," "Chapter 11") for entirely different content,
opens with a MetaHuman character already placed inside a pre-built
**"Temple of Cambodia"** demo map (not anything built earlier in that
other video), and the creator explicitly says "in my original video I
make a POV shot... now I'm going to show you how you can make your
custom metahuman animation" — referring back to a *different, separate*
video (possibly `ue5-starter-course-unrealsensei.md`, possibly a third
video altogether — unconfirmed). Treat this as its own tutorial from an
unverified channel until corrected.

Status: **partial capture** — picks up with exporting/animating a
MetaHuman in Sequencer, through video-based performance capture, a full
hand-held Niagara fire-torch Blueprint, a flickering Light Function
material, a full post-processing camera-lens pass, and animated camera
movement with a custom Perlin Noise camera shake and dynamically
animated focus distance (chapter 15). Likely at or near the end of this
video's content. Chapters 1-9 (presumably covering actually building/
customizing the MetaHuman character itself) are missing entirely.

## (Picked up mid-stream) Animating the MetaHuman in Sequencer

1. Export the created MetaHuman (from a Metahumans folder) — click
   **Export** (confirm on a second Export prompt).
2. Bring the MetaHuman into a Level Sequence: select the MetaHuman
   character in the viewport → Sequencer → **Add → Add Actor Track**.
   - Dragging in the MetaHuman's Blueprint also auto-adds a **MetaHuman
     Control Rig** track, which isn't needed for this — select it and
     **delete**.
3. Add body animation: **Body** track → **+** → **Animation** → select
   a walk animation clip. Extend the clip across the timeline.
4. Animate the character's position (movement), same pattern as the
   other two tutorials in this repo:
   - Go to the first frame, select the BP actor, **+** → add
     **Transform**, create a keyframe.
   - Right-click the keyframe → set interpolation to **Linear**, and
     set Linear as the default interpolation method.
   - Enable **Auto Keyframe**.
   - Go to the last frame, reposition the character → the end keyframe
     is created automatically.
   - Play back to confirm the walk-with-movement animation works.

## Chapter 10: Performance capture

1. Confirm in Selection mode that the MetaHuman is successfully
   animated.
2. **Recreating a POV (first-person) shot**: select the Cine Camera
   Actor → **+** → **Attach** → select the character's BP actor →
   search **"head"** in the socket picker → select the **head bone** —
   attaches the camera directly to the character's head.
   - Reset the camera's location, then reposition it for first-person
     framing.
   - Toggle the camera track off/on and press **G** to preview — camera
     now moves with the character's head.
   - Decrease **Focal Length** for a wider POV angle.
   - Delete any prior camera keyframes, go to the first frame, nudge the
     camera down slightly so the character's legs/hands are visible in
     frame, keyframe the camera's Transform, animate it over a few
     frames, and set this keyframe's interpolation to **Cubic** (smoother
     than Linear — used deliberately here for the POV camera motion).
   - Zoom in slightly, increase **Aperture** — final polish on the POV
     shot recap.
3. **Switching to real performance capture** (the actual point of this
   section): rather than hand-animating, transfer motion from a real
   video onto the MetaHuman.
   - Download and install a **plugin** for Unreal Engine — noted as
     **only compatible with Unreal Engine 5.8** specifically. Install
     via **"Install to Project"**, then **restart the engine** (required
     after installing it) and reopen the level.
   - The plugin ships with its own demo content: open **Temple of
     Cambodia folder → Demo Map → Interior Map**, open its Sequence.
4. **Importing the source video**: Tools → **Live Link Hub**.
   - In Live Link Hub: dropdown menu → **Capture Manager** → **Add** →
     select **Mono Video Ingest** → choose the directory containing the
     source video → select the video → **Add to Queue** → start
     processing. Close Live Link Hub once complete.
5. **Create a MetaHuman Performance asset**: in the Metahumans folder,
   right-click → **MetaHuman → Create MetaHuman Performance**.
6. Open the new MetaHuman Performance asset:
   - **Footage Capture** dropdown → select the imported footage.
   - Practical tip from the creator: in his source video he holds a
     stick on-camera, specifically so he'd "have something to put [a
     prop] in post" — i.e. a physical placeholder prop held during
     filming makes it easier to composite a CG prop into the character's
     hand afterward.
   - Enable **Body Tracking**.
   - A skeleton-tracking overlay appears on the footage preview.
   - Click **Process** — takes a while to run.
   - Once complete, the resulting animation can be previewed/played.
7. **Export the captured animation**: **Export Animation**, name it
   (tutorial uses "Walk Loop Around"), **Save**, **Create**, confirm
   **"Add Compatibility"** with **Yes** — produces a usable animation
   asset built from real video footage rather than a stock/preset clip.

## Chapter 11: Scene refinement

1. Close the MetaHuman Performance window, return to Sequencer.
2. **Detach the camera** from the character's head: select the Cine
   Camera Actor → **Attach** tab → delete the attachment.
3. Reset the camera's position (Details panel → reset Location),
   temporarily disable the camera track, re-select and manually
   reposition/rotate the camera (reset rotation as needed).
4. **Reposition the character**:
   - Delete all existing keyframes on the character's Transform.
   - Delete the old placeholder walk-animation clip.
   - Move the character to a new starting point in the scene.
   - Reposition the camera to frame this new position.
5. **Apply the newly captured performance animation**: select the BP
   actor → Animation track → **+** → select the exported "Walk Loop
   Around" animation (replacing the earlier stock clip).
6. Delete the camera's existing keyframes too, then re-extend the
   overall sequence length and — same gotcha as the other tutorials in
   this repo — separately extend the camera's own clip/cut length to
   match (extending the sequence range alone doesn't extend per-track
   clips).
7. Play back to confirm the custom captured animation works correctly.
8. Final composition pass: reposition the character again (disable all
   snapping while doing so), zoom the camera in slightly.
9. **Focus on the character**: select the Camera Component, Details
   panel → Focus settings → enable **"Draw Debug Focus"** (visualizes
   the focal plane in the viewport) → adjust **Focus Distance** until
   the character reads sharp.

## Chapter 12: Niagara fire effects

1. Goal: add a fire-torch effect held in the character's hand.
2. **Source Niagara asset**: a pack referred to as "Medieval Sewers
   Dungeons" (transcript renders it "medival swear dungeons" — treat as
   approximate). Inside it: a Niagara system folder → a **"Flame"**
   Niagara system — double-click to open/inspect.
3. **Build a complete, reusable fire torch as a Blueprint** (mesh +
   particles + light combined, same "wrap it in an Actor Blueprint"
   pattern as the wind-tree technique in the companion video):
   - Content Browser → right-click → **Blueprint Class → Actor**, name
     it **"FireTorch"**.
   - Open it, add the torch's static mesh: Content Browser → Temple of
     Cambodia folder (enable Static Mesh filter via the hamburger icon
     if no filters show) → find a **"Fire Torch"** static mesh → in the
     Blueprint, **+ Add** → search "static mesh" → add a **Static Mesh**
     component → assign the fire torch mesh to it.
   - Add the particle fire: **+ Add** → search "Niagara particle
     system" → add it → assign the **Flame** Niagara system found above
     (disable the Static Mesh filter, browse back to the Medieval Sewers
     Dungeons Niagara folder) → position/rotate it onto the torch mesh.
   - Add a light: **+ Add** → search "light" → **Point Light** →
     position it over the torch flame, change its color to an
     **orangish** tone in the Details panel.
   - Save, **Compile**, close the Blueprint.
4. Place the FireTorch blueprint into the scene.
   - **Troubleshooting — exposure too high**: go to Sequencer, select
     the camera, increase **Aperture**.
5. **Attach the fire torch to the character's hand**:
   - Bring the FireTorch blueprint into Sequencer: **Add → Add Actor
     Track** → select it.
   - **+** → **Attach** → select the character's BP actor → **Body** →
     search "hand" → select the **hand_r** (right hand) socket.
   - Reset the torch's Location, reposition it relative to the hand.
   - Camera tweaks: decrease **Exposure** (search "exposure", set to
     **10**) and decrease **Aperture**.
   - **Scale down the torch**: open the FireTorch blueprint, select the
     static mesh component in its Viewport, enable **Uniform Scale**,
     decrease the value (tutorial sets **7**).
   - Reposition the Niagara/fire component relative to the (now smaller)
     mesh. **Compile**, close.
6. **Troubleshooting — fire position doesn't track the torch correctly
   during animation** (multiple related issues worked through in
   sequence):
   - First symptom: fire doesn't update position in real time as the
     torch/hand moves. **Fix**: open the Niagara system, select the
     particle system (emitter), enable **"Local Space"** → Compile,
     Save, close. (Without this, the particle system simulates in world
     space and lags behind a moving attachment.)
   - Still slightly misaligned afterward → reposition the fire torch's
     Niagara component again to correct the offset.
   - Deeper symptom: when the character's animation **lowers the
     torch** (a different hand pose), the fire visibly detaches/shifts
     from the torch tip. **Root cause**: the Niagara particle system's
     own pivot point sits in its **middle**, not at the torch tip, so
     it doesn't track rotation around the right point.
   - **Fix — move the Niagara system's pivot** (same "find and relocate
     the pivot" concept as the lamp post's X-Form/Edit-Pivot fix in the
     road/material tutorial, applied here inside the Niagara/particle
     editor instead):
     - Open the Niagara system, dock it, zoom into its viewport.
     - Select the particle system, find its **Sprite Renderer**
       settings, expand **Sprite Rendering**, find **"Default Pivot in
       UV space"**.
     - Hold **Ctrl** and drag/adjust this value (tutorial tries values
       around **64-65**, likely a UV-space offset rather than world
       units — confirm the actual control behavior against the live
       video) until the pivot sits at the bottom of the particle system
       instead of its middle.
     - Compile the Niagara system, compile the Blueprint too, close
       both.
   - Reposition the torch once more and re-test — fire now stays
     correctly anchored to the torch tip even as the character's hand
     pose changes.
   - Reposition the attached point light similarly for consistency.
7. Remaining known issue, not yet resolved in the transcript: the fire's
   **render resolution looks low** — the creator notes it "fixes over
   time" (likely simulation warm-up or an anti-aliasing/render-setting
   effect at final export, not fully explained here).
8. **Next planned step**: add flickering to the torch's point light via
   a custom **Light Function material** — transitions into Chapter 13.

## Chapter 13: Lighting and materials

**Building the flickering Light Function material** (continuing from
the Time node):

1. Add a **Scalar Parameter** node (press **S** + click), name it
   **"Frequency"**.
2. Add a **Multiply** node (press **M** + click) to combine the two:
   connect **Time** → input A, **Frequency** → input B.
3. Add a **Sign** node (right-click, search "sign"), connect it after
   the multiply.
4. Add a **Frac** (fractional part) node (right-click, search "frac"),
   connect it in the chain.
5. Connect the final result into the material's **Emissive/Emitter
   Color** output.
6. Set a value on the remaining input (tutorial uses **0.5**), **Apply**,
   save, close the material.
7. Right-click the material → **Create Material Instance**.
8. **Apply to the light**: select the torch's Point Light → Details
   panel → find the **Light Function Material** slot → assign the new
   material instance. The light now flickers.
9. **Tune the flicker**: open the material instance, enable the
   **Frequency** parameter override, increase it (tutorial sets **1**),
   save.
10. **Duplicate the light** (right-click → Duplicate) — ends up with two
    point lights on the torch, one steady and one flickering (for a
    richer combined look rather than the whole torch glow pulsing
    uniformly). Decrease the **Intensity** on both lights to balance
    them against each other.
11. **Light quality settings** (applied to the light(s)):
    - **Source Radius**: tutorial tries **50**, settles on **10** — a
      larger radius gives a visibly softer-edged shadow from the torch.
    - **Volumetric Scattering**: tries **5**, settles around **2** for a
      subtle glow/scatter in the air near the flame.
12. Play to preview the lit, flickering torch in motion.

## Chapter 14: Post-processing

1. **Troubleshooting — unwanted/hard shadow**: select the Camera
   Component, search **"mega light"** (**Mega Lights**, a newer UE5
   lighting feature) and enable it from there — resolves the harsh
   shadow.
2. Minor reposition of the Niagara particle component on the torch.
3. **Note on fire texture looking low-res in the editor viewport**: this
   is just a real-time optimization/downsampling artifact — the
   creator confirms it resolves once rendered at full/high quality, not
   an actual problem to fix.
4. **Remove the default Post Process Volume**: Outliner → search
   "postprocess volume" → select the existing one → **delete** it (this
   tutorial drives all post-processing from the Camera Component's own
   settings instead, rather than a separate volume actor).
5. **Camera lens pass** (Camera Component, same recipe as the
   road/material-blending tutorial's final camera pass, with this
   video's own specific values):
   - **Squeeze Factor**: increase to maximum.
   - **Sensor Width**: halve it (type `/2`, Enter) — paired anamorphic-
     lens effect with Squeeze Factor.
   - **Focus**: Focus settings → enable **Debug Focus Plane** → adjust
     **Focus Distance** to bring the character into sharp focus.
   - **Bloom**: enable, method = **Convolution**, decrease **Intensity**
     slightly.
   - **Chromatic Aberration**: enable, **Intensity** and **Start
     Offset** both set to **0.5**.
   - **Lens Flare**: enable, decrease **Intensity** to **0.1**.
   - **Image Effects → Vignette**: enable, modest amount.
   - **Film Grain**: enable, **Intensity** = **0.5**.
   - **Aperture**: decrease slightly.
6. This completes the base shot — character, prop (fire torch), and
   camera lens treatment all combined.

## Chapter 15: Camera animation

1. Go to the first frame, select the camera's **Transform** track,
   create a keyframe.
2. Go to the last frame, move/reposition the camera to its end point.
3. Play back — confirms the camera transitions between the two
   positions.
4. Select all the middle/default keyframes, right-click → set
   interpolation to **Cubic** (smoother curve than Linear, used here for
   the main camera move — same choice made for the POV shot earlier in
   this video).
5. **Camera shake** (same general Camera Shake Blueprint technique as
   the companion environment-basics tutorial, with this video's own
   specific values):
   - Content Browser → Content folder → right-click → **Create
     Blueprint** → All Classes → search "shake" → select the **Camera
     Shake** base class.
   - Name it **"Shake"**, open it, find the root **Shake Pattern**,
     select **Perlin Noise Camera Shake Pattern** (transcript renders
     this "parallel noise camera shake pattern" — a mis-transcription of
     "Perlin Noise," matching the identical pattern/typo seen in the
     companion environment-basics tutorial's camera-shake chapter).
   - **Timing → Duration**: set to **0** (continuous/looping).
   - Set an initial **Rotation** value (~1), **Compile**.
   - Apply it to the camera: Sequencer → select the Camera → **+** →
     **Camera Shake** option → select the "Shake" blueprint. Extend this
     track across the timeline.
   - Play — default shake looks too strong/off, tune it:
     - **Rotation Frequency** = **2**, **Rotation Amplitude** = **0.5**.
     - **Pitch** (expand) ≈ **4**.
     - Decrease frequency to **0.5**. Compile.
   - Still refining — decrease **Rotation Frequency** further to
     **1.5**, compile, for a more subtle result.
   - Zoom the camera slightly, re-fix focus on the character afterward
     (the zoom changes framing/focus distance).
6. **Animating Focus Distance over time** (since the camera now moves
   continuously, a single static focus distance isn't enough to keep the
   character sharp throughout):
   - Go to the first frame, select the camera, find **Focal
     Length**/Focus settings, enable **Debug Focus Plane**.
   - Lock focus onto the character.
   - Disable the Debug Focus Plane visualization once correct (it's just
     an on-screen aid, not meant to show in the final render).
   - Result: the character stays in focus continuously as the camera
     moves and shakes.
7. Play the assembled shot.

---

*To extend: send more transcript/screenshots from later parts of this
video (any further polish, and the final rendering/export step — plus
ideally the missing chapters 1-9 covering the MetaHuman character's own
creation) and this file will be updated. If this turns out to be the
same video as `ue5-metahuman-animation-magnet.md` after all, these notes
should be merged into that file instead.*
