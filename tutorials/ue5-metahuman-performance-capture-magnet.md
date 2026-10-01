# Tutorial notes: MetaHuman performance capture from video (UE5.8)

Source: a YouTube video from the same channel as the other tutorial-
notes files in this repo (Magnet VFX / "Amit"), captured mid-stream —
**chapters 1-9 were not captured**, so this picks up partway through.
Captured from the video transcript (screenshots, not watched directly).

**Important — likely a separate video, not a continuation**: this
content was sent right after the landscape/water/PCG-tree video
(`ue5-metahuman-animation-magnet.md`), but the two don't fit together:
this one reuses chapter numbers already used there ("Chapter 10,"
"Chapter 11") for entirely different content, opens with a MetaHuman
character already placed inside a pre-built **"Temple of Cambodia"**
demo map (not anything built earlier in that other video), and the
creator explicitly says "in my original video I make a POV shot... now
I'm going to show you how you can make your custom metahuman animation"
— referring back to a *different, separate* video. Treat this as its own
tutorial unless corrected. If it turns out to actually be the same video
continuing, these notes should be merged into the other file instead.

Status: **partial capture** — picks up with exporting/animating a
MetaHuman in Sequencer, through video-based performance capture, a full
hand-held Niagara fire-torch Blueprint (mesh + particles + light, with
pivot/local-space tracking fixes), and the start of a flickering Light
Function material (chapter 13, cut off). Chapters 1-9 (presumably
covering actually building/customizing the MetaHuman character itself)
are missing entirely.

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

## Chapter 13: Lighting and materials (partial — cuts off mid-setup)

1. Content Browser → Content folder → right-click → **Create →
   Material**, name it **"Light Material"**.
2. Open it, select the material's root/output node, find **Material
   Domain** → set it to **"Light Function"** (confirms this material is
   meant to be plugged into a light actor to animate/modulate its
   output — i.e. to drive the planned flicker effect).
3. Right-click in the graph, search **"time"**, add a **Time** node.

*Transcript cuts off here, right after adding the Time node — likely
continues building out the flicker logic (probably feeding Time through
some noise/sine function into the light function's output) and then
assigning this Light Function material to the torch's Point Light.*

---

*To extend: send more transcript/screenshots from later parts of this
video (finishing the flickering light material, and ideally the missing
chapters 1-9 covering the MetaHuman character's own creation) and this
file will be updated. If this turns out to be the same video as
`ue5-metahuman-animation-magnet.md` after all, these notes should be
merged into that file instead.*
