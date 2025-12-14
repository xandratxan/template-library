## Notes & TODOs

Documentation:

- I want to get typical documentation badges (docs build passing, docs coverage) in the `README.md`.

Testing:

- I want to use `pytest-cov` to measure test coverage and report it in the CI.
- I want to get typical test badges (coverage, tests passing) in the `README.md`.

GitHub Workflows:

- See [GitHub Workflows — decision summary](github-workflows.md) for detailed workflow recommendations.

Others:

- How to deal with version being hardcoded in multiple places (e.g., `pyproject.toml`,
  `src/template_library/__init__.py`, documentation (`conf.py` and `index.rst`))? Consider using `setuptools_scm` or
  similar tools to manage versioning automatically from Git tags.
- Docs: Maybe I could use the documentation to explain the main features of the template and how to use it for new
  projects?
- Docs: Version switcher: Add latest version to switcher.

**NOW**:
