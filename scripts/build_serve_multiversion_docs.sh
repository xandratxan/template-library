#!/usr/bin/env bash
# Build and serve multiversion Sphinx docs with sphinx-multiversion

# exit on error, unset var, or pipe failure
set -euo pipefail

# determine project root (one level up from this script)
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# output and source directories
OUT="$REPO_ROOT/docs/_build/html"
SRC="$REPO_ROOT/docs/source"

# ensure all tags are fetched
git fetch --all --tags

# clean and create output dir
rm -rf "$OUT"
mkdir -p "$OUT"

# build allowed refs (tweak whitelist for CI)
sphinx-multiversion "$SRC" "$OUT"

# generate PyData switcher JSON and copy to latest/_static
python - <<'PY'
import json, re, os, pathlib
# directory with built docs
out = pathlib.Path('../docs/_build/html')
# whitelist pattern (matches "main" or semver like v1.2.3)
pattern = re.compile(r'^(?:main|v[0-9]+\.[0-9]+\.[0-9]+)$')
# collect versions
versions = []
if out.exists():
    # iterate visible directories and keep only those matching the pattern
    for p in sorted(out.iterdir()):
        if p.is_dir() and pattern.match(p.name):
            # add an entry for the switcher JSON
            versions.append({"name": p.name, "url": f"/{p.name}/"})
# write switcher.json at the site root
out.joinpath("switcher.json").write_text(json.dumps(versions, indent=2), encoding="utf-8")
# also write to latest/_static for compatibility
(out / "latest" / "_static").mkdir(parents=True, exist_ok=True)
(out / "latest" / "_static" / "switcher.json").write_text(json.dumps(versions, indent=2), encoding="utf-8")
# log result
print("wrote switcher.json with", len(versions), "entries")
PY

# serve for local inspection
python -m http.server 8000 --directory "$OUT"
