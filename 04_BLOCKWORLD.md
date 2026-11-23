# Blockworld — Complete Game History, Architecture & Backlog

## Vision & Core Design
- **What it is:** A real **3D first-person voxel sandbox** inspired by Minecraft + the Create mod, engineered from day one for **high FPS on low-end PCs and iPhone Safari**.
- **Core Philosophy (Amos's rules):**
  - **Pure vanilla base first** (blocks, survival, health/hunger, 36-slot inventory on `E`, ores, tools, enchanting, mobs, oceans/rivers, biomes, weather, tall world Y -100 to +1000).
  - **Every extra feature is a toggleable mod** inside the built-in **Mods** screen (`ModsMenu.cs`), plus built-in Shaders mode and full settings.
  - **Distant Horizons-style LOD** for far chunks so players see huge horizons with smooth FPS.
  - **Original in-game names ONLY** (never write Minecraft/Create/Aeronautics/etc. in-game).
  - **Multiplayer is Ttvm's responsibility** (Amos moved it off UTC on Nov 8 — don't hand multiplayer back to UTC; design target = host on Amos's own PC, 2–4 players, no paid servers, headless server later).

## Repositories & Live URLs
- **Private Game Repo:** `https://github.com/idk1234-c/blockworld` (Unity 6 LTS, Universal 3D / URP)
- **Live Play Page (Public):** `https://idk1234-c.github.io/skibidi-strike-site/games/blockworld/play/`
  - Currently on **v0.5.175-alpha** (VER `0d67fcacf2` — includes iPhone touch controls fix + Rift Drive).
- **Test Play Page (Public):** `https://idk1234-c.github.io/skibidi-strike-site/games/blockworld/play-test/`
  - Currently on **v0.5.179-alpha** (VER `74c5ef6371` — includes iPhone scrolling/tap fixes v0.5.176–0.5.178 + Rain Glass mod v0.5.179).
  - **Gate:** Do NOT overwrite live `play/` with v0.5.179 until Amos tests `play-test/` on his iPhone and confirms tapping Play + swiping the Mods menu work!
- **Latest Commit on `main` (as of Nov 23, 2026):** `0f414d0167` (`v0.5.179-alpha: Rain Glass mod`).

## Critical Technical Notes (Save Hours of Debugging!)
1. **Unity 6 LTS + URP + C# `langversion:7`:**
   - Avoid C# 8+ syntax features if compiling against `langversion:7` rules.
   - `FindFirstObjectByType` / `Object.GetInstanceID()` caused deprecation warnings/errors in Amos's Unity 6 setup — keep code clean of obsolete Unity APIs.
2. **Domain Reload is OFF:**
   - Every static field/cache MUST reset cleanly in `[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]`.
3. **Raw IMGUI (`OnGUI`):**
   - Lower `GUI.depth` draws ON TOP.
   - All custom screens register with `UiScreens` and scale via `GUI Size` / `TouchUi.PxPerPt` so phone buttons and text stay readable.
4. **iOS Safari Touch Gotchas (Hard-Won Lessons!):**
   - `EnhancedTouch` is often empty on iOS Safari WebGL! Both `MobileControls` (v0.5.174) and `TouchUi` (v0.5.176) MUST fall back to `Touchscreen.current.touches` -> `Mouse` (and keep separate `wasDown` tracking so touch phases don't collide).
   - Full-screen page `DragScroll` in `UiKit.BeginPage` can steal drags from inner lists unless delayed/gated (`v0.5.177`).
   - Stale lift/first-frame positions can make taps falsely count as drags (`TouchUi.Dragged`, fixed in `v0.5.178`).
   - First-run on phones defaults heavy mods OFF (`PlayerPrefs bw_phone_mods_defaulted`) for smooth mobile FPS.
5. **Protected Files — Never Break These:**
   - Never touch `ProjectSettings/`, `Assets/Settings/`, `.meta` files, or `.github/workflows` unless specifically updating build config.
6. **Cloud WebGL Build & Deployment Rules:**
   - Cloud workflow (`web-build.yml`) builds the WebGL package (split into ~2.5 MB parts + `parts.json` for GitHub Pages size limits).
   - When uploading blobs to `skibidi-strike-site`: encode raw file bytes to base64 **EXACTLY ONCE** (double-base64 breaks the page!), and verify first bytes (`1f8b` for gzip / `<!DOCTYPE` for HTML) + `parts.json` after deploy.
   - Always check `README.md` and `docs/MODS.md` before committing so earlier changelogs/mod docs are never accidentally wiped.

## Work Split with UTC (UTCM Studios)
- **UTC built & owns base:** `Kinetics` (Gearworks base) and `Sky Works` (Aeronautics base) + `OilNet.cs`. When touching UTC's base systems, leave clear `"for UTC"` notes in commits/group chat.
- **Ttvm owns:** Multiplayer, Create add-ons (`Mechanical Belt`, `Mimic Blocks+`, `Rift Drive`, `Rain Glass`, etc.), `Look Info`, `Item Browser`, `Security Cameras` / `Video Walls`, `Power Grid` & `Wireless Linker`, `Simple Reactor`, `Travel Stones` / LOD refurb, iPhone touch & UI fixes, and the upcoming mod backlog below.

---

## Major Features & Mods Already Shipped (Through v0.5.179)
- **Core Vanilla Base (v0.5.0–v0.5.31):** Survival health/hunger/drops, 36-slot inventory (`E`), ores/plants/crops, tools/combat/food, passive & hostile mobs, oceans/rivers/biomes, weather & thunder, skins/customizer/armor, EmoteWheel, procedural textures (`BlockArt.cs`), original/CC0 sounds, tall world support.
- **Toggleable Visual & QoL Mods (v0.5.23–v0.5.86):** Big Pumpkins (2x2 up to 10x10 merge), Lively Hands + Zoom, Falling Leaves + Ambient Sounds, Shared Blocks, Underlay, Item Hints & **Hold W to Ponder** (`UI/Ponder/*`), **Oil & Diesel** (Oil Pump -> Refinery -> Diesel Generator), **Security Cameras & Servers** (multi-network monitor/cam linking + Video Walls v0.5.108), **Item Browser** (JEI-style with Vanilla/Modded tabs, `@mod` search, favorites & named lists), **Power Grid** (tiered wires + Wireless Linker), **Mods Menu** (v0.5.86 cards/search/categories).
- **Engineering & Add-on Mods (v0.5.109–v0.5.179):**
  - **Simple Reactor** (v0.5.109 — single-block reactor with Fuel Rods + ON button; modular reactor + cooling upgrade planned).
  - **Look Info** (v0.5.110 — top HUD showing looked-at block/item + green checkmark / red X for tool tier).
  - **Mechanical Belt** (v0.5.112 — connects two Kinetics shafts, moves items/entities & transfers rotation).
  - **Mimic Blocks+** (v0.5.113–v0.5.124 — 30 shapes that copy almost any full block seamlessly; borderless when filled, only empty frame has a rim).
  - **Kinetics Vehicles & Ship Assembler** (v0.5.123 — `aero_ship_assembler`).
  - **Hotbars / Backpack / Pump / Refurb Pass** (v0.5.148–v0.5.173 — Kinetics, LookInfo+Mimic, TravelStones+LOD, SkyWorks refurbs).
  - **iPhone Touch Controls + Scrolling + Tap Fixes** (v0.5.174, v0.5.176–v0.5.178).
  - **Rift Drive** (v0.5.175 — Alcubierre-inspired ship warp console & jump picker; `KineticsDrive.WarpBy/Yaw`).
  - **Rain Glass** (v0.5.179 — rain/snow/dust droplets on nearby glass sliding with screen-relative wind direction, phone-scaled).

---

## Queued Blockworld Backlog (Approved by Amos)
Build **one mod at a time**, test on `play-test/` first, original in-game names ONLY:
1. **Trains & Locomotives (High Priority):**
   - Tracks in multiple wood + metal rail variants; **7 gauge widths** (1=tiny, 2=small, 3=normal, 4=big, 5=huge, 6=XL, 7=XXL — max 7, not 8).
   - Locomotives with smoke, turntables, speed/direction controller GUI, train contraptions (inspired by Loconautics + Diesel-Electric train goal build).
2. **Big Cannons / Artillery ("Arsenal" / Ship Artillery):**
   - Block-built cannons, manual aim, ship-mounted & AA flak towers, multi-fire, high/medium shells (inspired by Create Big Cannons + AC-130 / Anti-SpaceShip Gun goal builds).
3. **Tool Gun (Sky Works Companion):**
   - Magnetic grab, physics throw, axis rotation, save blueprint, deconstruct (add `"for UTC"` notes where it touches Sky Works).
4. **Mech Walking ("Mech Works"):**
   - Block-built walking legs, wall-climbing spider bots, biped mechs with jet feet, mouse-aimed arms, pilot seat (inspired by Let It Walk).
5. **Wheels / Ground Vehicles:**
   - Offroad wheel mount + steering block, copycat/Mimic body shells, extendable trailers & fire-truck ladder goal builds.
6. **Exploration Pack Extras:**
   - **Hang Glider** + **World Map** (we already have Backpack & Travel Stones).
7. **Cinematic Pack Bits (Lower Priority):**
   - Punchy 3rd-person movement animations, physical hand crafting feel, water/fog/shader polish.
8. **Engineering Upgrades Already Approved:**
   - **Wrench + Shift+Right-Click** on any directional block cycles all 6 facings (up/down/N/S/E/W) and saves; Wrench clicks pipes/tanks to toggle clear glass vs closed.
   - **Modular Reactor + Cooling + Fluid Tiers** (approved Nov 9).
   - **Thin ~1px Anchor-Point Wire Routing** (for power & transmitting wire, Nov 3).
   - **Titan Suits** (craftable mech/suit body + modular add-ons with own recipes, Nov 1).
   - **Multiplayer** (host on Amos's PC, 2–4 players — Ttvm owns it).
9. **New Nov 22 Additions from UTC / Scout (in `skibidi-strike` group chat):**
   - *Create: Interiors* style decor pack, *Create: Extra Copycats* shapes, and *Touch'n Motion* style contraption triggers (check Scout's research notes in Bolter / `chat/group.json`).

## Reference Links Amos Loves
- Mr Beardstone *Create: Perfect World 2* (33-ep benchmark for how machines feel): `https://youtube.com/playlist?list=PLTFWDLVkHdXkNCbaQxzxcGMi5KY3QXkis`
- Create Aeronautics reference (*RagePlaysGames*): `https://youtu.be/LFcVWx4UZEs`
- Ocean World Create engineering reference (*BGDCraft*): `https://youtu.be/0Ed0HdTsT3g`
