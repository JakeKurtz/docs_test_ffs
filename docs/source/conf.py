# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RexHue Paints'
copyright = '2024, Jake Kurtz'
author = 'Jake Kurtz'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = []
extensions = ["myst_parser",'sphinx_rtd_dark_mode',"sphinx_multiversion",]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_dark_mode'
html_logo = "_images/rexhue_logo_inv.png"
html_static_path = ['_static']

html_sidebars = {
    '**': [
        'versioning.html',
    ],
}

html_css_files = [
    'css/custom.css',
]
