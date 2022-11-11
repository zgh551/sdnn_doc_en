# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
# import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = 'SDNN'
copyright = '2022, Nanjing SemiDrive® Technology Co., Ltd. All Rights Reserved.'
author = 'SemiDrive'

# The full version, including alpha/beta/rc tags
release = '2.2.3'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinx.ext.autodoc',
  'sphinx.ext.doctest',
  'sphinx.ext.intersphinx',
  'sphinx.ext.todo',
  'sphinx.ext.coverage',
  'sphinx.ext.mathjax',
  'sphinx.ext.ifconfig',
  'sphinx.ext.viewcode',
  'sphinx.ext.githubpages',
  'sphinx_tabs.tabs',
  'sphinxmark',
]

sphinxmark_enable = True
sphinxmark_div = 'document'
sphinxmark_image = 'text'
#sphinxmark_text = "SemiDrive Confidential For Desay Use Only"
#sphinxmark_text = "SemiDrive Confidential For xxx Use Only"
sphinxmark_text = "SemiDrive Confidential For Internal Use Only"
sphinxmark_text_size = 40
sphinxmark_text_width = 1500
sphinxmark_text_rotation = 45
sphinxmark_text_spacing = 800

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'classic'
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
  'display_version': False,
  'navigation_depth': 2,
  'collapse_navigation': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = '_static/images/logo/logo1.png'

html_css_files = [
    'css/custom.css',
]