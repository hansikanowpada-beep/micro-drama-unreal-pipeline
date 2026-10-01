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

Status: **partial capture** — covers the intro, all the foundational
editor basics (chapters 3-4), an introduction to Blueprint editor
vocabulary (chapter 5), node-graph fundamentals including a live
"Hello World" demo, migrating the game's weapon/target assets from a
separate downloadable project, and the start of the first custom
Blueprint (`BP_Target`, an Actor-class Blueprint) — cut off right as
the target mesh is about to be added to it (chapter 8). The actual
shooting/scoring/UI/physics logic for the game hasn't started yet.

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
  preserving all its current properties/modifications. The duplicate
  lands exactly on top of the original (looks like nothing happened
  until you move it).
- **Alt+drag**: an alternative duplicate shortcut — hold **Alt** before
  dragging with the Move tool to drag out a new copy in one motion
  (same convention used throughout the environment-building tutorials
  in this repo).
- **Multi-select**: hold **Shift** and click to select multiple objects
  at once; hold **Ctrl** and click a selected object to deselect just
  that one. With several objects selected, Move/Rotate/Scale apply to
  the whole group together. **Ctrl+Z** undoes as usual.

## Chapter 5: Blueprint Programming

1. **What Blueprints are**: Unreal's visual scripting language, an
   alternative to writing C++ by hand. Instead of hundreds of lines of
   code, you connect boxes called **nodes** together — logically the
   exact same thing as code, just a different way to visualize a
   program. In the creator's opinion, Blueprints are easier and faster
   than C++ for most projects.
   - **Should you learn C++ or Blueprints?** For most projects, stick
     with Blueprints, especially as a beginner — they can do almost
     everything C++ can. Even if you do end up using C++, you'll still
     encounter Blueprints constantly, since they're used everywhere
     throughout Unreal Engine one way or another.
2. **First look at an existing Blueprint**: open the default **Third
   Person Character** Blueprint that ships with the Third Person
   template — Content Browser → Third Person → Blueprints →
   `BP_ThirdPersonCharacter` → double-click.
3. The Blueprint Editor window opens hovering over the main level
   editor — hold left-mouse-button on its tab to dock it, letting you
   quickly switch between the level editor and any open Blueprint
   editors (same docking mechanic as the main editor's panels).
4. **Blueprint Editor UI tour**:
   - **Event Graph** (middle): where the majority of a Blueprint's
     actual logic/programming happens.
   - **Construction Script** (to the left of the Event Graph): not
     covered in this tutorial — mostly used by artists/technical
     artists, not core gameplay logic.
   - **Viewport** (further left): shows every object that makes up this
     Blueprint. Important terminology: inside a Blueprint, these
     objects are called **Components** — e.g. the camera and the
     character mesh are both components of the character Blueprint.
   - **Components panel**: functionally the Outliner, but scoped to
     this Blueprint — lists every component it contains. Selecting a
     component here highlights it in the Viewport and vice versa.
   - **My Blueprint panel** (below Components): contains every node and
     variable used anywhere in this Blueprint — e.g. clicking "Event
     Graph" under its Graphs section jumps straight to that graph.
5. **Details panel** still works the same way here as in the level
   editor — select a component (e.g. the character's mesh) to edit its
   properties, including swapping the mesh entirely (the default
   Third Person template ships a "female" mesh by default; selecting
   `SKM_Manny` instead swaps in the male mesh).
6. **Blueprint Viewport navigation** mirrors the level viewport: hold
   RMB to look around, press **F** to focus the camera on a selected
   component, scroll wheel to zoom. Two extras specific to this
   viewport: **Alt + left-mouse-button** drag rotates the camera around
   the selected object (combine with scroll to zoom), and holding **L**
   + left-mouse-button rotates the preview sun, letting you check how
   the Blueprint looks under different lighting angles.
7. **Play** works from inside the Blueprint editor too — opens the same
   playable preview window as the main editor's Play button. **Escape**
   exits.
8. **Compile button**: whenever you change a Blueprint (e.g. add a new
   node to the Event Graph), you need to **Compile** it for the change
   to take effect — either by clicking the Compile button directly, or
   simply by pressing **Play**, which automatically compiles every
   Blueprint the game needs first.
9. Every panel here is a dockable, tabbed widget — rearrange the
   Blueprint editor's layout the same way as the main editor (drag tabs
   to redock), and recover the default arrangement the same way too
   (**Window → Load Layout → Default Editor Layout**) if it gets messed
   up.

## Chapter 6: First Person Template

1. Before building the actual first-person shooter, download the
   tutorial's **custom free assets** (link in the original video's
   description) — needed to follow along with the rest of the project.
2. **Create a new project specifically for this game** (the Third
   Person project used so far was just for demonstrating Blueprints
   basics): File → New Project (or exit back to the Unreal Project
   Browser), **Games** category → **First Person** template this time.
