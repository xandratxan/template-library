# Multiversion Sphinx Documentation Deployment Options

Options for self\-hosted multiversion Sphinx docs (GitHub Pages + PyData Sphinx Theme)

1) mike (recommended for simplicity)

- What: A tool to build and deploy multiple Sphinx versions to GitHub Pages (creates versioned folders, aliases like
  `latest`, and handles redirects).
- Pros: simple CLI, explicit control over which versions to publish, easy to promote/archive versions, good GitHub
  Actions examples, integrates fine with the PyData theme.
- Cons: you build one version at a time (you typically loop in CI), but that is straightforward and fast for most
  projects.
- Notes for PyData theme: `mike` emits a sane directory structure and you can populate `html_context` or theme options
  with version metadata for a version switcher.

2) sphinx\-multiversion (automatic, builds many branches/tags)

- What: Scans repository branches/tags and builds docs for each matched ref into versioned folders.
- Pros: automatic (builds all matched branches/tags), good for automatically keeping many versions live.
- Cons: can be slower (builds many versions), configuration is via whitelist/blacklist patterns; you’ll need CI
  memory/time tuning.
- Notes for PyData theme: it produces folders you can wire into the theme’s version switcher (via `html_context` or a
  small JSON index).

3) sphinxcontrib\-versioning (parallel builds)

- What: Builds many versions in parallel (uses git worktrees/containers).
- Pros: fast for many versions.
- Cons: historically more complex to configure and maintain; larger toolchain and potential CI friction.
- Recommendation: consider only if you must build many versions often and can afford extra CI complexity.

4) DIY GitHub Actions (manual per\-version builds)

- What: Custom CI job(s) that check out a specific ref, run `sphinx-build`, and push to `gh-pages` into a versioned
  subfolder.
- Pros: full control, simplest dependency footprint, easy to integrate with custom needs (search indexing, Algolia
  snapshots, etc.).
- Cons: more manual wiring to maintain multiple jobs or loops for many versions.

Decision criteria (how to choose)

- Ease of setup: choose `mike`.
- Automatic coverage of branches/tags: choose `sphinx-multiversion`.
- Many versions and speed matters: consider `sphinxcontrib-versioning`.
- Full control / custom workflows: DIY GitHub Actions loop.

Integration notes for the PyData Sphinx Theme

- The theme can display a version switcher if you provide per\-version metadata (links, labels). Tools like `mike` and
  `sphinx\-multiversion` produce predictable folder layouts you can expose to the theme via `html_context` or a small
  `versions.json`.
- Set `html_baseurl` in `conf.py` and ensure canonical links are correct for SEO.
- Search is per-version (Sphinx builds a search index per output); for cross-version search use an external indexer (
  Algolia DocSearch) configured per-version or a custom indexer.

Quick example workflows

- Brief: GitHub Actions using `mike` to deploy a single chosen version (simple and robust).

```yaml
name: Deploy docs (mike)
on:
  push:
    branches: [ main ]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt  # include Sphinx, pydata-sphinx-theme
          pip install mike
      - name: Build docs and deploy with mike
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          cd docs
          # build and deploy version "v1.2.3" (could be derived from git tag)
          mike deploy --push --update-aliases v1.2.3 latest
```

- Brief: GitHub Actions using `sphinx-multiversion` to build all matched refs and publish to `gh-pages`.

```yaml
name: Deploy docs (sphinx-multiversion)
on:
  push:
    branches: [ main ]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt  # include Sphinx, pydata-sphinx-theme
          pip install sphinx-multiversion
      - name: Build multiple versions
        run: |
          sphinx-multiversion docs docs/_build/html
      - name: Publish to gh-pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/_build/html
```

Recommended next step

- If you want minimal operational complexity: adopt `mike` + a GitHub Actions job that builds the current tag/branch and
  updates `latest`.
- If you want full automation across branches/tags: try `sphinx-multiversion`, but test CI time and memory (and
  whitelist only the refs you care about).

# Multiversion Sphinx Documentation deployed To GitHub Pages with PyData sphinx theme, sphinx\-multiversion and GitHub ActionsDeployment

Short summary

- `sphinx\-multiversion` scans git refs (branches/tags) you allow, checks out each ref, runs a Sphinx build for each,
  and writes each build into a versioned subfolder (for example `v1.2.3/`, `main/`, `stable/`) under your output
  directory.
- The CI job then publishes the whole output tree to `gh-pages` (or another branch) so each version is served as a
  separate folder on GitHub Pages.

How it works (general flow)

1. GitHub Actions checks out the repository (use `fetch-depth: 0` so tags/branches are available).
2. Action sets up Python and installs Sphinx, the `pydata-sphinx-theme`, and `sphinx\-multiversion`.
3. `sphinx\-multiversion` is run with your docs source (`docs`) and a publishable output dir (commonly
   `docs/_build/html`). It:
    - enumerates refs matching your whitelist/blacklist patterns,
    - for each ref checks out content (internally uses a temporary git worktree/checkout),
    - runs `sphinx-build` for that ref producing a per-version HTML tree and search index,
    - optionally emits a small index (you can also generate `versions.json` in CI).
4. CI publishes the entire output directory to `gh-pages` (e.g., with `peaceiris/actions-gh-pages@v4`). GitHub Pages
   serves each version folder; you can expose a `latest` alias by publishing an extra symlink-like folder or by
   copying/promoting a build.

Key configuration points

- Which refs to build: use `sphinx\-multiversion` flags or patterns to whitelist tags/branches you want (avoid building
  everything to save time).
- `html_baseurl` in `conf.py` should match your Pages site root for correct canonical links.
- Version switcher: the PyData theme needs a list of versions (labels + URLs). Provide it via `html_context['versions']`
  or a `versions.json` file generated in CI that the theme reads.
- Search: each version gets its own Sphinx search index. For cross-version search use an external indexer (Algolia) or
  build a combined index in CI.
- Performance: build time grows with number of refs. Limit refs, parallelize builds in CI if needed, and cache Python
  deps.

Minimal GitHub Actions job (example)
A concise job that fetches all refs, installs deps, runs `sphinx\-multiversion`, and publishes:

```yaml
name: Deploy docs (sphinx-multiversion)
on:
  push:
    branches: [ main ]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt    # include Sphinx and pydata-sphinx-theme
          pip install sphinx-multiversion

      - name: Build multiple versions
        run: |
          sphinx-multiversion docs docs/_build/html --output-encoding=utf-8

      - name: Publish to gh-pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/_build/html
```

Operational tips

- Start by whitelisting only a few tags/branches to validate the pipeline.
- Generate a `versions.json` or populate `html_context` in CI so the PyData theme shows a version switcher with friendly
  labels.
- Monitor build time and memory; if building many versions often, consider more advanced parallelization or a different
  tool.

This text can be used as the section content under the requested heading.

## How to test sphinx-multiversion + PyData Sphinx Theme locally

Short checklist, then a tiny script you can run locally.

- Make sure you have full refs locally: `git fetch --all --tags` (or `git fetch --unshallow` if clone was shallow).
- Create a venv, install your `requirements.txt` plus `sphinx-multiversion` and `pydata-sphinx-theme`.
- Run `sphinx-multiversion` pointing `docs` -> `docs/_build/html`, use `--whitelist-rx` to limit refs while testing.
- (Optional) generate `versions.json` or write `html_context['versions']` so the PyData theme shows the switcher.
- Serve the output with a simple HTTP server: `python -m http.server 8000 --directory docs/_build/html` and open
  `http://localhost:8000/`.

Brief explanation of the script below: it creates a venv, installs deps, fetches tags, builds only `main` and `v*` refs
with `sphinx-multiversion`, writes a simple `versions.json` from the built folders, and serves the site on port `8000`.

```bash
# bash
# File: `scripts/build-multiversion-local.sh`
set -euo pipefail

# repo root assumed
VENV=.venv-docs
DOCS_SRC=docs
OUT_DIR=docs/_build/html
PYTHON=python3
PORT=8000

# prepare venv and deps
$PYTHON -m venv $VENV
. $VENV/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install sphinx-multiversion

# ensure refs available
git fetch --all --tags

# clean and build (whitelist only main and tags like v1.2.3)
rm -rf $OUT_DIR
mkdir -p $OUT_DIR
sphinx-multiversion $DOCS_SRC $OUT_DIR \
  --output-encoding=utf-8 \
  --whitelist-rx '^(main|v[0-9]+(\.[0-9]+)*$)'

# generate a simple versions.json the PyData theme can consume
python - <<'PY'
import json, os
out = "docs/_build/html"
versions = []
for name in sorted(os.listdir(out)):
    path = os.path.join(out, name)
    if not os.path.isdir(path):
        continue
    versions.append({"name": name, "url": f"/{name}/"})
open(os.path.join(out, "versions.json"), "w").write(json.dumps(versions, indent=2))
print("wrote versions.json with", len(versions), "entries")
PY

# serve
echo "Serving built docs at http://localhost:$PORT/"
python -m http.server $PORT --directory $OUT_DIR
```

