#!/usr/bin/env python3
"""
Standalone atomic WebGL deploy script for TTVM Studios (Blockworld & Skibidi Strike).
Unpacks a Unity WebGL build zip (or GitHub Actions play-page artifact), splits files >2.5 MB
into parts + Build/parts.json if not already split, verifies gzip/HTML headers, and pushes
in ONE atomic commit to idk1234-c/skibidi-strike-site via the GitHub Git Data API.

Usage:
  GITHUB_TOKEN=ghp_xxx python3 deploy_web_build.py --zip build.zip --target play --message "Deploy Strike"
  GITHUB_TOKEN=ghp_xxx python3 deploy_web_build.py --zip build.zip --target games/blockworld/play-test --message "Deploy BW test"
"""

import argparse, base64, hashlib, json, os, sys, urllib.request, zipfile

OWNER = "idk1234-c"
SITE_REPO = "skibidi-strike-site"
CHUNK_BYTES = int(2.5 * 1024 * 1024)


def gh_req(method, path, token, payload=None):
    url = f"https://api.github.com{path}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))


def load_zip_files(zip_path):
    files = {}
    with zipfile.ZipFile(zip_path, "r") as zf:
        names = [n for n in zf.namelist() if not n.endswith("/") and "__MACOSX" not in n]
        # Strip common top-level wrapper folder if index.html is inside one
        prefix = ""
        for n in names:
            if n.endswith("/index.html") and n.count("/") == 1:
                prefix = n.split("/")[0] + "/"
                break
        for n in names:
            rel = n[len(prefix):] if prefix and n.startswith(prefix) else n
            if rel:
                files[rel] = zf.read(n)
    return files


def prepare_parts_and_ver(raw_files):
    out = {}
    parts_map = {}
    already_split = any(k.endswith("Build/parts.json") for k in raw_files)
    wasm_sha = None

    for rel, data in sorted(raw_files.items()):
        if ".wasm" in rel and ".part" not in rel and wasm_sha is None:
            wasm_sha = hashlib.sha1(data).hexdigest()[:10]
        if (not already_split) and rel.startswith("Build/") and len(data) > CHUNK_BYTES:
            part_names = []
            for idx in range(0, len(data), CHUNK_BYTES):
                p_name = f"{rel}.part{idx // CHUNK_BYTES:02d}"
                out[p_name] = data[idx : idx + CHUNK_BYTES]
                part_names.append(os.path.basename(p_name))
            parts_map[os.path.basename(rel)] = part_names
        else:
            out[rel] = data

    if (not already_split) and parts_map:
        out["Build/parts.json"] = json.dumps(parts_map, indent=2).encode("utf-8")

    # Sanity checks: HTML starts with <!DOCTYPE or <html, gzip starts with 1f 8b
    if "index.html" in out:
        head = out["index.html"][:64].lstrip().lower()
        assert head.startswith(b"<!doctype") or head.startswith(b"<html"), "index.html looks corrupted!"
    for k, v in out.items():
        if k.endswith(".gz") or k.endswith(".gz.part00"):
            assert v[:2] == b"\x1f\x8b", f"{k} does not start with valid gzip bytes (1f 8b)!"
    return out, wasm_sha


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", required=True, help="Path to WebGL build artifact zip")
    ap.add_argument("--target", required=True, help="Folder in skibidi-strike-site (e.g. play or games/blockworld/play-test)")
    ap.add_argument("--message", required=True, help="Git commit message")
    ap.add_argument("--branch", default="main")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("Error: set GITHUB_TOKEN env var first.")

    target = args.target.strip("/")
    raw_files = load_zip_files(args.zip)
    files, wasm_sha = prepare_parts_and_ver(raw_files)
    print(f"Prepared {len(files)} files for {SITE_REPO}/{target} (wasm_sha={wasm_sha})")

    ref = gh_req("GET", f"/repos/{OWNER}/{SITE_REPO}/git/ref/heads/{args.branch}", token)
    parent_sha = ref["object"]["sha"]
    parent_commit = gh_req("GET", f"/repos/{OWNER}/{SITE_REPO}/git/commits/{parent_sha}", token)
    base_tree = parent_commit["tree"]["sha"]

    # Remove stale files under target/ by marking old blobs null, then add fresh blobs
    full_tree = gh_req("GET", f"/repos/{OWNER}/{SITE_REPO}/git/trees/{base_tree}?recursive=1", token)
    new_paths = {f"{target}/{rel}" for rel in files}
    tree_entries = []
    for item in full_tree.get("tree", []):
        if item["type"] == "blob" and item["path"].startswith(target + "/") and item["path"] not in new_paths:
            tree_entries.append({"path": item["path"], "mode": "100644", "type": "blob", "sha": None})

    for rel, data in sorted(files.items()):
        b64 = base64.b64encode(data).decode("ascii")  # SINGLE base64 encode ONLY!
        blob = gh_req("POST", f"/repos/{OWNER}/{SITE_REPO}/git/blobs", token, {"content": b64, "encoding": "base64"})
        tree_entries.append({"path": f"{target}/{rel}", "mode": "100644", "type": "blob", "sha": blob["sha"]})
        print(f"  uploaded {target}/{rel} ({len(data)} bytes) -> {blob['sha'][:10]}")

    new_tree = gh_req("POST", f"/repos/{OWNER}/{SITE_REPO}/git/trees", token, {"base_tree": base_tree, "tree": tree_entries})
    new_commit = gh_req("POST", f"/repos/{OWNER}/{SITE_REPO}/git/commits", token, {
        "message": args.message,
        "tree": new_tree["sha"],
        "parents": [parent_sha],
    })
    gh_req("PATCH", f"/repos/{OWNER}/{SITE_REPO}/git/refs/heads/{args.branch}", token, {"sha": new_commit["sha"]})
    print(f"DEPLOYED! {SITE_REPO} {args.branch} -> {new_commit['sha']}")


if __name__ == "__main__":
    main()
