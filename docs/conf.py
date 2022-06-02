# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import difflib
import os
import sys

from sphinx.domains.python import PythonDomain

sys.path.insert(0, os.path.abspath("../src"))


# -- Project information -----------------------------------------------------

project = "Datadog API Client for Python"
copyright = "2022, Datadog"
author = "Datadog"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["m2r2", "sphinx.ext.autodoc"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_material"

html_logo = "assets/images/logo.svg"
html_favicon = "assets/images/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["assets"]

html_sidebars = {
    "**": ["globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_theme_options = {
    # Set the name of the project to appear in the navigation.
    "nav_title": "Datadog API Client for Python",
    # Set the color and the accent color
    "color_primary": "deep-purple",
    "color_accent": "deep-purple",
    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/DataDog/datadog-api-client-python/",
    "repo_name": "datadog-api-client-python",
    # Visible levels of the global TOC; -1 means unlimited
    "globaltoc_depth": 3,
    # If False, expand all TOC entries
    "globaltoc_collapse": False,
    # If True, show hidden TOC entries
    "globaltoc_includehidden": False,
    # No version menu
    "version_dropdown": False,
}

add_module_names = False

autoclass_content = "both"


def find_obj(domain, env, modname, classname, name, type, searchmode=0):
    # skip parens
    if name[-2:] == '()':
        name = name[:-2]

    if not name:
        return []

    matches = []

    newname = None
    if searchmode == 1:
        if type is None:
            objtypes = list(domain.object_types)
        else:
            objtypes = domain.objtypes_for_role(type)
        if objtypes is not None:
            if modname and classname:
                fullname = modname + '.' + classname + '.' + name
                if fullname in domain.objects and domain.objects[fullname].objtype in objtypes:
                    newname = fullname
            if not newname:
                if modname and modname + '.' + name in domain.objects and \
                   domain.objects[modname + '.' + name].objtype in objtypes:
                    newname = modname + '.' + name
                elif name in domain.objects and domain.objects[name].objtype in objtypes:
                    newname = name
                else:
                    # "fuzzy" searching mode
                    searchname = '.' + name
                    matches = [(oname, domain.objects[oname]) for oname in domain.objects
                               if oname.endswith(searchname) and
                               domain.objects[oname].objtype in objtypes]
                    if len(matches) > 1:
                        close_match = difflib.get_close_matches(modname, [m[0] for m in matches], n=1, cutoff=0.1)
                        if close_match:
                            matches = [m for m in matches if m[0] == close_match[0]]
    else:
        # NOTE: searching for exact match, object type is not considered
        if name in domain.objects:
            newname = name
        elif type == 'mod':
            # only exact matches allowed for modules
            return []
        elif classname and classname + '.' + name in domain.objects:
            newname = classname + '.' + name
        elif modname and modname + '.' + name in domain.objects:
            newname = modname + '.' + name
        elif modname and classname and \
                modname + '.' + classname + '.' + name in domain.objects:
            newname = modname + '.' + classname + '.' + name
    if newname is not None:
        matches.append((newname, domain.objects[newname]))
    return matches


PythonDomain.find_obj = find_obj
