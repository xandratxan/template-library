# Minimum viable repository layout

Here is the basic directory tree for a **minimum viable repository layout** for a Python package:

```
my-python-package/
├── .gitignore
├── dev-requirements.txt
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── src
│ └── my_package
│     ├── __init__.py
│     ├── my_module.py
│     └── other_module.py
└── tests
    ├── fixtures
    │ ├── sample_serial_data.json
    │ └── sample_tabular_data.csv
    ├── __init__.py
    ├── integration
    │ └── __init__.py
    └── unit
        └── __init__.py

```

### ✨ Next recommended improvements

While optional for the minimum layout, you may also add:

* **Documentation:** Start a `docs/` directory using tools like Sphinx or MkDocs.
*
* Continuous Integration (CI): a GitHub Actions workflow or other CI config to run tests and linters on push/PRs.
* Linting and formatting: `flake8`, `ruff`, and `black` in your dev requirements to maintain consistent style.
*
* I can add additional badges (e.g., PyPI downloads, license details, pre-commit status) or adjust badge styles/sizing.
* I can also create the referenced ci.yml workflow and a basic Codecov setup if you'd like.
*
* Add an automated release workflow that publishes to Zenodo and updates the DOI badge.
* Add a `CHANGELOG.md` file to track changes across versions.
*
* Utility scripts: a `scripts/` directory for helper scripts related to development or deployment.

# Last badges:

Package:
[![PyPI version](https://img.shields.io/pypi/v/template-library.svg)](https://pypi.org/project/template-library/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/template-library.svg)](https://pypi.org/project/template-library/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/template-library.svg)](https://pypi.org/project/template-library/)
[![PyPI Development Status](https://img.shields.io/pypi/status/template-library.svg)](https://pypi.org/project/template-library/)

Metadata:
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://choosealicense.com/licenses/bsd-3-clause/)
[![License](https://img.shields.io/badge/license-BSD%203--Clause-blue.svg)](https://github.com/xandratxan/template-library/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![LFX Insights Health](https://img.shields.io/badge/LFX%20Insights-Health-blue.svg)](https://lfxinsights.io/project/<OWNER>/<REPO>)  <!-- Replace <OWNER> and <REPO> with your GitHub owner and repository name, e.g. xandratxan/template-library -->

Testing:
[![Tests](https://github.com/xandratxan/template-library/actions/workflows/ci.yml/badge.svg)](https://github.com/xandratxan/template-library/actions)
[![Coverage](https://img.shields.io/codecov/c/gh/xandratxan/template-library.svg)](https://codecov.io/gh/xandratxan/template-library)

