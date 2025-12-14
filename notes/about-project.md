# About this project

A short reminder of the goals and main features of the `template-library` repository. Keep this file as the single place
to quickly recall why the template exists and what it provides.

## Purpose and goals

- Provide a minimal, well-structured Python library template for scientific / measurement tooling (ionizing radiation,
  metrology, physics) that is ready for development, testing, documentation and release.
- Make it easy to start a new library with best-practice layout and tooling: `src/` packaging, Hatch-based builds, Sphinx
  docs (PyData theme) and pytest-based tests. The layout is intentionally opinionated but lightweight to lower startup
  friction.
- Ship an out-of-the-box developer experience that includes:
  - a clear packaging configuration (`pyproject.toml` with Hatch),
  - test scaffolding and example unit/integration tests,
  - Sphinx documentation configured to read the package version and support multiversion builds,
  - and small helper scripts / notes for release hygiene.
- Provide a single, easy-to-find place for release guidance and pre-release checks so maintainers can produce
  reproducible releases and versioned docs with minimal manual steps.

## Main features

- src/ layout: production code lives in `src/template_library/` (avoids import pitfalls during development and testing).
- Packaging with Hatch (hatchling backend): `pyproject.toml` contains project metadata and dev extras for testing and docs.
- Package exposes a runtime version constant (`__version__` in `src/template_library/__init__.py`) so code and docs can
  read the canonical version programmatically.
- Release & helper tooling:
  - `scripts/check_versions.py` to validate version consistency across the package, `pyproject.toml` and docs.
  - `notes/publish-release.md` and a pre-release checklist (in `notes/`) that outline a safe release procedure.
- Documentation:
  - Sphinx-based docs in `docs/` using the `pydata_sphinx_theme`.
  - `docs/source/conf.py` is configured to import the package version and expose an RST substitution (|project_release|)
    so docs avoid hardcoded version strings.
  - Scaffolding for `sphinx-multiversion` is included so you can publish versioned docs (example settings in `conf.py`).
- Testing:
  - `pytest` scaffolding with unit and integration tests under `tests/` and shared fixtures under `tests/fixtures/`.
  - Recommendations for `pytest-cov` in dev extras to gather coverage information in CI.
- Runtime dependencies: a small, realistic set for numerical/tabular workflows (NumPy, pandas, SciPy) is included, but the
  template is easy to adapt to other domains.
- Examples & fixtures: small example modules (`my_module`, `other_module`) and sample fixtures (CSV / JSON) show common
  patterns for data-first libraries.
- CI / automation friendly: the repository layout, scripts and docs are prepared to be hooked into automation (tests,
  doc builds, and release workflows) with minimal additional configuration.

## Project layout (quick)

- src/template_library/ — library source code (public API should live here)
- tests/ — unit and integration tests, plus fixtures
- docs/ and docs/source/ — Sphinx documentation and build outputs
- pyproject.toml — packaging + metadata (Hatch)
- requirements.txt / dev-requirements.txt — convenience dependency lists

## Quick start (for development)

1. Create a virtual environment and install the package in editable mode with dev deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

2. Run tests:

```bash
pytest -q
```

3. Build docs (from `docs/`):

```bash
cd docs
make html
# open docs/build/html/index.html
```

## Publishing & release notes

- Use Hatch to build and publish distributions. Keep `pyproject.toml` as the single source of truth for metadata and
  dependencies.
- Follow semantic versioning for releases and document changes in a changelog (or GitHub releases).

## Audience / When to use this template

- Use this when starting a small-to-medium scientific Python library that needs numerical computation and tabular data
  support.
- Good starting point for reproducible code, tests, and documentation for research or engineering libraries.
