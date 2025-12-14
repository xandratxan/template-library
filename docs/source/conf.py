# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Configuration for finding your package source code (Crucial for `src` layout)
DOCS_SOURCE_DIR = os.path.dirname(__file__)  # Absolute path to conf.py directory
PROJECT_ROOT = os.path.abspath(os.path.join(DOCS_SOURCE_DIR, '..', '..'))  # Absolute path to project root
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'src'))  # Add the 'src' directory to sys.path

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TemplateLibrary'
copyright = '2025, Xandra Campo'
author = 'Xandra Campo'
release = 'v0.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "pydata_sphinx_theme",
    "sphinx_design",
    "sphinx.ext.autosummary",
    "numpydoc",
]

templates_path = ['_templates']
exclude_patterns = []

autosummary_generate = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_title = f'{project}'
html_theme_options = {
    "show_nav_level": 2,
    "navbar_end": ["version-switcher", "navbar-icon-links"],
    "switcher": {
        "json_url": "_static/versions.json",  # TODO: Update this path
        "version_match": release,
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/lmri-met/metpyir",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        }
    ],
}
