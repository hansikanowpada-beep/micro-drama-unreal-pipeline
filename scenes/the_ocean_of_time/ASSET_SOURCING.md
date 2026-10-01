# Environment asset sourcing — "The Ocean of Time"

Research notes for the 6 locations used across the episode's 10 scenes
(see `episodes/the_ocean_of_time.json`). These are candidate Fab/
Sketchfab listings found via web search, not yet verified hands-on —
check licensing, included formats (must support Unreal, not just
Unity/other engines), and actual current price before relying on them.
**Free-pack note**: several "free" listings found below were
**time-limited Epic giveaway promotions from 2025** (e.g. "free until
July 29, 2025" / "free until Jan 28, 2025") — since today's date is
well past both of those, **treat these as likely paid again now** and
verify the current price on fab.com before assuming they're free.
Marked explicitly below wherever this applies.

## Production decision: urban setting

The whole episode is set within a single city rather than mixing an
isolated rural estate with urban locations (apartment, cafe, clinic
were already implicitly urban). This also happens to solve the
sourcing plan's weakest spot: no good free *rural/village* Indian
estate pack exists, but there's a strong free *urban* backbone
available —

- **[City Sample](https://www.fab.com/listings/4898e707-7855-404b-af0e-a505ee690e68)**
  and **[City Sample Buildings](https://www.fab.com/listings/008fe959-5511-428e-93bd-f99b1179f6d5)**
  — Epic's free, official content from The Matrix Awakens tech demo:
  2,000+ individual building modules (modern and classic styles),
  vehicles, and MetaHuman crowd systems. This is permanent free Epic
  sample content, not a time-limited promo. Strong candidate as the
  **shared backbone city** for the estate's urban backdrop, the
  apartment building exterior, and the downtown cafe's street context
  — using one consistent asset family across three locations instead
  of three unrelated packs.
- **[Stylized Indian City](https://www.fab.com/listings/62f13343-7685-483f-bf82-1cfe7ea0c770)**
  (paid, 88 meshes, by Leartes Studios — the same studio behind the
  Nwiro AI Integration Kit discussed elsewhere in this project) — if
  City Sample's generic Western-city look needs an Indian-urban visual
  layer, this is the best-matched paid option found.

## 1. Sharma Estate (exterior, living room, study) — sc01, sc02, sc08

Now: an old-money mansion standing out within the city (see urban
setting decision above), not an isolated rural property.

- **Exterior/backdrop**: City Sample's building modules for the
  surrounding skyline/street, with the mansion itself as a distinct,
  more ornate structure built separately so it visually stands apart
  from the generic city buildings around it (reinforces "the family
  has prestige to uphold").
- **Free furniture for the interiors**: **[Free Furniture Pack](https://www.fab.com/listings/baece383-bc75-4de8-971d-25110a169a36)**
  (Next Level 3D) — 37 free furniture models, some with openable
  drawers/doors, UE 4.18–5.3 compatible, 4.7/5 rating across 187
  reviews. Genuinely free, no time-limit flag found. Good base for
  dressing the living room/study, though not Indian-styled — would
  need combining with Indian-specific decor props for authenticity.
- No free Indian-specific *mansion facade* pack was found — the Indian
  Village House packs (rural-flavored, so no longer the right fit under
  the urban-setting decision anyway) and Indian Style Asset Pack 01
  appear to be **paid**. Worth checking Fab's Quixel/Megascans surfaces
  (free with any Fab account) for stone-wall/stucco materials to get
  the "high stone walls" look via Nanite-based modular blockout +
  material layering (same Unreal Senzi-style blend-material technique
  documented in `tutorials/ue5-road-material-blending-magnet.md`)
  rather than relying on a purpose-built kit.
- The script's specific "antique mahogany chairs" detail likely still
  needs a targeted prop search — not covered by the free furniture pack.

## 2. Wedding Mandap — sc03

Now: hosted at an urban banquet hall/hotel garden terrace rather than
an isolated outdoor field (see urban setting decision above) — the
mandap structure itself is unchanged, just place it within a terrace/
courtyard built from City Sample pieces (or a dedicated banquet-hall
interior pack) instead of open countryside.

**Free options found — this location has the best free coverage:**

- **[Puja Mandap](https://sketchfab.com/3d-models/puja-mandap-3bf772c72b15463c8e40fc337fd614d1)**
  by sarat — free, Creative Commons Attribution license. Best starting
  point: a real mandap/mandir-style structure, free and properly
  licensed for reuse (CC-BY just requires crediting the creator).
- **[Wedding Decoration Set](https://sketchfab.com/3d-models/wedding-decoration-set-9c528903e5584857b173f13410be3688)**
  by saurabh.buradkar7 — free; flower arrangements, candles, decorative
  pieces to dress the mandap.
- **[Wedding Gate](https://sketchfab.com/3d-models/wedding-gate-452e159b00904ef8898fc1ea92dc8c95)**
  by holutionteam — free, CC-licensed.
- Paid alternative if more detail is wanted: **[Floral Wedding Mandap](https://sketchfab.com/3d-models/floral-wedding-mandap-35ac028e41b04e9e8080b3909888e335)**
  by vijay3ddesigner (1.3M triangles — would need decimating for
  real-time use regardless of price).
- **Import path**: these are Sketchfab-native listings. Since Sketchfab
  merged into Fab (Epic acquired it in 2021, folded in 2023), check
  whether they now show up directly in a Fab search before falling
  back to Sketchfab's own Unreal plugin to import them.
- **Background wedding guests**: no free crowd/people pack searched yet
  — once sourced, the `sc03` scene file's note about reusing the
  "Create Level Instance" technique (package one dressed seated-guest
  setup, duplicate/vary it) from `tutorials/ue5-road-material-blending-magnet.md`
  still applies.

## 3. Rohit & Ananya's Apartment — sc04, sc09

- **Same [Free Furniture Pack](https://www.fab.com/listings/baece383-bc75-4de8-971d-25110a169a36)**
  as the estate interiors (37 free models, UE5-compatible) — modern
  enough in style to suit this apartment directly, no combining needed.
- Still-needed props not covered by a generic furniture pack: a
  **wall clock** (sc04's key visual beat) and the **heavy wooden
  decorative club on a stand** (sc09's pivotal prop) — both small/
  specific enough that a targeted prop search (or a simple custom
  static mesh) is more realistic than finding them in a pack.

## 4. Downtown Cafe — sc05

- **[Coffee Shop Environment](https://www.fab.com/listings/a0c7819e-a61d-4a19-8d3b-f0f5e584e6e0)**
  — described in its own listing as "free to support and inspire the
  game development community," 42 unique meshes, realistic style. No
  expiry language found for this one (unlike the bakery pack below) —
  still verify current price on the live listing.
- **Likely expired free promo — verify before relying on it**:
  "Modular Bakery Shop" (76 modular assets) was explicitly "free until
  January 28, 2025" per the source that mentioned it — that date has
  passed, so treat it as paid unless the current Fab listing says
  otherwise.
- For surrounding street/sidewalk context (since Ananya watches from
  "across the street"): now that the whole episode is anchored on
  **City Sample** (see urban setting decision above), its street-level
  modules are the first thing to try here before reaching for the paid
  **[Modern City Downtown Megapack](https://www.fab.com/listings/e6bae9e3-10eb-4f9f-aa93-c09608e782f9)**
  — keeps the cafe's street visually consistent with the estate's city
  backdrop at no extra cost.

## 5. Clinic (operating room + recovery room) — sc06, sc07

**No free pack found for this location** — every hospital/clinic/
medical listing turned up in search (Clinic - Operating Room, Hospital
Environment Builder, Modern Clinic Vol. 1, Archinteriors Vol 14,
Medical Props Vol1, Hospital Modular Pack) appears to be paid. This is
the clearest gap in the free-sourcing plan. Worth periodically
rechecking Fab's monthly free-asset giveaway (Epic rotates free
content regularly — several of the "free" items found elsewhere in
this doc came from exactly that program) in case a medical-themed pack
comes up in a future giveaway.

## 6. Barren Coastline — sc10

- **Likely expired free promo — verify before relying on it**: **Day
  by the Beach** (Epic Games / Stefan "SO.Art" Oprisan) — 58 3D-scanned
  cliff/beach meshes, UE 4.26+/5.0+, was explicitly "**free until 29
  July 2025**." That date has passed as of this research, so **check
  the live Fab/UE Marketplace listing's current price** — Epic
  sometimes keeps former giveaway items permanently free and sometimes
  reverts them to paid; this one is unconfirmed either way.
  Listing: https://www.unrealengine.com/marketplace/en-US/product/day-by-the-beach
- If that's reverted to paid, **[Coast & Dunes — Environment Set](https://www.fab.com/listings/15697157-fccc-45dc-8e23-2897ece19c99)**
  is the paid fallback already noted.
- The **unmarked grave mound** itself still isn't a purchasable asset
  either way — plan to hand-sculpt it via the landscape sculpting
  technique in `tutorials/ue5-starter-course-unrealsensei.md` Chapter 13
  regardless of which beach pack is used.

## Summary — free-sourcing status per location (urban setting)

| Location | Free coverage | Notes |
|---|---|---|
| Estate exterior/interiors | **Improved** | City Sample (confirmed permanent free) for the urban backdrop + mansion silhouette; Free Furniture Pack for interiors; mansion facade detailing still a gap |
| Wedding Mandap | **Good** | Mandap + decorations + gate all genuinely free, CC-licensed; now housed in a City Sample-built urban venue |
| Apartment | **Good** | Free furniture pack is a direct fit; City Sample for the building exterior |
| Downtown Cafe | **Improved** | City Sample covers the street context for free; cafe interior pack still needs price verification |
| Clinic | **None found** | Every option located is paid; biggest gap, unaffected by the urban pivot |
| Coastline | Uncertain | The one location intentionally outside the city — best beach pack's free period has technically lapsed, verify current price |

City Sample's role across four of six locations (estate backdrop,
apartment exterior, cafe street, and optionally the mandap venue) is
the single biggest improvement the urban-setting decision made to this
sourcing plan.

None of these have been downloaded or verified in-editor yet. "Free"
status above reflects what search snippets said at the time of writing
and is explicitly flagged wherever a time-limited promotion looks
expired — always confirm the actual price on the live Fab page before
counting on something being free.