3. **Future-proofing note**: if Epic ever changes or removes the
   built-in First Person template in a later engine version, start
   instead from the **"First Person Template"** project bundled inside
   the tutorial's own downloadable asset package — keeps the rest of
   the tutorial compatible regardless of Unreal version drift.
4. Download the tutorial's **"target game assets"** package (description
   link). **Important**: unzip it before opening — double-click the
   archive, drag it onto the Desktop (or wherever) to extract.
5. Once unzipped: close the Unreal Project Browser if it's open. The
   extracted project folder can be renamed to anything (the creator
   renames it "my first game"), then open that folder.
6. **Rename the project itself** (it's still internally named
   "FirstPersonTemplate" even after the folder rename): right-click the
   `.uproject` → **Rename**, or select it and press **F2** — rename to
   e.g. "my first game".
7. Double-click to open it in Unreal. This bundled template is very
   similar to Unreal's own built-in First Person template, with one
   deliberate difference: a gun is **already auto-spawned** when you
   press Play, specifically to make demonstrating Blueprint basics
   easier later in the tutorial.
8. **Quick demo of the template**: press **Play** — **WASD** to walk,
   **Space** to jump, **left mouse button** fires the built-in weapon
   (bouncing-ball projectiles). Firing at the included target boxes
   knocks them away via physics simulation. **Escape** to exit.
9. **Open the First Person Character Blueprint** to keep learning
   Blueprint basics: **Ctrl+Space** (Content Drawer) → First Person
   folder → Blueprints → double-click the character Blueprint.
10. Its Viewport shows: a **Capsule Collision**, a **Camera**, **Arms**,
    and a **Weapon** component — in this starter template, the weapon/
    gun is built directly into the first-person character Blueprint
    itself (not a separate pickup-able actor).
11. **Open its Event Graph** to introduce core Blueprint vocabulary
    before building anything from scratch:
    - Navigation: hold RMB to pan the graph, scroll wheel to zoom.
    - Reassurance: "don't worry if this looks complicated — we're going
      to build our own Blueprint from scratch very soon; this is just
      open as a reference to see what Blueprints are actually doing
      behind the scenes."
    - **Red nodes = Events**. An Event can be linked to other Blueprint
      logic, or tied directly to actual player input (e.g. a keyboard/
      mouse button press).
    - Walked-through example: an Event node that fires **when the
      player presses the left mouse button** — once triggered, an
      **executable wire** (the solid white connector line, distinct
      from the colored data-type wires used elsewhere in a graph) fires
      out to whatever node(s) it's connected to next.
12. **Reading the fire-weapon logic as a worked example**: when
    triggered, Unreal executes every connected node **in order**. For
    the left-mouse-button fire event: first an animation plays, then a
    **projectile bullet** is spawned (visualized as a yellow sphere),
    then a sound effect plays at that spawn location — all three nodes
    together make up the complete "fire" logic. A separate example
    nearby: a **Jump** action is bound to the Space Bar — pressing it
    makes the player jump, releasing it stops the jump.
13. **Watching nodes execute live** (debugging technique): move the
    Details panel aside for more graph space, then press **Play** —
    this opens a small standalone game window. Once you click into that
    window the editor loses mouse access; press **Shift+F1** to get the
    mouse cursor back without closing the game window. Resize/reposition
    that small game window (e.g. shrink it to the top-right corner) so
    both it and the Blueprint graph are visible at once.
    - To watch a *specific* Blueprint's nodes fire in real time: find
      the **"No Debug Object Selected"** dropdown (top of the Blueprint
      editor) and select the actual First Person Character instance —
      now walking around and pressing Space/firing in the live game
      window visibly lights up the corresponding nodes in the graph.
    - The **executable wire turns orange** while/after its event fires,
      confirming exactly which nodes just ran — described as one of
      Blueprints' biggest strengths: you can literally watch your
      game's logic execute in real time, which is a huge help when
      debugging.

## Chapter 6 (continued): Building your first node graph

