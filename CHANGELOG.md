# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

* [Describe any new features added since the last release]

### Changed

* [Describe any changes made since the last release]

### Deprecated

* [Describe any deprecated features since the last release]

### Removed

* [Describe any removed features since the last release]

### Fixed

* [Describe any bug fixes made since the last release]

### Security

* [Describe any security fixes made since the last release]

## [0.0.4] - 2025-12-14

### Added

* Initial public pre-release of the template library.
* Project layout and packaging
    * `src/template_library/` — library source using the recommended `src/` layout.
    * `pyproject.toml` configured for Hatch (hatchling) with project metadata and dev extras for testing and docs.
* Runtime versioning
    * `__version__` exposed in `src/template_library/__init__.py` for runtime introspection and docs.
* Documentation
    * Sphinx docs scaffolded under `docs/` using the `pydata_sphinx_theme`.
    * Scaffolding for `sphinx-multiversion` included to support versioned docs.
* Tests and examples
    * `tests/` includes unit and integration test scaffolding and fixtures (`tests/fixtures/`).
    * Example modules: `template_library.my_module` and `template_library.other_module` with sample fixtures (CSV/JSON).
* Release & helper tooling
    * `notes/publish-release.md` and a pre-release checklist describe a recommended release workflow.
    * `scripts/check_versions.py` checks version consistency across the package, `pyproject.toml`, and docs.
* CI & automation readiness
    * Repo layout and scripts prepared to be integrated into CI workflows for tests, doc builds, and release automation.