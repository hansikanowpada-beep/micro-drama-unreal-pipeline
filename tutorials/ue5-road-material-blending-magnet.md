# Tutorial notes: UE5 road creation and multi-layer blend materials

Source: a different YouTube tutorial, same channel as
`ue5-environment-basics-magnet.md` (creator name transcribed as "Omitage"
this time — likely the same "Amit"/Magnet channel, speech-to-text just
rendered the name differently). Captured from the video transcript
(screenshots, not watched directly) — double-check exact button labels
against the live video, but the operation sequence below is accurate to
the transcript.

This is a **separate** video from the character/cinematics one — this
one is specifically about building a custom road/ground surface using a
multi-layer blend material system, not character animation or Sequencer
work. Kept as its own file per the note at the end of the other one.

Status: **partial capture** — covers through the start of mesh-paint
layering (chapter 4, cut off mid-sentence). More to be added as further
transcript/screenshots are shared.

## Chapter 1: Introduction

- Creating an environment/ground scene in **Unreal Engine 5.8**.
- The finished map is available free via the creator's Patreon link (in
  the original video's description).

## Chapter 2: Scene setup and foundation

1. Launch Unreal Engine → **New Project** → **Games** category → select
   the **Third Person** template → name the project → **Create**.
2. **File → New Level → Empty Level → Create**.
3. Quick environment lighting setup via **Window → Environment Light
   Mixer** — this panel has one-click buttons to add each of:
   - **Create Skylight**
   - **Create Directional Light**
   - **Create Sky Atmosphere**
   - **Create Volumetric Cloud**
   - **Create Height Fog**

   (This is a faster path to the same base environment actors built
   manually one-by-one in the other tutorial's Chapter 3.)
4. In the Height Fog's settings (still in the Light Mixer or via its
   Details panel), enable **Volumetric Fog**, then close the Environment
   Light Mixer window.
5. **Landscape**: Selection Mode dropdown → **Landscape** → leave default
   settings → **Create** → switch back to **Select** mode.
6. **Scale reference**: Content Drawer → Characters folder → Manikins →
   Mesh folder → drag a mannequin mesh into the scene, to judge scale
   while building.
7. Move on to building a custom road (modeled directly, not an imported
   asset) — see Chapter 3.

## Chapter 3: Road creation and texturing

1. Selection Mode → **Modeling** → create a **Rectangle** primitive.
2. Increase its subdivisions for a denser, more deformable mesh:
   **Width Subdivisions = 200**, **Depth Subdivisions = 200** → **Accept**.
3. Back in Select mode, select the rectangle, right-click → **Browse to
   Asset** (locates/selects it in the Content Drawer).
4. **Enable Nanite** on it: right-click the asset → **Nanite** → **Enable
   Nanite**.
5. Press **R** (scale gizmo) to scale the rectangle up to road size,
   reposition (raise slightly off the landscape).
6. **Apply a blend master material** — the tutorial uses a free material
   called **"Unreal Senzi"**:
   - Download from **andrealengi.com → Resources** section → find the
     Unreal Senzi master material → enter name/email → a download link
     is emailed.
   - Open the downloaded content, copy all its folders.
   - In your Unreal project: Content Drawer → right-click the Content
     folder → **Show in Explorer** → paste the copied folders in.
   - Back in the project's **Materials** folder, you'll find 4 blend
     materials shipped with it. Right-click one → **Create Material
     Instance** (the tutorial calls this instance a "metal instance" —
     it's the Nanite-compatible instance of the blend master material).
   - Drag that material instance onto the road rectangle.
7. **Source road textures** from the **Fab marketplace** — the tutorial
   searches for and adds a material called **"Droid American Road"**
   (quality: High) → **Add to Project**.
8. Don't apply that downloaded road material directly — instead, open
   its own **Textures** folder and feed its individual texture maps into
   the Unreal Senzi blend material's **Material A** slot set:
   - Open the Unreal Senzi material, in the Details panel for **Material
     A**, enable the **Albido color**, **Roughness**, **Height**, and
     **Normal** texture-slot toggles.
   - Drag in: the Albido map → Albido slot, the Height map → Height
     slot, the Normal map → Normal slot, and the **OM map** (combined
     Occlusion/Roughness/Metallic) → the Roughness slot.
9. Save and close the material — Material A (the base road surface) is
   done.
10. **Save the level**: File → Save All → name it (e.g. "tutorial") →
    Save.
11. **Troubleshooting — displacement too strong**: the parallax/
    tessellation displacement effect looked too extreme on the finished
    road.
    - Fix: reopen the material asset, find the **Displacement Amount**
      parameter under the Material A settings, enable it, and lower the
      value (tutorial tries **0.5**).
    - This introduced a visible rendering artifact — fixed by nudging
      the Directional Light's position slightly (**Ctrl+L**, then move
      the mouse) — same control from the other tutorial's Chapter 3/9.
    - Displacement was then tuned back up a bit (to roughly **2–3**) for
      a better-looking result, and saved.

## Chapter 4: Material refinement and painting (partial — cuts off mid-sentence)

Goal: blend in "imperfection" layers (moss, concrete debris) on top of
the base road material, using the blend material's additional layer
slots plus vertex-color mesh painting to control where each shows.

1. Download two more Fab materials and **Add to Project**:
   - **"Mossy Concrete Wall"**
   - **"Military Trench Ground [Dirt]"** (transcript says "dart," almost
     certainly a mis-transcription of "dirt")
2. **Material B** (mix in the Mossy Concrete Wall textures):
   - Open the Mossy Concrete Wall asset's own folder → its High-quality
     subfolder → Material/Textures folder to find its maps.
   - Open the Unreal Senzi blend material, scroll up to find **"Second
     Metal Layer"**, enable it — this reveals the **Material B** slot
     set.
   - Enable all of Material B's texture-slot toggles (Albido, Height,
     Normal, Roughness).
   - Drag in: Albido map → Albido slot, Height map → Height slot, Normal
     map → Normal slot, OM map → Roughness slot (same pattern as
     Material A).
3. **Material C** (mix in the Military Trench Ground textures) — repeat
   the identical process:
   - Scroll up in the material, enable **"Third Material Layer"**.
   - From the Military Trench asset's High/textures folder, enable all
     Material C texture slots and drag in each map the same way.
4. Save and close the material.
5. **Paint the extra layers onto the road** using Unreal's built-in
   **Mesh Paint** mode (this is how you control *where* Material B/C
   show, versus the base Material A):
   - Select the road mesh, switch to **Mesh Paint** mode.
   - Under its options, go to **Texture Color** (vertex-color paint
     target), select the road asset, click the **+ / switch** button to
     add a paintable layer.
   - Open the **Paint** tool options.
   - **Deselect the Blue and Green color channels**, leaving only the
     **Red channel** active — the blend material reads the vertex
     color's channels to decide how much of each extra layer (B/C)
     shows at a given point, so painting in a specific channel targets a
     specific blend layer.
   - Set **Strength** to maximum (**1**).
   - Paint directly on the road mesh in the viewport to reveal the moss
     layer in chosen spots.
6. Troubleshooting note (transcript cuts off here): after painting, the
   newly-blended layer's displacement again looked too strong — same fix
   pattern as Chapter 3 step 11 (reopen the material, lower that layer's
   Displacement Amount parameter) was about to be repeated when the
   transcript ends mid-sentence.

---

*To extend: send more transcript/screenshots from later parts of this
video (finishing the paint layering, any further set dressing, lighting,
or export) and this file will be updated.*
