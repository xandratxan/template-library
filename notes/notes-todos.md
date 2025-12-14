## Notes & TODOs

Documentation:

- [ ] Version switcher: Add latest version to switcher.
- Maybe I could use the docs to explain the main features of the template and how to use it for new projects?

Testing:

- [ ] I want to use `pytest-cov` to measure test coverage and report it in the CI.
- [ ] I want to get typical test badges (coverage, tests passing) in the `README.md`.

GitHub Workflows:

- See [GitHub Workflows — decision summary](github-workflows.md) for detailed workflow recommendations.
- [ ] Implement CI — `ci.yml` (P0) - Purpose: Run tests and produce coverage on push/PR.
- [X] Docs build & deploy — `docs.yml` (P1) - Purpose: Build Sphinx docs and publish to GitHub Pages.
- [ ] Release / Publish — `release.yml` (P2) - Purpose: Build dists and publish to PyPI + create GitHub Release on tag.
- [ ] Lint & format — `lint.yml` (P1) - Purpose: Fast static checks (ruff/black/isort or pre-commit).

Others:

- How to auto update the `CHANGELOG.md`?
- How to deal with version being hardcoded in multiple places (e.g., config files, src, docs)?
- Get a DOI for the project via Zenodo and add the badge to the `README.md`.
- Get LFX Insights set up for the project and add the badge to the `README.md`.
