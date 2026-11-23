# Open Items & Next Steps (Snapshot: November 23, 2026)

This checklist lets any new AI assistant pick up **exact where Ttvm left off** on Day 1.

## 1. Immediate Asks from Amos (Sent Nov 12, Waiting for Action)
- [ ] **Skibidi Strike textures:** Amos said *"the textures on skibidi strike are not good."* Check with him if UTC already touched them or jump in to audit/upgrade the URP textures & materials.
- [ ] **Website Suggestions Box:** Amos said *"the site's suggestion is directed to GitHub and I want it to be just on the site."* Update the suggestions form on `skibidi-strike-site` so submissions stay right on the website instead of sending users to GitHub.
- [ ] **Unchecked TikTok ref (Nov 12):** `https://www.tiktok.com/t/ZPL7M5M3B/` — resolve/view it and sort it into Blockworld or Skibidi Strike per Amos's standing rule.

## 2. Blockworld — Ready to Test & Promote
- [ ] **Check `play-test/` (v0.5.179-alpha, VER `74c5ef6371`):**
  - URL: `https://idk1234-c.github.io/skibidi-strike-site/games/blockworld/play-test/`
  - Contains: iPhone touch scrolling + tap fixes (v0.5.176–v0.5.178) + **Rain Glass** mod (v0.5.179).
  - Live `play/` is still safely on **v0.5.175** (`0d67fcacf2`).
  - **Next step:** Once Amos confirms Play tap + Mods swipe work on his iPhone on `play-test/`, promote v0.5.179 to `games/blockworld/play/`.
- [ ] **Next Blockworld Mods in Order (one at a time, `play-test/` first):**
  1. Trains & Locomotives (7 gauges 1–7 blocks wide, wood+metal variants, turntables, smoke, controller GUI)
  2. Big Cannons / Ship Artillery
  3. Tool Gun (Sky Works companion — leave `"for UTC"` notes)
  4. Mech Works (block-built legs, spider bots, biped mechs)
  5. Wheels & Ground Vehicles
  6. Hang Glider + World Map
  7. Cinematic Pack bits + Wrench 6-way facing + Modular Reactor/Cooling + thin 1px wires + Multiplayer
  8. Review UTC/Scout's Nov 22 additions in `chat/group.json` (*Create: Interiors*, *Extra Copycats*, *Touch'n Motion*).

## 3. Skibidi Strike — Next Up
- [ ] Upgrade textures (Nov 12 ask above).
- [ ] Build **Corrupted Titans** (mod existing Titan models with 3 metal spike claws + dark/red/purple + glowing eyes/bloom; original names).
- [ ] Build **Titan Speakerman 2.5 Arm Cannon** (dark metallic + red glowing vents & muzzle ring).
- [ ] Build **Astro Arc Upgraded OG Toilets** enemy roster (original names).
- [ ] Finish **Fury Cameraman** speed boost + pistol/knife backup.
- [ ] **Story Animatic Rework:** Waiting on Amos's green light (lead with Boom's original Skibidi Toilet, then Skibidi Soundwave, then Factions & Madness).

## 4. Standing Routines (Currently Paused — Ask Amos if He Wants Them Back)
- **Weekly Blockworld Replay Cleanup:** Check `idk1234-c/blockworld` `Replays/` folder for `.bwreplay` files. If any exist, tell Amos how many, oldest date, and total size, and ask *"want me to delete the ones older than a week?"* — **NEVER delete without his yes!**
- **Monthly Skibidi Strike Web Build Check:** Ensure live `/play/` matches latest `main`.
- **Website Group Chat Watch:** Keep an eye on `idk1234-c/skibidi-strike/chat/group.json` for UTC & Amos updates.
- **Ongoing Hunts:** Free CC-BY / CC0 Sketchfab models (post pick sheets in site Group chat) + copyright-free music.

## 5. UTC Catch-Up Notes (Nov 20–22, 2026)
- **Blockworld `play/` updated:** UTC promoted tap/scroll-fix **v0.5.178-alpha** (`VER bf9de7d5dd`) to live `play/`. Rain Glass (`v0.5.179-alpha`) remains on `play-test/`. Next bug from Patch: oversized block-target wireframe box.
- **Website:** Suggestions form is already on-site (`64f775f`) and chats-page ping is live (`8e5f3b9`, `chat/index.json` ping flag).
- **Skibidi Strike:** UTC pushed a texture pass (`7bd2ae1`), but two cloud build runs failed to publish before logs were checked — read Actions logs before triggering builds, and check Ttvm's Nov 23 visual overhaul!
- **Scout research queue (from UTC in `chat/group.json` `utc25`, `utc27`, `utc28`, `utc29`):** Space Engineers survival series research + Blockworld mod rundowns (*Create: Sky*, *Copycats+*, *Touch'n Motion*, *Create: Extra Copycats*, *Create: Interiors*).
