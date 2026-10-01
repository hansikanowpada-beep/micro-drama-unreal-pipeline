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

Status: **partial capture** — covers the intro and all the foundational
editor basics (viewport navigation, object manipulation, the Content
Browser, main UI panels, layout customization, Play mode, duplicating
objects — chapters 3-4). This is all material the creator explicitly
says experienced users can skip — the real game-building content
(Blueprints programming, UI, weapons, Chaos physics) hasn't started yet
in the transcript, but should begin in the next chapter.

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
- **Immersive Mode / F11**: toggles a true full-screen viewport, hiding
  every editor panel so you can focus purely on the level. Game View
  mode (**G**) can still be toggled on/off while in immersive mode.
  Press **F11** again (or select Immersive Mode again) to exit back to
  the normal windowed editor layout.

**Adding objects to the world**:
- The **Add** button in the toolbar lets you hover over categories and
  drag in Unreal's built-in default assets — e.g. a **Sphere** (then
  scale it up), or a new **Light** (e.g. a Rectangle Light to light up
  a dark corner).
- **Gotcha**: a newly added object's editor widget/icon may not be
  visible if **Game View mode (G)** is still toggled on from earlier —
  toggle it off to see the new object's gizmo/icon.
- For **custom assets that are part of your own project** (not
  Unreal's generic built-ins), use the **Content Drawer** instead of
  the Add button — opens the **Content Browser**, which holds every
  asset, code file, and content change that makes up your game.
  Navigate it like a normal OS folder tree.
  - **Shortcut**: **Ctrl+Space** opens/closes the Content Drawer from
    anywhere, without needing to click the bottom-left button each time.
  - **Search**: Content Drawer → search field → type a term (e.g.
    "Cube") to filter for every matching asset across all folders, then
    drag the one you want (e.g. a specific colored cube) into the
    world.
  - **Ctrl+B**: with an asset selected (in the viewport or Content
    Browser), jumps the Content Browser straight to that asset's actual
    folder location — genuinely useful once a project has hundreds of
    nested folders and you're trying to figure out where, say, a "ramp"
    asset actually lives (example: jumps to a Content → Prototyping →
    Meshes folder).

## Chapter 4: User Interface

1. To see the Blueprint programming behind an object (previewed here,
   covered in depth in the next chapter): Content Browser → Third
   Person folder → Blueprints folder → double-click the character
   Blueprint to open it.
2. Close a Blueprint/window via its **X**, or drag its tab into the
   main viewport area to dock it.

**Main editor panels**:
- **Details panel** (bottom-right by default): shows every property of
  whatever's currently selected. Properties can be edited directly here
  instead of via the viewport gizmos — e.g. select a Cube, go to
  Details → **Scale** → type a precise Z-axis value (e.g. **2**)
  instead of dragging the Scale gizmo by hand.
- **Outliner** (above the Details panel by default): lists every object
  in the world. Hover between the two panels and drag to resize either
  one. Selection is **bidirectional**: selecting an object in the
  Outliner selects it in the viewport and populates the Details panel,
  and selecting an object in the viewport highlights it in the
  Outliner too.
- **Hide/unhide an object**: in the Details panel, hover the eye icon
  next to the object's name and click to toggle visibility — or use
  the shortcut key **H** with the object selected (select it again via
  the Outliner afterward, since it's no longer clickable in the
  viewport once hidden).
- **Tip — recovering after flying away**: since holding RMB + scrolling
  up makes the camera move very fast, it's easy to fly far enough that
  you lose track of your whole world. Fix: select any object in the
  **Outliner**, press **F** to instantly focus/snap the camera back to
  that object's location.

**Rearranging the UI layout**:
- Hold the **left mouse button** on a panel's tab (e.g. "Details") and
  drag to reposition/dock it elsewhere.
- Drag a tab on top of another panel to merge them into a tabbed group
  (switch between the two via sub-tabs at the bottom).
- Drag a tab out into empty space in the middle of the screen to
  **undock** it as a free-floating window — useful with multiple
  monitors.
- **Close a window**: click its **X**, or hover its tab and click the
  **middle mouse button** as a shortcut.
- **Hide without closing**: right-click a tab → **Hide Tab** — a small
  blue triangle then appears in that corner; hover/click it to restore
  the hidden tab.
- **Reset to Unreal's default layout** if things get rearranged beyond
  recovery: **Window** menu → **Load Layout** → **Default Editor
  Layout** — restarts the engine with the original default window
  arrangement.
- **Opening a window that isn't currently visible**: the **Window**
  menu lists every available panel, even hidden ones — e.g. **World
  Settings** (commonly used, not shown by default). Selecting it from
  the menu adds it as a new tab alongside Details, so you can switch
  between the two.

**Toolbar and Play**:
- The toolbar (top of the editor) holds frequently-used buttons already
  covered, like the **Add** tab.
- **Play button**: starts an actual playable preview of the game —
  since this project uses the Third Person template, pressing Play
  spawns a walkable, jumpable third-person character immediately.
  Press **Escape** to exit play mode and return to editing.
- **Selection Mode dropdown**: switches between editor modes, e.g.
  **Landscape** mode for terrain-sculpting tools (same mode used
  throughout the companion `ue5-starter-course-unrealsensei.md`). This
  tutorial is explicitly **programming-focused only** — it won't cover
  what these other modes do; that's the subject of the separate
  environment-design tutorial.
- **Duplicating an object**: rather than dragging a fresh copy from the
  Content Browser and redoing any custom Details-panel edits by hand,
  select the object and press **Ctrl+D** to duplicate it directly,
  preserving all its current properties/modifications.

*Transcript cuts off here, right after introducing Ctrl+D — likely
continues into the actual Blueprints programming chapter next.*

---

*To extend: send more transcript/screenshots from later parts of this
video (Blueprints programming, UI, weapons, Chaos physics destruction,
and adding the finished game to an environment) and this file will be
updated.*
