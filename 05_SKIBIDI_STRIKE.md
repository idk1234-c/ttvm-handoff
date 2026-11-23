# Skibidi Strike — Complete Game History, Story & Backlog

## Vision & Core Design
- **What it is:** A 3D wave-survival action shooter in **Unity 6 LTS (Universal 3D / URP)** inspired by **Skibidi Toilet** and Roblox's *Blockade Battlefront*.
- **Repositories & Live URL:**
  - **Private Game Repo:** `https://github.com/idk1234-c/skibidi-strike` (also hosts the site's `chat/*.json` files!)
  - **Live Play Page (Public):** `https://idk1234-c.github.io/skibidi-strike-site/play/` (currently VER `509aa5a48a`, includes Fury Cameraman + Shadow Agent Cameraman).
  - **Latest Game Code Commit:** `a7a2568a0c` (Nov 11, 2026).

## Gameplay & Design Rules (Amos's Direct Calls)
1. **Becoming a Titan (Oct 26 & Nov 3):**
   - NO 30-second Titan timer! When you spawn/buy/request a Titan, you **BECOME the Titan and stay Titan until you die**, then return to a smaller Alliance unit.
   - Helicopter supply/shop drops every 5 waves (`Titan Request` -> become Titan; Lobby `Titans` tab scaling size by level; Striders & camera rocket helis).
2. **Male-Only Titans Rule (Nov 3, 2026):**
   - **Titans are MALE ONLY** (Titan TV Woman was removed as inappropriate for kids).
   - **Female ground units** (TV Woman, Clock Woman, Drill Woman, Computer Woman, etc.) ARE allowed.
3. **Skibidi Lore Amos Follows (Oct 31):**
   - **Astro Toilets** = original "security toilet" race, pure evil.
   - **Skibidi Toilets** = betrayed the Astros and broke away with G-Toilet.
   - **The Alliance** = Cameramen, Speakermen, TV Men (and Titans).
4. **Audio, SFX & Music Rules:**
   - Keep the **credited Skibidi series SFX** (`Assets/Resources/Sfx`, 61 `.ogg` clips via `SfxBank.cs`) and menu music (*The Uncanny Valley* by Perturbator) as fan-made credited content — do NOT push Amos to delete them unless an actual takedown/claim arrives (if a real claim arrives, verify & swap immediately).
   - Always credit **DaFuq!?Boom!**, **Count!Dow** (Alliance Titan Prisma3D model), **TTVM Studios**, **UTCM Studios**, and all CC-BY Sketchfab creators.
5. **Original Names for Fan-Concept Additions:**
   - When adding fan-concept characters/enemies Amos finds on TikTok, give them **original in-game names** and credit the concept artist.

---

## What's Already Built & Shipped
- **Core Game Loop & Menu:** Main menu, lobby with portal, wave spawner (up to Wave 90 + achievements + scaling Astro Boss + flying laser toilets + warp effects + damage popups + camcorder HUD + Dev Mode).
- **Playable Characters:**
  - Regular Cameraman, Secret Unlockable **Astro UFO** (unlock rules: wave 50 + secret orb + points bank), **Alliance Titan** (3rd-person `V` toggle, punch `LMB`, chargeable laser arm `Q`, beam `RMB`), plus **Fury Cameraman** (`furycameraman` — minigun + axe + shield + auto-trigger Rage Mode when an ally takes damage) and **Shadow Agent Cameraman** (`shadowagent` — FBI vest, blue-flame jetpack, X-ray pulse, dual arm shields, dual orb guns).
  - *Note on Fury & Shadow Agent (Nov 11):* Compiled & deployed, not yet play-tested; Fury's speed boost & pistol/knife backup still pending.
- **Weapons:** Hotbar + Arm Cannon, Claws, Eye Laser, Heavy Blaster + **35 kept realism-passed weapon FBX models** (out of 44 modeled; Amos rejected #9, 10, 11, 12, 13, 19, 23, 28, 38 and recolored #17 EmberClaw purple).
- **Models & Rigging:** Rigged Cameraman + Astro UFO FBX in `Assets/Models/Rigged`; decimated Alliance Titan FBX + 25 textures in `Assets/Resources/Textures/`. Amos also approved 94 CC-BY Sketchfab picks across 44 characters (downloadable once signed into Sketchfab).

---

## Story & Visual Style References
- **Story Animatic Rework (Waiting on Amos's Go):**
  - Priority ranking Amos gave (Nov 9, 2026):
    1. **Original Skibidi Toilet (DaFuq!?Boom!)** — leads the story & tone.
    2. **Skibidi Soundwave** — Amos's favorite fan series, feels like Boom's successor (story + animation + own twist).
    3. **Skibidi Factions** — most creative + great quality.
    4. **Skibidi Madness** — great animation quality.
- **Visual / Animation Look References:**
  - `https://www.youtube.com/shorts/20rCBOkJODI` (*Destroyer Titan Saved Cameraman Titan*) — model/texture/animation look ref ONLY (not story).
  - `https://youtu.be/j675goCLiIE` (*cameraman base is under attack (P3D)* by ILHM Doodles) — animation & lighting style ref.
  - Papercraft **Titan TV Man 3.0** (`@kingsapo08`) — black + purple, big shoulder TVs, claw-wing spikes look ref.

---

## Queued Skibidi Strike Work (As of Nov 23, 2026)
1. **URGENT — Fix Skibidi Strike Textures (Nov 12, 2026):**
   - Amos texted: *"Hey the textures on skibidi strike are not good."*
   - First step: ask him which specific textures look worst (map/ground, characters, toilets, or weapons) or audit the existing URP materials/textures & upgrade them with crisp procedural/PBR detail and proper lighting/bloom.
2. **Corrupted Titans (New Bosses / Enemies, Nov 12):**
   - Build by modding our existing Titan models (faster & more accurate!): dark/red/purple corrupted monster variants, **three metal spike claws** instead of hands on most of them, **glowing red/blue eyes + bloom/glow-scan lighting** (Prisma3D tutorial style). Needs original in-game names.
3. **Titan Speakerman 2.5 Arm Cannon (Nov 12):**
   - Dark metallic cannon with red glowing vents + red muzzle ring (matches Corrupted Titans glow aesthetic).
4. **Astro Arc Upgraded OG Toilets — Enemy Roster (Nov 12):**
   - Glowing yellow/green astro-upgraded enemy toilets (original in-game names): Shieldbearer Laser Toilet, Quad Buzzsaw Spider Toilet (base defense), Searchlight/Police Toilet 3.0, Buzzsaw Mutant 4.0 (scout), Female Squad Toilet, Winged Guardian Toilet, Ultimate Toilet 2.0, Armored Overload Toilet 2.0 (explosives/tank), Savage Mutant 2.0, Hook Toilet 3.0, Collector Toilet, and Animal Toilet.
5. **Watcher Enemy Concept (Parked, Nov 3):**
   - Fan concept by `@mrfr1ez`: ceiling-hanging spy toilet with camera eyes, server cables, long spider legs, weak to bright light, nearly immobile (credit `@mrfr1ez`).
6. **Astro Duchess Concept (Parked, Nov 12):**
   - Red halo/orbs armored enemy/boss concept (`@astro.jbb`) — needs Amos's call on enemy vs. look ref + original name.
7. **Fury Cameraman Finish:** Add speed boost + pistol/knife backup once confirmed.
