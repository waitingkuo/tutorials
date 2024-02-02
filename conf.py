#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PyTorch Tutorials documentation build configuration file, created by
# sphinx-quickstart on Wed Mar  8 22:38:10 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
#

# Because the sphinx gallery might take a long time, you can control specific
# files that generate the results using `GALLERY_PATTERN` environment variable,
# For example to run only `neural_style_transfer_tutorial.py`:
#   GALLERY_PATTERN="neural_style_transfer_tutorial.py" make html
# or
#   GALLERY_PATTERN="neural_style_transfer_tutorial.py" sphinx-build . _build
#
# GALLERY_PATTERN variable respects regular expressions.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('./.jenkins'))
import pytorch_sphinx_theme
import torch
import numpy
import gc
import glob
import random
import shutil
from custom_directives import IncludeDirective, GalleryItemDirective, CustomGalleryItemDirective, CustomCalloutItemDirective, CustomCardItemDirective
import distutils.file_util
import re
from get_sphinx_filenames import SPHINX_SHOULD_RUN

import plotly.io as pio
pio.renderers.default = 'sphinx_gallery'


try:
    import torchvision
except ImportError:
    import warnings
    warnings.warn('unable to load "torchvision" package')
import pytorch_sphinx_theme

rst_epilog ="""
.. |edit| image:: /_static/pencil-16.png
           :width: 16px
           :height: 16px
"""

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.katex',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'sphinx_gallery.gen_gallery',
    'sphinx_design'
]

intersphinx_mapping = {
    "torch": ("https://pytorch.org/docs/stable/", None),
    "tensordict": ("https://pytorch.github.io/tensordict/", None),
    "torchrl": ("https://pytorch.org/rl/", None),
    "torchaudio": ("https://pytorch.org/audio/stable/", None),
    "torchtext": ("https://pytorch.org/text/stable/", None),
    "torchvision": ("https://pytorch.org/vision/stable/", None),
}

# -- Sphinx-gallery configuration --------------------------------------------

def reset_seeds(gallery_conf, fname):
    torch.cuda.empty_cache()
    torch.manual_seed(42)
    torch.set_default_device(None)
    random.seed(10)
    numpy.random.seed(10)
    gc.collect()

sphinx_gallery_conf = {
    'examples_dirs': ['beginner_source', 'intermediate_source',
                      'advanced_source', 'recipes_source', 'prototype_source'],
    'gallery_dirs': ['beginner', 'intermediate', 'advanced', 'recipes', 'prototype'],
    'filename_pattern': re.compile(SPHINX_SHOULD_RUN),
    'promote_jupyter_magic': True,
    'backreferences_dir': None,
    'first_notebook_cell': ("# For tips on running notebooks in Google Colab, see\n"
                            "# https://pytorch.org/tutorials/beginner/colab\n"
                            "%matplotlib inline"),
    'reset_modules': (reset_seeds),
    'ignore_pattern': r'_torch_export_nightly_tutorial.py',
    'pypandoc': {'extra_args': ['--mathjax'],
                 'filters': ['.jenkins/custom_pandoc_filter.py'],
    },
}

if os.getenv('GALLERY_PATTERN'):
    # GALLERY_PATTERN is to be used when you want to work on a single
    # tutorial.  Previously this was fed into filename_pattern, but
    # if you do that, you still end up parsing all of the other Python
    # files which takes a few seconds.  This strategy is better, as
    # ignore_pattern also skips parsing.
    # See https://github.com/sphinx-gallery/sphinx-gallery/issues/721
    # for a more detailed description of the issue.
    sphinx_gallery_conf['ignore_pattern'] = r'/(?!' + re.escape(os.getenv('GALLERY_PATTERN')) + r')[^/]+$'

for i in range(len(sphinx_gallery_conf['examples_dirs'])):
    gallery_dir = sphinx_gallery_conf['gallery_dirs'][i]
    source_dir = sphinx_gallery_conf['examples_dirs'][i]
    # Create gallery dirs if it doesn't exist
    try:
        os.mkdir(gallery_dir)
    except OSError:
        pass

    # Copy rst files from source dir to gallery dir
    for f in glob.glob(os.path.join(source_dir, '*.rst')):
        distutils.file_util.copy_file(f, gallery_dir, update=True)


# Add any paths that contain templates here, relative to this directory.


templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'PyTorch Tutorials'
copyright = '2024, PyTorch'
author = 'PyTorch contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = str(torch.__version__)
# The full version, including alpha/beta/rc tags.
release = str(torch.__version__)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
exclude_patterns += sphinx_gallery_conf['examples_dirs']
exclude_patterns += ['*/index.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

# # Theme options are theme-specific and customize the look and feel of a theme
# # further.  For a list of options available for each theme, see the
# # documentation.
# #

# html_theme_options = {
#     'page_width': '1000px',
#     'fixed_sidebar': True,
#     'code_font_size': '0.87em',
#     'sidebar_includehidden': True
# }

# # Add any paths that contain custom static files (such as style sheets) here,
# # relative to this directory. They are copied after the builtin static files,
# # so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# # Custom sidebar templates, maps document names to template names.
# html_sidebars = {
#     'index': ['sidebarlogo.html', 'globaltoc.html', 'searchbox.html', 'sourcelink.html'],
#     '**': ['sidebarlogo.html', 'globaltoc.html', 'searchbox.html', 'sourcelink.html']
# }


html_theme = 'pytorch_sphinx_theme'
html_theme_path = [pytorch_sphinx_theme.get_html_theme_path()]
html_logo = '_static/img/pytorch-logo-dark.svg'
html_theme_options = {
    'pytorch_project': 'tutorials',
    'collapse_navigation': False,
    'display_version': True,
    'navigation_with_keys': True,
    'logo_only': False,
    'analytics_id': 'GTM-T8XT4PS',
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'PyTorchTutorialsdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'PyTorchTutorials.tex', 'PyTorch Tutorials',
     'Sasank, PyTorch contributors', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pytorchtutorials', 'PyTorch Tutorials',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'PyTorchTutorials', 'PyTorch Tutorials',
     author, 'PyTorchTutorials', 'One line description of project.',
     'Miscellaneous'),
]

html_css_files = [
        'https://cdn.jsdelivr.net/npm/katex@0.10.0-beta/dist/katex.min.css',
        'css/custom.css',
        'css/custom2.css'
    ]

def setup(app):
    # NOTE: in Sphinx 1.8+ `html_css_files` is an official configuration value
    # and can be moved outside of this function (and the setup(app) function
    # can be deleted).
    #html_css_files = [
    #    'https://cdn.jsdelivr.net/npm/katex@0.10.0-beta/dist/katex.min.css',
    #    'css/custom.css'
    #]
    # In Sphinx 1.8 it was renamed to `add_css_file`, 1.7 and prior it is
    # `add_stylesheet` (deprecated in 1.8).
    #add_css = getattr(app, 'add_css_file', app.add_stylesheet)
    #for css_file in html_css_files:
    #    add_css(css_file)
    # Custom CSS
    #app.add_stylesheet('css/pytorch_theme.css')
    # app.add_stylesheet('https://fonts.googleapis.com/css?family=Lato')
    # Custom directives
    app.add_directive('includenodoc', IncludeDirective)
    app.add_directive('galleryitem', GalleryItemDirective)
    app.add_directive('customgalleryitem', CustomGalleryItemDirective)
    app.add_directive('customcarditem', CustomCardItemDirective)
    app.add_directive('customcalloutitem', CustomCalloutItemDirective)
