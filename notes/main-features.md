# Goal

A minimal starting point for developing a Python library: the template sets up a clear project layout, packaging, basic
testing, and documentation so you can focus on implementing domain code quickly.
It aims to be small, well-documented, and easy, enabling to adopt best practices without boilerplate.

Secondary goals:

- Provide a reproducible project structure that follows common Python packaging conventions.
- Demonstrate basic testing and documentation workflows that are easy to extend.
- Include lightweight release and versioning helpers to reduce friction when publishing.

- Make it easy to start a new library package with best-practices.

# Main features

## General

- Minimal, opinionated project layout using the recommended "src/" layout (package under `src/template_library/`).
- Package metadata and build configured in `pyproject.toml` (Hatch/hatchling build backend).
- Runtime version exposed via `src/template_library/__init__.py` (`__version__`) for easy introspection and docs.
- BSD-3-Clause license, semantic versioning convention, and a `CHANGELOG.md` scaffold.
- README with basic instructions and a docs build badge (docs build referenced in README).

## Source code

- Simple, documented example modules demonstrating constants, classes, and functions.
- Clear, minimal public API and docstrings (NumPy-style) in source modules to support autosummary and documentation
  generation and testing
- `__version__` present in package init for release/version checks.

## Documentation

- Sphinx documentation scaffold under `docs/` with `docs/source/conf.py` configured for the `src/` layout.
- Uses `pydata_sphinx_theme`, `sphinx_design`, `numpydoc` and `sphinx-multiversion` (scaffolded) for theme, formatting
  and versioned docs.
- Autosummary generation enabled to auto-create API pages from docstrings.
- Publish the docs to GitHub Pages using CI with GitHub Actions workflows.

## Testing

- `tests/` includes unit tests and an integration test demonstrating how to exercise the package with `pytest`.
- [] Example fixtures are provided under `tests/fixtures/` (sample JSON and CSV) to show common test data patterns.
- [] Development extras include `pytest` and `pytest-cov` in the project dev dependencies.
- Tests demonstrate basic behavior checks and exception handling for example modules.

## Packaging & release

- `pyproject.toml` contains project metadata (name, version, description, authors, classifiers) and runtime
  dependencies.
- Hatch (hatchling) is configured as the build backend; `tool.hatch.build` includes packaging rules for the `src`
  package.
- Release-supporting files: `CHANGELOG.md`, `notes/publish-release.md`, and `scripts/check_versions.py` assist with
  release tasks.
- Example of runtime version consistency checking implemented in `scripts/check_versions.py`.

## Automation

- Scripts folder includes:
  - a small helper to check consistency of version strings across files.
  - a small helper to serve the documentation locally for review.
- CI-ready repository layout and scripts prepared to be integrated into CI workflows for tests, doc builds, and release
  automation.
- Documentation ready to be built and deployed to GitHuB Pages via CI (using a GitHub Actions workflow).

# Tools & technologies used

- Python 3.12+ (project requires Python >=3.12).
- Packaging: Hatch / hatchling (pyproject.toml build-system).
- Testing: pytest, pytest-cov.
- Documentation: Sphinx, pydata_sphinx_theme, sphinx-multiversion, sphinx_design, numpydoc.
- Automation: GitHub Actions.
- Publication: PyPI, GitHub Releases, GitHub Pages.
