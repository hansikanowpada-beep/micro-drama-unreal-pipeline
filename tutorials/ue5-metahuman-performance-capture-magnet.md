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
MetaHuman in Sequencer, through video-based performance capture and the
start of a Niagara fire-effect addition (chapter 12, cut off). Chapters
1-9 (presumably covering actually building/customizing the MetaHuman
character itself) are missing entirely.

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

## Chapter 12: Niagara fire effects (partial — cuts off at the start)

1. Goal: add a fire-torch effect held in the character's hand.
2. Plan to download a Niagara fire system asset — the transcript cuts
   off right as the source is about to be named ("So for the Niagara
   fire system, I'm going to download this asset. And after
   download...").

---

*To extend: send more transcript/screenshots from later parts of this
video (finishing the Niagara fire effect, and ideally the missing
chapters 1-9 covering the MetaHuman character's own creation) and this
file will be updated. If this turns out to be the same video as
`ue5-metahuman-animation-magnet.md` after all, these notes should be
merged into that file instead.*
