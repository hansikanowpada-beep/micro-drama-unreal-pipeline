# Tutorial notes: How to Create a Game in UE5 (first-person shooter)

Source: **"How to Create a Game in Unreal Engine 5 - UE5 Beginner
Tutorial"** by **Unreal Sensei** (same channel as
`ue5-starter-course-unrealsensei.md` — confirmed via the YouTube "Next
video" card shown after that one finished playing). 2.3M+ views,
published 3 years before capture, runtime **2:39:04**. This is video 2
of Unreal Sensei's 11-part "Unreal Engine 5 Beginner Tutorials"
playlist (video 1 is the Starter Course landscape/environment video
already captured in this repo).

Unlike the other tutorial files here, this one is **pure gameplay/
Blueprint programming** — no Fab/Megascans asset downloads, no
landscape or material work. It builds a first-person shooter from
scratch: destroy all targets before a timer runs out. Kept as its own
file since the subject matter (Blueprints, UI, weapons, Chaos physics)
is distinct from the environment-building tutorials.

Captured from the video transcript (screenshots, not watched directly)
— double-check exact button labels against the live video.

Status: **partial capture** — covers the intro and the very basics of
viewport navigation/object manipulation (chapter 3, in progress). This
is foundational material the creator explicitly says experienced users
can skip — the real game-building content (Blueprints, UI, weapons,
physics) hasn't started yet in the transcript.

## Chapter 1: Intro

- Goal: build a complete first-person shooter — destroy all targets
  before the timer hits zero.
- Topics the full tutorial covers: Blueprints visual scripting, a user
  interface to display game info, custom weapons built from scratch,
  object destruction using **Chaos physics**, and finally adding the
  finished game to any environment of your choice.
- No prior Unreal or programming experience assumed — everything is
  shown step by step.
- Cross-reference: the creator has a separate UE5 beginner tutorial
  focused on **level and environment design** — almost certainly
  `ue5-starter-course-unrealsensei.md`, already captured in this repo.
- This tutorial is mostly programming-focused. The creator explicitly
  says: if you already know how to navigate Unreal and move objects,
  skip ahead to the Blueprints chapter — the next chapter (viewport
  navigation/manipulation) is pure basics for newcomers.

## Chapter 2: Creating a Project

1. Get Unreal Engine 5 via the Epic Games Launcher → Unreal Engine tab
   → Library. Under installed versions, click **+** to add a version if
   none are installed (the creator already has UE 5.2 at capture time —
   a newer version is fine too).
2. Launch via the **Launch** button, or create a desktop shortcut from
   the dropdown next to it for faster access later.
3. First launch shows the **Unreal Project Browser** — the "Recent
   Projects" tab lists previously opened projects (empty on first run).
4. To create a new project from a template: **Games** category → pick a
   starter template. The creator selects **Third Person** (even though
   the end goal is a first-person game) specifically to show off
   Unreal's built-in features via the Third Person template first — the
   project gets converted to first-person in a later chapter.
5. Leave the project settings at their defaults for now.
6. **Project name**: e.g. "My First Project".
7. Choose a save location (file-folder icon) — the creator saves to the
   Desktop. Click **Create**.
8. This generates a new folder (named after the project) at the chosen
   location containing all the project's files/assets.
9. **Tip**: once a project exists, you can skip the Project Browser
   entirely next time — open the project's folder and double-click its
   `.uproject` file directly.

## Chapter 3: Viewport (in progress)

Pure navigation/manipulation basics — skippable if already familiar
with Unreal.

**Camera navigation**:
- Hold **right mouse button** to enable look-around; move the mouse to
  pan the camera.
- With RMB held: **W** forward, **S** backward, **A** left, **D** right,
  **E** up, **Q** down — the same WASD+QE scheme as any first-person
  game.
- **Camera speed**: adjustable via the camera-speed icon in the
  viewport toolbar (drag down to slow down, up to speed up — tutorial
  example sets it to **3.2**), or as a shortcut, hold RMB and scroll the
  mouse wheel (scroll up = faster, down = slower).

**Selecting and moving objects**:
- **Left-click** an object to select it.
- With an object selected, the move/rotate/scale **gizmo** appears.
  Hovering over an axis arrow and dragging moves the object along that
  axis (left-click drag).
- **Snapping** is enabled by default (visible as a stepped/incremental
  movement) — toggle it off via the snap button in the toolbar for
  smooth, non-snapped movement. Re-enabling it lets you pick a specific
  snap increment (e.g. **100** = 100cm = 1 meter steps).
- **Rotation** works the same way — select the Rotate tool, drag an
  axis ring to rotate; rotation snapping can likewise be toggled off for
  smooth rotation.
- **Undo**: **Ctrl+Z** at any time.
- **Scaling**: drag an individual axis handle to scale on just that
  axis, hover the small white box in the gizmo's center to scale
  uniformly on all three axes at once, or hover between two axis
  handles to scale on just those two axes together. Scale snapping can
  also be toggled off (via the same Snap Tools area, top right).
- **Combined-axis movement**: hovering over the small square between
  two move-arrows (rather than directly on one arrow) moves the object
  along both of those axes at once.
- **Tool hotkeys**: **W** = Move, **E** = Rotate, **R** = Scale (same
  convention confirmed across every other tutorial in this repo).
- **Delete an object**: select it, press **Delete** or **Backspace**.

**View modes**:
- **Grid visibility**: Show menu → uncheck **Grid** to hide the
  viewport's reference grid (the creator finds it visually distracting).
- **Editor-only widgets/icons**: visible in the editor but never shown
  to the actual player at runtime — they're purely a development aid.
- **Game View toggle — G key**: hides all editor icons/gizmos/widgets
  for a clean preview of exactly what the player will see. Described as
  one of the most-used shortcuts in the whole tutorial — the workflow
  throughout is: select an icon, make a change, press **G** to hide it
  again immediately once you don't need it selected anymore.
- **Rendering view modes** (viewport toolbar, next to the camera speed
  control): **Wireframe** (shows all polygon edges), **Unlit** (world
  with no lighting applied — useful to find/select objects in an
  otherwise-too-dark scene), **Lighting Only** (shows just the lighting
  contribution, no materials/textures) — normally left on **Lit** (the
  default) for regular work.

*Transcript continues past this point — more to be added as further
screenshots are shared.*

---

*To extend: send more transcript/screenshots from later parts of this
video (Blueprints programming, UI, weapons, Chaos physics destruction,
and adding the finished game to an environment) and this file will be
updated.*
