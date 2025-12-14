# About this project

A short reminder of the goals and main features of the `template-library` repository. Keep this file as the single place to quickly recall why the template exists and what it provides.

## Purpose and goals

- Provide a minimal, well-structured Python library template for scientific / measurement tooling (ionizing radiation, metrology, physics).
- Make it easy to start a new library with best-practice layout: `src/` packaging, Hatch-based builds, Sphinx docs, and pytest-based tests.
- Include a small, realistic dependency set (NumPy, pandas, SciPy) so the template is ready for numerical and tabular data workflows.
- Be opinionated but lightweight: sensible defaults for packaging, docs, testing, and CI-ready structure.

## Main features

- src/ layout: production code lives in `src/template_library/` to avoid import pitfalls during development.
- Packaging with Hatch (hatchling backend) using `pyproject.toml` for modern builds.
- Runtime dependencies included for scientific workflows: NumPy, pandas, SciPy.
- Test scaffolding with `pytest` (unit and integration test folders) and fixtures under `tests/fixtures/`.
- Documentation built with Sphinx (source under `docs/source/`, prebuilt HTML under `docs/build/html/`).
- Minimal examples and sample fixtures to demonstrate common data patterns (CSV / JSON fixtures included).

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

- Use Hatch to build and publish distributions. Keep `pyproject.toml` as the single source of truth for metadata and dependencies.
- Follow semantic versioning for releases and document changes in a changelog (or GitHub releases).

## Audience / When to use this template

- Use this when starting a small-to-medium scientific Python library that needs numerical computation and tabular data support.
- Good starting point for reproducible code, tests, and documentation for research or engineering libraries.

## Notes & TODOs

Documentation:

- I want to use self-hosted multiversion docs via GitHub Pages. I need multiversion support tools from Sphinx that integrates well with the PyData Sphinx theme.
- I want to get typical documentation badges (docs build passing, docs coverage) in the `README.md`.

Testing:

- I want to use `pytest-cov` to measure test coverage and report it in the CI.
- I want to get typical test badges (coverage, tests passing) in the `README.md`.

GitHub Workflows: 

- See [GitHub Workflows — decision summary](github-workflows.md) for detailed workflow recommendations.

Other:

- How to deal with version being hardcoded in multiple places (e.g., `pyproject.toml`, `src/template_library/__init__.py`, documentation (`conf.py` and `index.rst`))? Consider using `setuptools_scm` or similar tools to manage versioning automatically from Git tags.