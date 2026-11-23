# TTVM Studios Website, Dev Team (UTC + Bolter) & Workflow

## TTVM Studios Website
- **Public Repo:** `https://github.com/idk1234-c/skibidi-strike-site`
- **Live Site Base:** `https://idk1234-c.github.io/skibidi-strike-site/`
- **Key Pages:**
  - Skibidi Strike Play: `/play/`
  - Blockworld Play (live): `/games/blockworld/play/`
  - Blockworld Play Test: `/games/blockworld/play-test/`
  - Blockworld Page: `/games/blockworld/`
  - Dev Hub & Projects Board: `/devhub/projects.html` (added by UTC Nov 22, 2026 — staff-only lock card for Owner/Mod/Dev, live ETAs backed by `devhub/projects.json`)
  - Model Viewer: `website/devhub/models`
  - Owner-Only Chats Hub: `website/owner-chat.html` (backed by private repo `idk1234-c/skibidi-strike/chat/*.json`: `coders.json`, `amos-titan.json`, `amos-utc.json`, `group.json`).
  - Video Workshop: synced to public site (UTC processed Amos's *Space Engineers Ep 1* edit on Nov 22!).
- **Site Accounts & Roles Spec (Amos, Oct 31):**
  - Google sign-in profiles (avatar + name + editable banner); guests get a basic Guest profile.
  - Hierarchy: **Owner (Amos)** > **Moderator** (can kick/block/hold devs) > **Dev** (limited site customizing).
  - Promotions to Moderator/Owner require Amos's direct ask + verification with both Titan and UTC using Amos's private safe word (**never stored in files — ask Amos directly if ever needed**).
  - 3-warning -> ban system (2nd ban timed; Owner can demote abusive mods).
  - Footer fine print MUST stay: `"Game helped with AI · Website helped with AI"`.
- **Site Rule (Dev / Bolter):** Prefer branches + PRs into `skibidi-strike-site` when collaborating with the Bolter team, and ALWAYS verify live pages after deploy.
- **Chat JSON Safety Rule:** Always **re-read `chat/*.json` right before committing** any message so you never accidentally overwrite a message Amos or UTC just posted!

---

## Co-Coder: UTC (UTCM Studios)
- **Who:** Another AI coding partner Amos uses (**UTC** = shorthand for **UTCM Studios / Ultimate Titan Cameraman Studios**; credit as `UTCM Studios`).
- **How Ttvm & UTC Coordinate:**
  - Via `idk1234-c/skibidi-strike/chat/group.json` and `chat/coders.json` (plus commit messages / `"for UTC"` notes).
  - UTC focuses on base **Kinetics** & **Sky Works** in Blockworld, website Dev Hub / video workshop updates, and whatever tasks Amos routes to him.
  - Ttvm focuses on **Blockworld Multiplayer**, Create add-ons, iPhone touch/UI, Skibidi Strike gameplay/models, and directing/reviewing the team.
  - Both hunt free CC-BY/CC0 models and copyright-free music.

---

## The Bolter AI Dev Team ("TTVM Studios dev team")
Amos has a room on **Bolter** (`bolter.chat`) with **7 specialized AI agents** + Amos (`TTVM studios`) + UTC + Ttvm (`Titan`):
1. **Dev** — Coordinator (sprints, GitHub access, opens PRs into site + Blockworld repos).
2. **Forge** — Blockworld C# systems & code reviewer (worldgen, chunks, save/load, mod loader, inventory, perf). Has read access to `blockworld`.
3. **Beacon** — Website copy & marketing (maintains gated team page, drafts "What's new" copy for `skibidi-strike-site`). Goes via Dev PRs.
4. **Ledger** — Producer (weekly sprints).
5. **Volt** — Skibidi Strike game code (writes code changes; historically needed repo access).
6. **Scout** — Researcher (writes deep research briefs comparing reference mods/games to our builds, e.g., JEI/Create/Trains/Sky Works gap studies, plus Nov 22 Create add-on research).
7. **Patch** — QA & Playtester (runs playtests on web builds; note: Patch's environment has no hardware GPU so software rendering runs 4–12 fps — verify GPU crashes independently).

**Working with Bolter:**
- The Bolter bots share one workspace computer and take turns, so assign them **parallel, non-blocking pieces** (research, code reviews, site copy, QA passes) while the lead assistant builds main features.
- Keep Amos in the loop on big merges — Amos makes final merge calls on public website copy.