Visit `http://localhost:8000/`. To iterate faster, change the `--whitelist-rx` pattern to build fewer refs or test a
single ref with `git checkout <ref>` + `sphinx-build -b html docs docs/_build/html/<ref>` instead of
`sphinx-multiversion`.

# References

- [sphinx-multiversion documentation](https://sphinx-contrib.github.io/multiversion/main/index.html)
- [PyData Sphinx Theme documentation](https://pydata-sphinx-theme.readthedocs.io/en/stable/)
- [PyData Sphinx Theme version switcher documentation](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/version-dropdown.html)

# PyData Sphinx Theme version switcher

The switcher requires the following configuration steps:

1. Add a JSON file containing a list of the documentation versions that the switcher should show on each page.
2. Add a configuration dictionary called switcher to the html_theme_options dict in conf.py. switcher should have 2
   keys:

    - json_url: the persistent location of the JSON file described above.
    - version_match: a string stating the version of the documentation that is currently being browsed.

3. Specify where to place the switcher in your page layout. For example, add the "version-switcher" template to one of
   the layout lists in html_theme_options (e.g., navbar_end, footer_start, etc.).

## Configuring the switcher in conf.py

To configure the version switcher, add a switcher dictionary to the html_theme_options dict in your conf.py file. For
example:

```python
version = my_package_name.__version__.replace("dev0", "")  # may differ

html_theme_options = {
    "navbar_end": ["version-switcher", "navbar-icon-links"],  # Where to place the switcher (at the end of navbar)
    "switcher": {
        "json_url": "https://xandratxan.github.io/template-library/latest/_static/switcher.json",
        # Version JSON location TODO: Update this URL
        "version_match": version,  # Current version
    }
}
```

1. **Configure switcher['json_url']**: The JSON file needs to be at a stable, persistent, fully-resolved URL (i.e., not
   specified as a path relative to the sphinx root of the current doc build). Each version of your documentation should
   point to the same URL, so that as new versions are added to the JSON file all the older versions of the docs will
   gain switcher dropdown entries linking to the new versions. This could be done in a few different ways:

    - The location could be one that is **always associated with the most recent documentation build** (i.e., if your
      docs
      server aliases “latest” to the most recent version, it could point to a location in the build tree of version
      “latest”). For example: `"json_url": "https://mysite.org/en/latest/_static/switcher.json"`. In this case, the JSON
      is versioned alongside the rest of the docs pages but only the most recent version is ever loaded (even by older
      versions of the docs).

    - The JSON could be stored **outside the doc build trees**. This probably means it would be outside the software
      repo,
      and would require you to add new version entries to the JSON file manually as part of your release process.
      Example: `"json_url": "https://mysite.org/switcher.json"`

    - **Key question if using sphinx-multiversion: does it generate a versions.json you can host somewhere
      stable? You can also generate your own in CI.** TODO: confirm this.

2. **Configure switcher['version_match']**:
    - This configuration value tells the switcher what docs version is currently being viewed, and is used to style the
      switcher (i.e., to highlight the current docs version in the switcher’s dropdown menu, and to change the text
      displayed on the switcher button).

    - Typically, you can re-use one of the sphinx variables version or release as the value of
      switcher['version_match']; which one you use depends on how granular your docs versioning is. See the Sphinx
      “project info” documentation for more information).

3. **Specify where to display the switcher**: Finally, tell the theme where on your site’s pages you want the switcher
   to appear. There are many choices here: you can add "version-switcher" to one of the locations in
   html_theme_options (e.g., navbar_end, footer_start, etc).

# sphinx-mutiversion

## How does it work?

Instead of running sphinx build, just run sphinx-multiversion from the root of your Git repository. It reads your Sphinx
conf.py file from the currently checked out Git branch for configuration, then generates a list of versions from local
or remote tags and branches. This data is written to a JSON file - if you want to have a look what data will be
generated, you can use the --dump-metadata flag.

KEY QUESTION: Where is this json file written? How to use it with PyData theme?

Then it copies the data for each version into separate temporary directories, builds the documentation from each of them
and writes the output to the output directory. The conf.py file from the currently checked out branch will be used to
build old versions, so it’s not necessary to make changes old branches or tags to add support for sphinx-multiversion.
This also means that theme improvements, template changes, etc. will automatically be applied to old versions without
needing to add commits.

## Setting the whitelist of branches/tags to build

Regarding whitelists:

By default, sphinx-multiversion builds all branches and tags, unless you pass a whitelist/blacklist pattern.

I want to use this mainly for publish the docs of versions published in PyPI. So, which branches/tags should I include?

Include the tags that exactly correspond to the releases you publish on PyPI, plus one branch for the live/latest docs
(typically `main` or `stable`). Common choices and their regexes:

- `main` + `v`\-prefixed semver (flexible): matches `v1`, `v1.2`, `v1.2.3`
- `main` + strict `vX.Y.Z` semver: only full releases like `v1.2.3` (excludes pre\-releases/partials) (RECOMMENDED)
- `main` + numeric tags (no `v` prefix): if your tags are `1.2.3`

Why should I include main? I do not want to be public until a new version is released, right?

Short answer: include main only if you want a continuously published "latest / unreleased" site. If you must keep docs
private until a release, exclude main and build/publish only on release tags.
Why include main?

- Provides a public, always-up-to-date "latest" or "nightly" docs for contributors and reviewers.
- Lets you test the full multiversion pipeline (switcher, theme, search) against unreleased changes.
- Helpful for QA before cutting a release.

**Note about tagging:**

- For release versions, use `vX.Y.Z` for release tags (e.g., `v1.0.0`, `v2.1.3`).
- For development versions, use pre-release tags like `v1.2.0-beta`, `v2.0.0-rc1`, or branches like `main` or `develop`.
- Whitelist only release tags.

```python
# TODO: configure whitelists in conf.py
```

# How to integrate sphinx-multiversion with PyData Sphinx Theme?

Summary (short)

- Build docs per-ref with `sphinx-multiversion`, produce a stable JSON index that the PyData theme reads, and publish
  the whole output tree (including a stable copy of the JSON) to GitHub Pages.
- `sphinx-multiversion` itself does not automatically publish a PyData `switcher.json`; use `--dump-metadata` or scan
  the built folders and write the JSON in CI or locally to a stable path such as
  `docs/_build/html/latest/_static/switcher.json`.
- Configure the PyData theme `html_theme_options['switcher']` to point at that stable URL and set `version_match`.

conf.py snippet (what to add)

- Add `html_baseurl`, the theme, and the switcher options. Do not need to add `sphinx-multiversion` to `extensions` (it
  runs externally); if you do add it, use the Python name `sphinx_multiversion`.

Brief explanation: this sets the theme, places the switcher in the navbar, and points the switcher to the stable JSON
URL; `version_match` highlights the current version.

```python
# python
version = "0.1.0"  # set from your package or tag
html_baseurl = "https://xandratxan.github.io/template-library/"  # site root

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "navbar_end": ["version-switcher", "navbar-icon-links"],
    "switcher": {
        "json_url": "https://xandratxan.github.io/template-library/latest/_static/switcher.json",
        "version_match": version,
    },
}
```

Build + generate stable `switcher.json` (local / CI)

- Brief explanation: run `sphinx-multiversion` to build versions, optionally capture `--dump-metadata`, then create a
  PyData-compatible `switcher.json` at the site root and copy it into `latest/_static/` so it is always reachable at a
  stable URL.

```bash
# bash
set -euo pipefail
OUT=docs/_build/html
SRC=docs

git fetch --all --tags
rm -rf "$OUT"
mkdir -p "$OUT"

# build allowed refs (tweak whitelist for CI)
sphinx-multiversion "$SRC" "$OUT" --whitelist-rx '^(main|v[0-9]+\.[0-9]+\.[0-9]+)$'

# generate PyData switcher JSON and copy to latest/_static
python - <<'PY'
import json, os, pathlib
out = pathlib.Path("docs/_build/html")
exclude = {"_static","_sources","_images","search"}
versions = []
for p in sorted(out.iterdir()):
    if p.is_dir() and p.name not in exclude and not p.name.startswith("."):
        versions.append({"name": p.name, "url": f"/{p.name}/"})
out.joinpath("switcher.json").write_text(json.dumps(versions, indent=2), encoding="utf-8")
(out / "latest" / "_static").mkdir(parents=True, exist_ok=True)
(out / "latest" / "_static" / "switcher.json").write_text(json.dumps(versions, indent=2), encoding="utf-8")
print("wrote switcher.json with", len(versions), "entries")
PY

# serve for local inspection
python -m http.server 8000 --directory "$OUT"
```

Notes (short)

- Ensure `git` refs are present (`git fetch --all --tags`) before running `sphinx-multiversion`.
- Set `html_baseurl` to your Pages root so canonical links are correct.
- Publish the enti

# Redirecting output tree to GitHub Pages?

# Setting a latest alias?