Still within the Chapter 6 transcript segment (before the "Migrate
Assets" chapter heading appears), the creator walks through creating a
node and an event completely from scratch, as a small guided example:

1. **Create a node**: right-click anywhere empty in the graph to open
   the node-creation search menu.
2. Create an event linked to the keyboard: type **"keyboard F"** in the
   search and select it — now the event fires whenever the **F** key is
   pressed, and anything connected to it executes.
3. **Connecting nodes**: drag from an output pin and release over a
   target node's input — Unreal is smart enough to prompt for which
   node you want to connect to directly (the creator picks **Print
   String** to demo it).
4. **Breaking a connection**: hold **Alt** and left-click a wire to
   break it; connections can always be remade afterward.
5. **Connecting two pins without dragging**: hold **Shift**, click the
   first pin, then (still holding Shift) click the second pin — connects
   them automatically.
6. **Moving a pin's connection**: if you connect a pin to the wrong
   place, hold **Ctrl** and drag with the left mouse button to pull that
   connection out and reconnect it elsewhere.
7. **Duplicating a node**: hover over the node(s) to duplicate and press
   **Ctrl+D** (same shortcut as duplicating an object in the level).
   **Delete** removes a selected node.
8. **"Context Sensitive" search toggle**: if a node you're searching
   for by name doesn't show up, that's because Unreal's search is
   trying to intelligently guess which nodes are actually relevant to
   your current context. It's correct roughly 95% of the time, but for
   the rare cases it isn't, uncheck **Context Sensitive** in the search
   panel to see every possible node.
9. **Worked example — "Hello World" on keypress**:
   - Search (with Context Sensitive still on) for **Print String**,
     connect it after the F-key event.
   - Print String has a text field — set it to `Hello World!` and a
     **Duration** field (defaults to 2 seconds; changed to **5**).
   - Move the Print String output's message into view, press **Play**,
     press **F** in the game window — "Hello World!" appears in the
     top-left corner of the screen for the set duration. Spamming F
     re-triggers it each time.
   - Summary: this tells Unreal "whenever the player presses F, print
     Hello World to the screen" — deliberately simple logic just to
     demonstrate the mechanics, before moving into the actual shooter
     game logic next.

## Chapter 7: Migrate Assets

Bringing custom weapon/target assets from a *separate* downloadable
project into the main "my first game" project — the same **Migrate**
tool documented in the companion
`ue5-road-material-blending-magnet.md` tutorial, used here for a
different purpose (moving a handful of specific assets between two of
your *own* projects, not pulling in a whole third-party pack):

1. The assets to migrate ship inside a separate **"beginner game
   assets"** download (same link as earlier in Chapter 6). If not
   already downloaded, get it, then drag the zip onto the Desktop to
   unzip it.
2. This unzip produces a **brand new, separate Unreal project** — open
   it. It's an otherwise-blank project that exists solely to hold the
   assets to migrate: **Sci-Fi weapon** meshes (the gun the player will
   use) and **target meshes** (the objects to destroy).
   - Why these weren't bundled directly into the First Person template
     project from Chapter 6: this is specifically meant to demonstrate
     **migrating assets between two different projects**, a core skill
     for working with multiple projects/asset packs.
3. **Find your destination project's location first**: open "my first
   game" (saved on the Desktop in this case), go to its **Content**
   folder, and copy that folder's path/location.
4. **Perform the migration** (from the source "beginner game assets"
   project): select the relevant folders (hold **Shift** to multi-
   select), right-click → **Migrate**. Confirm migrating all the
   selected assets (**OK**).
5. When prompted for the destination, navigate to (or paste, if already
   copied) the target project's **Content** folder location, then
   **Select Folder** — copies the assets across into "my first game."
6. The source "beginner game assets" project is no longer needed after
   this — it can be deleted.
7. Back in the main project (**Ctrl+Space** to open the Content Drawer),
   the migrated **weapons** and **target** assets now appear, ready to
   use. Time to create the first custom Blueprint class.

## Chapter 8: Creating a Blueprint

Building a Blueprint completely from scratch for the first time (versus
just inspecting the existing First Person Character Blueprint earlier):

1. Navigate to the folder where the new Blueprint should live — the
   creator picks the **First Person → Blueprints** folder, to keep all
   custom programming logic organized in one place.
2. Right-click an empty area of the Content Browser → **Blueprint
   Class** (listed first in the creation menu — "the most important
   asset type in Unreal").
3. Unreal asks what **parent class** to base the new Blueprint on —
   select **Actor**. Reasoning: **Actors are anything that can be
   placed in the world** — a box, the sun, the sky are all Actors
   because they can all exist in the level. Since this Target object
   needs to be placed in the world, it has to be an Actor-class
   Blueprint.
4. Name it — the creator uses **`BP_Target`** (`BP_` prefix is just a
   personal naming convention for all Blueprints, not a requirement;
   you could just call it "Target"). **Rename an asset** anytime via
   right-click → Rename, or the **F2** shortcut (same as renaming
   project files, Chapter 6).
5. Double-click to open the new Blueprint — it's completely blank
   except for a small widget icon in the middle of the viewport,
   representing the Blueprint's **Scene Root** (its origin point).
6. **Adding the target mesh as a component**: in the Content Browser,
   navigate to the migrated **Target** static mesh asset — the
   transcript cuts off right as this step begins ("go to Target right
   here and we have that static mesh so there are two...").

*Transcript cuts off here, mid-sentence, right as the target mesh is
about to be added to the new Blueprint as a component.*

---

*To extend: send more transcript/screenshots from later parts of this
video (finishing the Target Blueprint, weapon/shooting logic, UI, Chaos
physics destruction, and adding the finished game to an environment)
and this file will be updated.*
