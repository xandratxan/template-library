#!/usr/bin/env bash
# Build and serve multiversion Sphinx docs with sphinx-multiversion

# exit on error, unset var, or pipe failure
set -euo pipefail

# determine project root (one level up from this script)
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# output and source directories
export OUT="$REPO_ROOT/docs/_build/html"
SRC="$REPO_ROOT/docs/source"
export SITE_URL='https://xandratxan.github.io/template-library'

# ensure all tags are fetched
git fetch --all --tags

# clean and create output dir
rm -rf "$OUT"
mkdir -p "$OUT"

# build allowed refs (tweak whitelist for CI)
sphinx-multiversion "$SRC" "$OUT"

# generate PyData switcher JSON and copy to latest/_static
python - <<'PY'
import os, json, re, shutil, pathlib, sys

out = pathlib.Path(os.environ.get('OUT'))
site_url = os.environ.get('SITE_URL', '').rstrip('/')

def ver_key(name):
    nums = re.findall(r'\d+', name)
    return tuple(int(x) for x in nums)

pattern = re.compile(r'^v(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)$')
candidates = [p for p in out.iterdir() if p.is_dir() and pattern.match(p.name)]
versions = [{"name": p.name, "url": f"/{p.name}/"} for p in sorted(candidates, key=lambda p: ver_key(p.name), reverse=True)]
print("Release versions", versions)

chosen = sorted(candidates, key=lambda p: ver_key(p.name), reverse=True)[0]
chosen_name = chosen.name
print("Chosen latest version:", chosen_name)

shutil.copytree(chosen, out / "latest")
print("Copied", chosen, "to", out / "latest")

(out / "latest" / "_static").mkdir(parents=True, exist_ok=True)
(out / "latest" / "_static" / "switcher.json").write_text(json.dumps(versions, indent=2), encoding="utf-8")
out.joinpath("switcher.json").write_text(json.dumps(versions, indent=2), encoding="utf-8")
print("Wrote switcher.json with and latest/_static/switcher.json with", len(versions), "entries")

index_html = f"""<!DOCTYPE html>
<html>
  <head>
    <title>Redirecting to master branch</title>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url=./latest/index.html">
    <link rel="canonical" href="{site_url}/latest/index.html">
  </head>
</html>
"""
(out / "index.html").write_text(index_html, encoding="utf-8")
print("Wrote index.html redirecting to latest version")
PY

# serve for local inspection
python -m http.server 8000 --directory "$OUT"
