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
editor basics (chapters 3-4), Blueprint editor vocabulary (chapter 5),
node-graph fundamentals, migrating assets (chapter 6-7), a finished
`BP_Target` (chapter 8), a fully working score system (chapter 9), a
complete score UI (chapter 10), graph organization tools (chapter 11),
dynamic target counting plus a working win condition (chapter 12), a
complete `WBP_EndScreen` (chapter 13), and a fully working countdown
timer with a lose condition, including the `Expose on Spawn` technique
for passing a `Lost Game?` flag straight into the widget at creation
time (chapter 14, cut off right as the win/lose text branching is
about to be wired up). Chaos physics destruction and final environment
assembly haven't been covered yet.

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
6. **Adding the target mesh as a component** — two ways:
   1. Drag the migrated **Target** static mesh asset directly on top of
      the default Scene Root in the Blueprint's Viewport and release —
      adds it immediately (**Ctrl+Z** undoes it).
   2. Or: **+ Add** → search "static mesh" → add a **Static Mesh
      Component**, then in that component's own **Mesh** dropdown,
      type/select "Target".
   - The drag-onto-root method (#1) is the quicker of the two.
7. **Compile**.
8. **Place it in the world**: drag `BP_Target` from the Content Browser
   (First Person → Blueprints folder) into the level. Since it's a
   Blueprint, **Alt+drag** duplicates it around the level same as any
   other object (disable snapping first, as covered in Chapter 4).
9. **Shortcut — reopening a placed Blueprint's editor quickly**: select
   a placed Blueprint instance in the level and press **Ctrl+E** to
   open its asset editor directly, instead of manually hunting for it
   in the Content Browser.
10. **Adding hit-detection logic**: select the **Static Mesh component**
    (not the Scene Root) in the Blueprint, scroll down the Details
    panel to find **"On Component Hit"**, click its **+** to create
    that event. Two other similar-but-unneeded hit-related event stubs
    appear alongside it by default — delete those, only the one needed
    is kept.
11. Connect a **Print String** to confirm it's firing: text set to
    `Target hit!`, text color changed to **reddish** (plain
    white/default text is hard to read against the blue sky
    background), **Duration** set to **5** seconds.
12. Press Play, fire the weapon at a target — confirms the event fires
    ("Target hit!" prints).
    - **Bug found**: simply *walking into* / touching the target also
      triggers it — because **On Component Hit** fires for literally
      any actor that collides with the mesh, not just the projectile.
13. **Fix — restrict the event to projectile hits only**: drag from the
    event's **Other Actor** output pin, type **"Cast To"**, and select
    the projectile Blueprint's class — `BP_FirstPersonProjectile` (the
    bullet/sphere spawned when the weapon fires). This inserts a
    **Cast** node.
    - Brief explanation of casting (described as "a whole other
      lesson," kept short here): the Cast node asks "is the actor that
      just hit my static mesh actually a First Person Projectile?" — if
      **yes**, everything connected to its success output executes; if
      **no**, that logic simply doesn't run.
14. **Re-test the fix**: delete two of the three placed Targets to
    simplify testing, scale up the remaining one, reopen the
    `BP_Target` Blueprint, press Play:
    - Firing at the target still correctly prints "Target hit!".
    - Walking directly into the target now does **nothing** — execution
      reaches the Cast node and stops there, since the player character
      isn't a `BP_FirstPersonProjectile`. Bug confirmed fixed.
15. **Next requirement**: track *how many* targets have been hit (so the
    game can later detect when all targets are destroyed and the player
    wins) — this needs somewhere to actually store that count, which
    leads into Chapter 9.

## Chapter 9: Gamemode

1. **What a Game Mode is**: a Blueprint that governs a game's overall
   rules/features — e.g. in Capture the Flag, the Game Mode tracks how
   many flags each team has captured. In this project, the Game Mode
   will track how many targets have been hit and the countdown timer.
   - The First Person template already ships with a default Game Mode,
     but the tutorial deliberately builds a new one from scratch to
     demonstrate the process.
2. **Create it**: right-click in the Content Browser → **Blueprint
   Class** → search/select **Game Mode Base** as the parent class →
   name it **`GM_TargetGame`** (`GM_` prefix, same personal-convention
   pattern as `BP_` for regular Blueprints).
3. Open it. Unlike an Actor Blueprint, a Game Mode Blueprint opens
   straight to a Details-style defaults panel rather than a Viewport —
   a Game Mode isn't itself a placeable world object, it governs rules
   instead.
4. **Set Default Pawn Class**: controls which Blueprint the player
   actually controls/possesses. Currently set to the generic "Default
   Pawn" — change it to **`BP_FirstPersonCharacter`**.
5. **Assign this Game Mode to the level**: back in the main map, open
   **Window → World Settings** (hidden by default — same "open a
   non-default window" technique as Chapter 4), find **Game Mode
   Override**, and select the new `GM_TargetGame`.
6. **Add a crosshair/reticle**: nothing shows on-screen to indicate aim
   point by default. In the same World Settings area, under **HUD**,
   select **"First Person HUD"** — a widget asset that came in with the
   assets migrated back in Chapter 7 — and assign it as this Game
   Mode's HUD.
7. Press Play — confirms a small crosshair now appears centered on
   screen.
8. **Tracking the hit count — Variables**:
   - Concept: variables store data, same as in any programming
     language.
   - Create one: in the Game Mode Blueprint's **My Blueprint** panel,
     click **+** next to Variables, name it (demo uses `MyVar`), choose
     its **type** — selects **Integer** (a whole number).
   - **Compile** — a newly created variable can't actually be dragged
     into the graph until it's been compiled at least once.
   - Set a default value directly in the Details panel while the
     variable is selected (demo sets **20**).
   - Drag the variable into the Event Graph — prompts a choice between
     **Get** (reads the current value) and **Set** (overwrites it).
     Dragging it also auto-creates two placeholder custom-event node
     stubs, which get deleted since they aren't needed here.
   - **Demo — reading it on game start**: bring back the **Begin Play**
     event (fires automatically once, at the very start of the game) →
     connect **Get MyVar** → **Print String** (Print String's text
     input pin automatically converts the integer into text) → set the
     text color to red for visibility against the sky → **Compile**.
   - Confirm the level's World Settings still has `GM_TargetGame`
     selected, so this Blueprint's Begin Play actually fires.
   - Press Play — **"20"** prints in the top-left corner, confirming the
     variable correctly holds and outputs its stored value.
   - **Changing a variable's value at runtime**: drag the variable out
     again, this time choosing **Set** instead of Get — lets you
     overwrite its stored value during gameplay. Demo: set it to
     **-5** instead of its default 20, wire that into Print String —
     confirms the value starts at 20, is immediately overwritten to -5
     by `Set`, and -5 is what actually prints. This confirms how `Set`
     works before using it for real.
9. **Creating the real score-tracking variable**: delete the demo
   variable, create a new one named **`CurrentScore`**, type
   **Integer**.
10. Drag it into the graph as **Get**, then drag from its output and
    type **"++"** — selects the **Increment Integer** node, which adds
    1 to the variable's current value and sets it in one step (e.g. 3
    becomes 4).
11. **Calling this from the Targets**: the increment logic needs to be
    triggered by `BP_Target` whenever a target is actually hit — wrap
    it in a **Custom Event**: right-click → type "custom events" →
    Enter → name it **`Add Score`** → connect it to feed into the
    Increment Integer node. Add a **Print String** after the increment
    too (Duration **5**, text color **orange**) to visually confirm the
    score as it changes.
12. **Cross-Blueprint calling** — back in `BP_Target`'s event graph
    (where `On Component Hit` → `Cast To BP_FirstPersonProjectile`
    already lived from Chapter 8): right-click → type **"Get Game
    Mode"** → returns the world's current Game Mode, but only as a
    generic type. Drag from its output, type **"Cast To
    GM_TargetGame"** → narrows it to the specific Game Mode class. From
    that cast's output, drag again and type **"Add Score"** → Enter —
    this calls the custom event just created in the Game Mode directly
    from the Target. (Double-clicking an `Add Score` call node jumps
    straight to that event's definition, for quick navigation between
    Blueprints.)
13. Press Play, fire at the first target — confirms **"1"** prints (then
    2, then 3 for subsequent distinct targets) — cross-Blueprint custom
    event calling confirmed working.
14. **Bug found — exploit**: repeatedly hitting the *same* target over
    and over keeps incrementing the score each time, letting a player
    "win" by spamming one target instead of hitting all of them. Each
    target needs to only count once.
15. **Fix — a per-target Boolean flag**: in `BP_Target`'s Variables,
    create a new one — default type is **Boolean**, change via the
    type dropdown if needed — name it **`IsHit?`** (question-mark
    naming convention for booleans, a personal style choice, not
    required). This flag tracks whether *this specific target
    instance* has already registered a hit.
16. **Branch (the if-statement equivalent)**: described as "probably
    the most essential node in Unreal Engine, or in programming in
    general." Right-click → type "if" → select **Branch** (Unreal's
    name for an if-statement), or use the shortcut: hold **B** and
    left-click in the graph to create one directly.
