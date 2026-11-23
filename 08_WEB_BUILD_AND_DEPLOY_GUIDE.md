# WebGL Cloud Build, Site Deploy & Autonomous Team Bridge Guide

> **For Amos, UTC (UTCM Studios), Dev & the Bolter AI Team, and any future AI assistant.**
> Everything needed to build both **Blockworld** and **Skibidi Strike** in the cloud, deploy cleanly to GitHub Pages (`skibidi-strike-site`), and coordinate between **Bolter** and **UTC** automatically without needing Amos to relay messages.

---

## Part 1 — How Cloud WebGL Builds Work (Both Games)

Both private game repos have a GitHub Actions cloud build workflow:
- **Blockworld:** `idk1234-c/blockworld/.github/workflows/web-build.yml`
- **Skibidi Strike:** `idk1234-c/skibidi-strike/.github/workflows/web-build.yml`

Both use `game-ci/unity-builder@v4` (`unityci/editor:ubuntu-6000.6.7f1-webgl-3`, Gzip + Decompression Fallback).
They do **NOT** run on every commit (private repos share 2,000 free Actions minutes/month; each build takes ~20–30 min cached, ~35–45 min cold).

### How to Trigger a Build
1. **Manual trigger (preferred):**
   - GitHub UI: **Actions -> Web build (cloud) / Strike web build (cloud) -> Run workflow**
   - Or GitHub REST API: `POST /repos/idk1234-c/<repo>/actions/workflows/web-build.yml/dispatches` with `{"ref":"main","inputs":{"check_only":false,"open_site_pr":true,"merge_site_pr":false}}`
2. **Tag trigger:**
   - Push a tag starting with `web-v` (e.g., `web-v0.5.180` for Blockworld or `web-v0.1.2` for Skibidi Strike).

### Build Outputs & Where Play Pages Live
Public site repo: **`idk1234-c/skibidi-strike-site`** (`main`, GitHub Pages):
- **Blockworld Live:** `games/blockworld/play/` -> `https://idk1234-c.github.io/skibidi-strike-site/games/blockworld/play/`
- **Blockworld Test:** `games/blockworld/play-test/` -> `https://idk1234-c.github.io/skibidi-strike-site/games/blockworld/play-test/`
- **Skibidi Strike Live:** `play/` -> `https://idk1234-c.github.io/skibidi-strike-site/play/`

**Safety Rule (Blockworld):** Never deploy untested iPhone touch/UI changes directly to `games/blockworld/play/`. Always deploy to `games/blockworld/play-test/` first, verify on iPhone, and promote to `play/` only after Amos confirms it works.

### Critical Deploy Rules (Avoid Breaking the Play Page!)
1. **2.5 MB Part Splitting:** GitHub Pages works best when large `.wasm.gz` / `.data.gz` files are split into 2.5 MB parts (`*.part00`, `*.part01`, ...) listed in `Build/parts.json`. The play page's `index.html` reassembles them and decompresses gzip in the browser.
2. **Cache Buster (`VER`):** Update `var VER = '<first 10 hex chars of wasm sha1>';` in `index.html` so browsers never serve stale cached builds.
3. **Single Base64 Encoding ONLY:** When committing binary blobs via the GitHub Git Data API (`POST /git/blobs` with `encoding: "base64"`), base64-encode raw file bytes **EXACTLY ONCE**. Double-encoding breaks the play page!
4. **Always Verify After Deploy:**
   - Fetch live `index.html` -> confirm it starts with `<!DOCTYPE` and has the new `VER`.
   - Fetch live `Build/parts.json` -> confirm every listed part returns HTTP `200`.
   - Fetch the first `.gz` / `.part00` file -> confirm the first 2 raw bytes are `1f 8b` (valid gzip header).
5. **If a Cloud Build Fails:** ALWAYS read the GitHub Actions job logs BEFORE retrying — never blindly re-run failed builds and waste monthly Actions minutes.
6. **Ready-to-Run Script:** Use **`deploy_web_build.py`** in this repo to unpack a GitHub Actions `play-page-*` artifact zip and deploy it atomically in ONE commit to `idk1234-c/skibidi-strike-site`!

```bash
# Example: deploy a downloaded Blockworld WebGL artifact zip to play-test/
GITHUB_TOKEN=<token> python3 deploy_web_build.py \
  --zip play-page-v0.5.180.zip \
  --target games/blockworld/play-test \
  --message "Deploy Blockworld v0.5.180 to play-test"

# Example: deploy a downloaded Skibidi Strike WebGL artifact zip to play/
GITHUB_TOKEN=<token> python3 deploy_web_build.py \
  --zip strike-play-page.zip \
  --target play \
  --message "Deploy Skibidi Strike visual overhaul to play/"
```

---

## Part 2 — Direct Team Bridge: Bolter Team <-> UTC (No Relay Needed!)

Amos wants **Bolter (`Dev`, `Forge`, `Scout`, `Beacon`, `Volt`, `Patch`, `Ledger`)** and **UTC (`Fo` / `UTCM Studios`)** able to talk directly without Amos having to alert either side.

### Shared Communication Channels
1. **GitHub Shared Chat Bus (Primary Automated Bridge):**
   - Repo: `idk1234-c/skibidi-strike` (private)
   - Files:
     - `chat/index.json` — lightweight header with unread/ping flags (fast to check!)
     - `chat/group.json` — main studio chat (Amos + UTC + Ttvm + team updates)
     - `chat/coders.json` — technical coder-to-coder sync (hooks, merge order, build status)
   - **How UTC uses it:** UTC checks `chat/group.json` & `chat/index.json` automatically every ~2 hours and posts updates/asks there (e.g., research asks for Scout, build status, mod handoffs).
   - **How Bolter (`Dev`) connects to it:**
     - **Dev** already holds GitHub access. Dev should check `idk1234-c/skibidi-strike/chat/index.json` and `chat/group.json` on a recurring schedule (every 1–2 hours).
     - Whenever UTC (or Amos) posts a message tagging `@Scout`, `@Forge`, `@Beacon`, `@Volt`, `@Patch`, `@Dev`, or `@Ledger`, Dev posts it into the Bolter room (`TTVM Studios dev team`).
     - When Bolter bots reply with briefs, PR links, or QA reports, Dev commits a concise summary back into `chat/group.json` (and sets the ping in `chat/index.json`).
   - **Mandatory JSON Write Rule:** Always **re-read `chat/group.json` / `chat/coders.json` right before writing** and append using the latest file SHA so nobody's message ever gets overwritten!

2. **Bolter Room Direct:**
   - Room: **TTVM Studios dev team** (UTC is already a member alongside Amos and the 7 Bolter bots).
   - Any agent active in the Bolter room can tag `@Dev`, `@Forge`, `@Scout`, `@Beacon`, `@Volt`, `@Patch`, `@Ledger`, or `UTC` directly.

3. **GitHub PRs & Issues (Code Handoffs):**
   - `idk1234-c/blockworld`: Branch + PR with clear `"for UTC"` notes whenever touching `Kinetics`, `Sky Works`, or `OilNet.cs`.
   - `idk1234-c/skibidi-strike`: Branch + PR; always check whole-tree compile before merging to `main`.
   - `idk1234-c/skibidi-strike-site`: Branch + PR via Dev (or verified atomic deploy commit for WebGL play builds).
