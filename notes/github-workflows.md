# GitHub Workflows — decision summary

A compact list of recommended GitHub Actions workflows for this library template. Use this to decide which workflows to implement.

1) CI — `ci.yml` (P0)
- Purpose: Run tests and produce coverage on push/PR.
- Triggers: push, pull_request.
- Essentials: Python 3.12 matrix (start with `ubuntu-latest`), install dev deps, run `pytest` (+ `pytest-cov`), produce coverage XML/JUnit.
- Why: Basic quality gate — implement first.

2) Docs build & deploy — `docs.yml` (P1)
- Purpose: Build Sphinx docs and publish to GitHub Pages.
- Triggers: push to `main` (optional PR previews/manual dispatch).
- Essentials: doc deps, `sphinx` (and `sphinx-multiversion` if multi-version), deploy to `gh-pages` (uses `GITHUB_TOKEN`).
- Why: Keep docs current and discoverable.

3) Lint & format — `lint.yml` (P1)
- Purpose: Fast static checks (ruff/black/isort or pre-commit).
- Triggers: pull_request, push.
- Essentials: run linters/format-checks; optional auto-fix job.
- Why: Prevent trivial style issues and keep codebase consistent.

4) Release / Publish — `release.yml` (P2)
- Purpose: Build dists and publish to PyPI + create GitHub Release on tag.
- Triggers: tag push (e.g., `v*.*.*`) or release publish.
- Essentials: `hatch`/build tools, `PYPI_API_TOKEN` secret, attach artifacts to release.
- Why: Automate publishing once CI/docs are reliable.

5) Dependabot + scheduled maintenance (P2)
- Purpose: Automated dependency updates and periodic long/extended tests.
- Triggers: Dependabot schedule; cron for nightly jobs.
- Essentials: `dependabot.yml` for updates; separate scheduled workflow for heavy matrices.

6) PR previews (optional, P3)
- Purpose: Build docs/tests for PRs and publish a preview link.
- Triggers: pull_request.
- Essentials: increases CI time/cost but improves review quality.

Key secrets/artifacts
- `PYPI_API_TOKEN` for publishing; `CODECOV_TOKEN` optional for Codecov; `GITHUB_TOKEN` used for GH Pages deploy.
- Artifacts to consider uploading: coverage XML, JUnit, built docs HTML.

Priority recommendation (short)
1) Implement `ci.yml` (tests + coverage).
2) Add `docs.yml` (docs build & deploy).
3) Add `lint.yml` to enforce style.
4) Enable `release.yml` when ready to publish (provide `PYPI_API_TOKEN`).
5) Add Dependabot and scheduled/nightly jobs as maintenance.
6) Add PR preview jobs if you want richer review feedback.

Tradeoffs — short note
- Start small (ubuntu + Python 3.12) to avoid wheel/build flakiness for NumPy/SciPy.
- Add caching for pip to speed CI. Multiversion docs need full git history (`fetch-depth: 0`).