17. **Wiring the full fixed flow**: `On Component Hit` → `Cast To
    BP_FirstPersonProjectile` (success) → **Branch** on `Get IsHit?` →
    - **True** pin (already hit): left unconnected — nothing happens.
    - **False** pin (not yet hit): → **Set IsHit? = True** (marks this
      target as hit, so it won't pass this check again) → → `Cast To
      GM_TargetGame` → `Add Score`.
18. **Re-test**: hitting a target once adds to the score; hitting the
    *same* target again does nothing (the Branch's True pin catches it
    and stops); hitting the other distinct targets each adds correctly.
19. **Optional cleanup/aesthetic tip** (not functionally required): to
    have the main logic chain hang off the Branch's **True** pin
    instead of False (purely for a visually tidier graph), insert a
    **NOT Boolean** node between `Get IsHit?` and the Branch's
    condition input — inverting the check to "is NOT hit," so the main
    flow now reads as the True case.
20. **More node shortcuts**:
    - **Reroute/"Knot" node**: lets you bend a wire's path for
      readability without changing what it connects — referred to in
      the transcript as "adding a knot."
    - **Ctrl+drag** a variable into the graph to auto-create a **Get**
      node directly (skipping the Get/Set choice popup).
    - **Alt+drag** a variable into the graph to auto-create a **Set**
      node directly.
21. **Recap of the finished Target-hit logic** (in the creator's own
    words): "This event will run whenever our Target is hit, then we
    check if it was the First Person Projectile that hit it, and if it
    was we check whether this target has already been hit — and if it
    hasn't, we set that variable to true so these nodes won't run again
    in the future, then we tell the Game Mode to add a score to our
    CurrentScore."
22. In-game test confirms the score now correctly climbs 1, 2, 3 across
    the three distinct targets — "the game is slowly forming," but with
    one acknowledged problem: relying on a `Print String` to show the
    score "looks kind of ugly" and isn't a real UI — motivating Chapter
    10.

## Chapter 10: User Interfaces

1. Unreal's UI-building tool is **UMG** — "Unreal Motion Graphics UI
   Designer." Goal here: build a real on-screen UI showing the player's
   score (how many targets hit / remaining), replacing the Print String
   placeholder.
2. **Save everything first** — Save All / Save Selected — explicitly
   called out as important practice before this next step.
3. **Create a Widget Blueprint**: right-click in the Content Browser →
   scroll down to **User Interface** → **Widget Blueprint** → choose
   the basic/default widget type → name it **`WBP_UI`** (`WBP_` prefix
   convention for Widget Blueprints, `UI` suffix since this will be the
   player's main on-screen interface during gameplay).
4. Double-click to open it — shows the widget designer canvas. In the
   top-left is the **Palette**, containing every UI element type that
   can be displayed to the player.
5. **Canvas Panel**: the very first element any new Widget Blueprint
   needs — drag one in before anything else. It's the root container
   everything else gets placed inside.
6. Move the Details panel aside for a clearer view. Navigation controls
   in the designer are the same as the Blueprint graph: hold RMB to
   pan, scroll wheel to zoom.
7. **Adding text**: drag a **Text** element from the Palette onto the
   canvas.
8. **Anchors** (the small flower-shaped icon on a selected widget):
   control how that element repositions itself relative to the screen
   as the window is resized — this is UMG's equivalent of responsive
   web design. Either drag the anchor icon directly to a corner (e.g.
   top-left), or use the **Anchors** dropdown in the Details panel to
   pick a preset (top-left, top-right, center, etc.).
   - Each added text element also gets renamed in the **Hierarchy**
     panel for organization (distinct from the actual text it
     displays) — e.g. the first one is named **"Top Left"**.
9. **Demonstrating anchors**: duplicate the text element (**Ctrl+C /
   Ctrl+V**), drag the copy to the top-right corner, set its anchor to
   top-right, rename it "Top Right." Duplicate again, drag to the
   center, set its anchor to Center, rename it "Center."
   - Press **Compile**, then **Play** — resizing the game window shows
     the Center text staying centered and the Top Left/Top Right texts
     staying pinned to their respective corners regardless of window
     size — exactly what anchors are for, since not every player's
     window is the same resolution/aspect ratio (ultrawide monitors,
     1:1 setups, etc. all need the UI to stay correctly positioned).
10. Delete the "Center" and "Top Right" demo texts — only "Top Left" is
    actually needed for the real score display. Rename it **"Score"**.
11. **Resize the text**: default size is too small. Select it →
    **Appearance → Size** — tries **64** (too large, would dominate the
    screen), settles on **45-50** as a reasonable final size.

**Wiring the score display to real data** (the Widget Blueprint's own
Graph tab, not just the static Designer view):

12. Clean the graph of any leftover demo nodes. Rename the Text widget
    to **"Score Text"** in the Hierarchy, for a clear, easy-to-find name
    once referencing it from code.
13. **Expose it to the graph**: select the Score Text widget, enable its
    **"Is Variable"** checkbox (this is what makes a design-time widget
    element referenceable from Blueprint logic) — then drag it into the
    graph as **Get Score Text**.
14. Drag from that output, type **"Set Text"**, select the Set (Text)
    node — this is what actually changes the text displayed on screen.
    Demo: feed in the literal text `Hello World` and connect to **Event
    Construct** (widgets don't have `Event Begin Play` — their
    equivalent, which fires as soon as the widget itself is created, is
    called **Event Construct**).
    - Press Play — "Hello World" now shows where "Score" used to be,
      confirming the Set Text wiring works.
15. **Wiring in the real score value**: need `CurrentScore` from the
    Game Mode instead of a literal string:
    - Drag out, type **"Get Game Mode"**, drag from its output, type
      **"Cast To GM_TargetGame"** (same casting pattern as `BP_Target`
      in Chapter 9), then from that cast's success output drag and type
      **"Get Current Score"**.
    - An Integer can't plug directly into Set Text's Text input — hover
      the pin and Unreal auto-offers a conversion node (int-to-string,
      shown in the purple "String" wire color) — accept it.
    - Compile, Save. Firing at targets still doesn't update the display
      yet, though.
16. **The real problem**: `Event Construct` only fires *once*, when the
    widget is first created — so this logic runs a single time and
    never again, instead of updating every time a target is hit. The
    Set Text logic needs to be called again each time `Add Score` runs
    in the Game Mode.
17. **Getting a reference to this specific widget instance** (needed so
    the Game Mode can call logic *inside* it, not just its generic
    class):
    - Back where the Game Mode originally creates the widget (`Event
      Begin Play` → `Create Widget` → `Add to Viewport`, from Chapter
      9): drag from the **Create Widget** node's **Return Value**
      output pin — this holds a reference to the exact widget instance
      just created.
    - **Shortcut — Promote to Variable**: right-click directly on that
      output pin and select **"Promote to Variable"** — automatically
      creates a correctly-typed variable (here, one that can hold a
      `WBP_UI` reference) without manually going through the Variables
      panel's **+** button. (This works on essentially any output pin —
      also handy for quickly promoting an Integer or other value to a
      variable.)
    - Alternative manual method also shown: creating a variable and
      typing the specific widget class name (`WBP_UI`) instead of
      picking from the normal type list, then choosing **Object
      Reference** as its type.
    - **Alt+drag** this new variable into the graph to auto-create a
      **Set** node, and plug the Create Widget node's Return Value into
      it — stores the widget reference for later use.
18. **Calling into the widget from the Game Mode's Add Score event**:
    Ctrl+drag the widget-reference variable into the `Add Score` custom
    event's graph as a **Get**, then drag from it and call a new custom
    event to be created in the widget — **"Update Score"**.
    - Delete the earlier debug `Print String` node from `Add Score`
      (no longer needed now that real UI exists) and route this call to
      Update Score in its place.
19. Press Play — the score display now correctly updates to 1, 2, 3 as
    targets are hit, driven by the real `Add Score` → `Update Score`
    call chain instead of a one-time `Event Construct` run.
20. **Formatting the display text** — want it to read "Score 1" instead
    of a bare "1":
    - Back in the Widget Blueprint's graph: drag from an input pin and
      type **"append"** (another case where **Context Sensitive**
      needs to be unchecked if the node doesn't show up, per the
      Chapter 6 note on that toggle) → select the **Append** node,
      which combines two text pieces into one. It auto-creates two
      helper string-conversion nodes alongside it.
    - Wire: Sentence A = the literal text `Score ` (trailing space),
      Sentence B = the `CurrentScore` integer (auto-converted to text).
      Append combines them into e.g. "Score 1", "Score 2", etc.
    - Compile, Save, Play — confirms "Score 1" / "Score 2" / "Score 3"
      now displays correctly as targets are destroyed, completing the
      working score UI.
21. **Simplifying with Custom Event input parameters**: the widget's
    `Update Score` event currently does its own `Get Game Mode → Cast
    To → Get Current Score` chain internally, which is redundant since
    the Game Mode already has that value when it calls the event.
    Cleaner approach — **give the custom event an input parameter**:
    - Select the `Update Score` custom event, in its Details panel find
      **Inputs**, click **+**, name the new input **"Current Score"**,
      type **Integer**.
    - The event node now exposes a `Current Score` input pin directly —
      use that inside the widget's graph instead of re-fetching the
      value.
    - Back in `GM_TargetGame`: the call to `Update Score` now shows a
      matching `Current Score` input pin — plug the `CurrentScore`
      variable straight into it when calling.
    - This removes the need for the widget to know anything about the
      Game Mode at all — it just receives the value it needs as a
      parameter. Compile, re-test — confirms it still works, with a
      simpler graph.

## Chapter 11: Organize Nodes

1. **Bug — score starts at a random/leftover value**: nothing explicitly
   resets `CurrentScore` to 0 display when the game starts. Fix: call
   `Update Score` (with `Current Score = 0`) from `Event Begin Play` in
   the Game Mode too, not just from `Add Score`.
2. **Graph organization tools** (purely cosmetic, demonstrated while
   wiring the above):
   - **Reroute node**: hover over any wire and **double-click** to
     insert a reroute point, letting you bend the wire's path for
     readability without changing what it connects.
   - **Comment boxes**: hover over a group of nodes and press **C** to
     wrap them in a labeled comment box (e.g. "Add Score by calling the
     widgets") — helpful for yourself or teammates to understand a
     graph section at a glance. Individual nodes can also get their own
     small comment (hover the node, click its comment icon, type text).
     Comments can be removed the same way they're added.
3. Save everything. Test: 3 targets in the world, hit 1, 2, 3 — confirms
   the counter and reset-at-start logic both work correctly.

## Chapter 12: Get Targets

1. **New variable**: `MaxScore` (Integer) in `GM_TargetGame`.
   `CurrentScore` = how many targets have been hit so far; `MaxScore` =
   how many targets exist in total / need to be hit to win.
2. **Counting targets dynamically** (rather than hardcoding a number) —
   in `Event Begin Play`:
   - Drag out, type **"Get All Actors of Class"**, specify the class as
     `BP_Target` — returns a reference to every Target actor currently
     in the level.
   - This returns an **array** (shown as a small-squares icon pin) —
     explicitly flagged as out of scope for this tutorial ("we are not
     going over arrays in this video"), but conceptually: it's a list
     holding every Target actor found.
   - Drag from that array output, type **"Length"** — gives the actual
     count of targets found.
   - **Alt+drag** the `MaxScore` variable in to auto-create a **Set**
     node, and wire the Length output into it — `MaxScore` now reflects
     the real number of targets placed in the level at game start,
     rather than a hardcoded number.
3. **Showing progress as "X/Y"**: add another **Input** parameter to the
   widget's `Update Score` custom event — **"Max Score"**, Integer.
   - In the Append logic from Chapter 10, change the formatting to
     combine `CurrentScore`, a literal `/`, and `MaxScore` — so the
     display reads e.g. **"0/3"** instead of just a bare number.
   - Back in `GM_TargetGame`: both the `Add Score` call **and** the
     `Event Begin Play` call to `Update Score` need to pass `MaxScore`
     into this new input pin too (Ctrl+drag `MaxScore` in and connect it
     at both call sites) — otherwise the initial display would show
     "0/0" instead of "0/3".
4. Press Play — confirms "0/3" at the start, then "1/3", "2/3", "3/3" as
   targets are hit.

**Win condition**:

5. After the score-update logic in `Add Score`, add a **Branch** (hold
   **B** + click, or right-click → "if").
6. **Comparing CurrentScore to MaxScore**: drag from `CurrentScore`,
   type `==` (or "equal"), select the integer equality comparison node,
   plug `MaxScore` into its other input. Wire this Boolean result into
   the Branch's condition.
7. If **True** (scores are equal — every target has been hit), that's
   the win condition. For now, before building a proper end screen,
   confirm it with a placeholder `Print String`: "Congrats, you won!"
   with a smiley face, default duration — text color needs setting to
   something visible against the sky (plain white/default text is easy
   to lose, same issue as earlier Print Strings in this project).

## Chapter 13: Win Screen

1. **Shortcut**: **Alt+P** plays the game directly — equivalent to
   clicking the Play button, but faster to trigger repeatedly while
   testing.
2. Testing confirms hitting all 3 targets fires the win Print String —
   but a tiny debug message isn't something an actual player would
   notice or understand as "the game is over, stop playing."
3. **Build a proper End Screen widget**, same process as the score UI:
   Ctrl+Space → right-click → User Interface → Widget Blueprint → name
   it **`WBP_EndScreen`** — this single widget is planned to handle
   *both* the win screen and (implied) a lose screen.
4. Open it: first step for any widget (again) is adding a **Canvas
   Panel**. Side note from the creator: in Unreal Engine 4 this used to
   be added automatically by default; in UE5 it must be added manually
   every time.
5. Add a **Text** element, place it centered on screen, make it fairly
   large (**Size 60**, then bumped even larger).
6. **Justification**: select the middle/center justification option so
   the text's own internal alignment stays centered (distinct from the
   Anchor, which positions the whole element on screen — Justification
   controls alignment *within* the text box itself).
7. **Drop Shadow polish** (text looked "a little bland" without it):
   - Find the text's **Shadow Color** property, increase its **Alpha**
     (transparency) value — default is **0** (fully transparent/
     invisible shadow); raising it toward **1** makes the shadow fully
     opaque (black by default).
   - Adjust **Shadow Offset** to nudge the shadow's position relative to
     the text for a better-looking effect.
8. Set placeholder text content — a short celebratory message with a
   smiley face (exact wording unclear from the transcript's
   speech-to-text rendering; treated as a placeholder the creator says
   will be edited again shortly, not final copy).
9. **Displaying this widget when the player wins**: back in
   `GM_TargetGame`'s win-condition Branch (True pin) — delete the
   earlier placeholder `Print String`.
   - Drag from the Branch's **True** pin, type **"Create Widget"**,
     select `WBP_EndScreen` as the class. From its **Return Value**,
     drag out and connect to **"Add to Viewport"**.
10. Compile. Testing confirms the win screen now appears when all
    targets are hit — but two problems remain: the player can still
    move around in the background, and there's no way to play again.
11. **Add a Restart button**: in `WBP_EndScreen`, drag in a **Button**
    widget, set its Anchor to **Center**, resize it, add a **Text**
    child reading "Restart?".
    - Style fix: the button is too bright by default — **Style →
      Normal → Tint** → decrease to something darker.
12. **Stopping gameplay and restoring the mouse on win**: back in
    `GM_TargetGame`, after `Create Widget → Add to Viewport`:
    - Drag out, add **"Set Input Mode UI Only"**, targeting the
      End Screen widget — restricts player input to the UI only (no
      more WASD/shoot while the end screen is up).
    - Drag from **Get Player Controller**, add **"Show Mouse Cursor"**,
      set to **true** — makes the cursor visible again (it's hidden
      during normal FPS gameplay), so the player can actually click
      Restart without needing the editor-only Shift+F1 shortcut.
13. **Wiring the Restart button**: select it in `WBP_EndScreen`, scroll
    its Details panel down, create an **On Clicked** event (default
    name is an unclear auto-generated one like "OnClicked
    (Button_0)" — rename the node to **"Restart Button"** for clarity).
    - Drag out, add **"Open Level (by Object Reference)"**, and set its
      Level input to the current level (`First Person Map`) — reloads
      the entire level fresh, resetting everything.
14. **Bug — after restarting, the player can't move**: the input mode
    is still set to UI Only from the win screen and never gets reset.
    **Fix**: in `GM_TargetGame`'s `Event Begin Play` (which runs again
    on every level load, including after a restart), add `Get Player
    Controller` → **"Set Input Mode Game Only"** — ensures every fresh
    start/restart resets input back to normal gameplay controls.
15. **Remaining issue — residual momentum on win**: if the player is
    mid-movement when they land the final hit, their character keeps
    sliding forward briefly even with input now blocked, since existing
    momentum isn't input. **Fix**: on win (alongside the input-mode/
    mouse-cursor nodes), drag from the Player Controller again and add
    **"Set Ignore Move Input"** — immediately halts all movement
    processing for the character the instant the win screen appears,
    regardless of any momentum already in progress.
16. Full flow re-tested and confirmed: hit all targets while running →
    character stops dead, mouse cursor appears automatically, click
    Restart → level reloads with movement fully working again.
17. **Polish — blurred background on the end screen** (currently looks
    "kind of bland"):
    - In `WBP_EndScreen`'s Designer, search the Palette for "blur",
      drag in a **Background Blur** element.
    - Resize it to fill the entire canvas, set its Anchor to full-
      screen stretch (same anchor concept as the score UI, so it covers
      the screen at any window size).
    - With it selected, increase **Blur Strength** to **2**.
    - **Troubleshooting — the blur covers/hides the text and button**:
      caused by Hierarchy ordering. Unlike Photoshop-style layer lists,
      **Unreal's Hierarchy panel stacks bottom-to-top** — an element
      lower in the list renders *underneath* elements above it. Since
      Background Blur was added last (at the bottom), it was rendering
      on top of everything. **Fix**: drag the Background Blur entry up
      in the Hierarchy so it sits directly after the Canvas Panel
      (i.e., first/bottommost child) — the text and button now
      correctly render on top of the blur instead of being hidden
      behind it.
18. **Recap of the whole system so far** (in the creator's own words):
    `BP_Target` is a static mesh that checks whether a projectile hit
    it; if so, adds a score to the Game Mode and marks itself so it
    can't be hit again. The Game Mode does most of the work: at `Event
    Begin Play` it counts how many Targets exist in the world and sets
    that as `MaxScore` (confirmed dynamic — adding a 4th Target in the
    level makes the max automatically become 4 instead of 3), creates
    the score UI widget, adds 1 to `CurrentScore` and updates the UI
    whenever a Target is hit, and checks whether `CurrentScore` equals
    `MaxScore` — if so, showing the End Screen and stopping the player.

## Chapter 14: Timer (partial — cut off mid-explanation)

1. **Motivation**: the game currently has no time pressure — the player
   has unlimited time to hit every target, which isn't very
   challenging. Plan: add a countdown timer; if it expires before all
   targets are hit, the player **loses** — the game now has two
   possible outcomes (win or lose), not just one.
2. **Level prep — spread the targets out** for the timer to actually
   matter: reposition the 3 existing targets further apart in the
   level, vary their size (make one bigger than another) for visual
   interest.
3. **Troubleshooting — a Target rotates oddly / doesn't visibly "face"
   anywhere**: caused by the specific mesh variant being used (a
   rotationally-symmetric sphere shape by default in this asset, which
   looks the same no matter how it's rotated). Fix: swap to a different
   mesh variant within the same asset (e.g. a cube-shaped option
   instead of the sphere icon) so rotation now has a visible effect.
4. Reposition the Directional Light (**Ctrl+L**, same technique as
   throughout this and the companion tutorials) for the new target
   layout.
5. **Player Start actor**: without one in the level, pressing Play
   spawns the player wherever the editor camera currently happens to
   be — unpredictable. Adding a dedicated **Player Start** (Place
   Actors panel → Basics category) lets you fix exactly where and which
   direction the player spawns, regardless of the editor camera's
   position. Angle it to face the targets.
   - **Tip — testing from the current camera view instead**: click the
     small 3-dot menu next to the **Play** button → under its Spawn
     Player options, choose **"Current Camera Location"** instead of
     **"Default Player Start"** for quick iteration without needing to
     reposition the camera to match the Player Start each time; switch
     back to **"Player Start"** afterward for normal testing.
6. **Building the timer logic**: in `GM_TargetGame`'s event graph,
   select the `Add Score` event and its whole connected node group,
   nudge it down to make room above for the new timer logic.
7. At the very end of `Event Begin Play` (after the initial score UI
   setup), drag out Unreal's built-in **"Set Timer by Event"** node —
   this schedules a given custom event to run after a delay (and
   optionally repeatedly).
   - **Correction from the previous capture**: "Set Timer by Event" is
     the built-in scheduling node itself, not something you name
     yourself — you separately create your *own* custom event and plug
     it into this node's **Event** input. Create one called
     **"Decrease Counts"** and connect it.
8. **How Set Timer by Event works** (demonstrated step by step):
   - It needs a **Time** input (seconds until the connected event
     fires) — set to **1** second initially.
   - Demo: wire a `Print String` ("Decrease Count is activated") off
     the `Decrease Counts` event, press Play — confirms it fires once,
     after 1 second, then **stops** (doesn't repeat by default).
   - Enable the **Looping** checkbox on Set Timer by Event — now the
     event re-fires every interval indefinitely (1s, 2s, 3s, ...).
   - Lower Time to **0.1** seconds — fires much more frequently.
9. **The actual countdown variable**: create `Time` (Integer), default
   value **500** — a difficulty-tunable "unit count," not literal
   seconds (its real duration depends on both this starting value and
   the tick rate below).
   - Inside `Decrease Counts`: Ctrl+drag `Time` in as **Get**, subtract
     1 (the `--` decrement node), **Set** it back. Delete the debug
     Print String.
   - **Tick rate**: lower Set Timer by Event's Time input further, to
     **0.01** seconds (100 ticks/second) — so even though `Time` only
     decrements by 1 per tick, it visibly counts down fast from 500 to
     0 (and, unaddressed at this point, keeps going negative).
10. **Displaying the timer in the UI**: duplicate the Score Text
    (Ctrl+C/V), set its displayed text/name to "Time," anchor it to the
    **top-right** corner, rename the widget itself **"Time Text"** in
    the Hierarchy.
    - In the UI's graph: create a new Custom Event **"Update Time"**
      with an Integer input (same pattern as `Update Score` /
      `Current Score` from Chapter 10).
    - `Get Time Text` → `Set Text`, formatted through an **Append**
      node: Sentence A = literal `"Time "`, Sentence B = the integer
      input (auto-converted) — combines into "Time 500", etc.
11. **Calling Update Time from the Game Mode**: after decrementing
    `Time` in `Decrease Counts`, call the stored widget reference's
    `Update Time` event, passing the new value. Also call it once from
    `Event Begin Play` (so the display shows the correct starting value
    immediately, before the first tick) — copy the two nodes
    (`Get User Interface` → `Update Time` call) to both places, reusing
    the existing widget-reference variable rather than re-fetching it.
12. Play — confirms a working on-screen countdown from 500 to 0 (still
    continuing into negative numbers at this point, fixed next).
13. **Tuning difficulty**: the starting `Time` value is the main lever —
    tried **100** (ends almost instantly, too fast), settled on **400**
    as a reasonable value for this game.

**Lose condition**:

14. Compare `Time` to 0: drag from `Time`, type `<=` ("less than and
    equal"), check against **0**. Hold **B** + click for a **Branch**,
    feed in this comparison's result.
    - If **True** (time's up): placeholder `Print String` — "YOU LOST"
      — to be replaced with the real End Screen shortly.
15. **Bug — the lose condition keeps re-firing**: since the Set Timer
    loop keeps ticking every 0.01s indefinitely, once `Time` hits 0 the
    lose branch re-triggers on every subsequent tick too, not just
    once.
16. **Fix — a `Game Over?` Boolean gate**: create `Game Over?`
    (Boolean), set it to **true** inside the lose branch (and,
    implicitly, the win branch too) once the game actually ends.
    - At the very start of `Decrease Counts`, before doing anything
      else: Ctrl+drag `Game Over?` in as **Get**, run it through a
      **NOT Boolean**, and gate the rest of the tick logic behind a new
      **Branch** on that — the timer only keeps decrementing/checking
      while the game is *not* already over.
    - Re-tested: `Time` now counts down and stops cleanly at 0, "YOU
      LOST" prints exactly once.
17. **Replacing the placeholder with the real End Screen** — reusing
    the win condition's existing widget-creation logic (`Create Widget`
    → `Add to Viewport` → `Set Input Mode UI Only` → `Show Mouse
    Cursor` → `Set Ignore Move Input`), since it's identical between
    win and lose except for the displayed message:
    - Select that whole node group from the win branch, **Ctrl+C/V** to
      duplicate it, wire the lose Branch's True pin into the copy.
    - **Problem**: this produces two *separate* End Screen creation
      calls that happen to show the exact same hardcoded "You Won!"
      text — losing would incorrectly display a win message, and
      duplicating the whole widget just to swap text is wasteful.
18. **Fix — a `Lost Game?` flag passed in via "Expose on Spawn"** (a
    genuinely useful, reusable technique for initializing a widget with
    data right at creation time, rather than calling a separate custom
    event afterward):
    - In `WBP_EndScreen`: create a Boolean variable **`Lost Game?`**
      (default **false** — false = player won, true = player lost).
    - Select this variable in the Variables panel, enable
      **"Instance Editable"** and, crucially, **"Expose on Spawn"**.
    - Back in the Game Mode: the **Create Widget (WBP_EndScreen)**
      node now shows a new input pin for `Lost Game?` directly on the
      node itself — set it to **True** on the lose path's Create
      Widget call, leave it at its default (False) on the win path's —
      no second widget or custom event call needed just to pass this
      one flag in.
    - **Troubleshooting — the new pin doesn't appear**: right-click the
      `Create Widget` node and select **"Refresh Nodes"** to force
      Unreal to re-scan the widget class and expose the newly-added
      spawn parameter.

*Transcript cuts off here, right as the creator begins explaining how
the win path explicitly sets `Lost Game?` to false ("now down here when
the player wins the game we want to make...") — likely continues into
using this flag inside `WBP_EndScreen`'s `Event Construct` to actually
switch the displayed text between "You Won!" and "You Lost!".*

---

*To extend: send more transcript/screenshots from later parts of this
video (finishing the win/lose text branching, Chaos physics
destruction, and adding the finished game to an environment) and this
file will be updated.*
