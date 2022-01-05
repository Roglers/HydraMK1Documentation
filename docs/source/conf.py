# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Hydra MK1'
copyright = '2022, Rogler'
author = 'S. Rogler'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

div.leftside {
    width: 414px;
    padding: 0px 3px 0px 0px;
    float: left;
}

div.rightside {
    margin-left: 425px;
}
