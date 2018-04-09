#-*- coding: utf-8 -*-
import sys
import os
import datetime
import re
import sphinx_redactor_theme


sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.split(__file__)[0],
            "..",
            "..",
            "..",
            "..",
            "pyquickhelper",
            "src")))

local_template = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "phdoc_templates")

from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet
set_sphinx_variables(__file__, "sparkouille", "Xavier Dupré", 2018,
                     "sphinx_redactor_theme", sphinx_redactor_theme.get_html_theme_path(),
                     locals(), extlinks=dict(
                         issue=('https://github.com/sdpython/sparkouille/issues/%s', 'issue')),
                     title="sparkouille", book=True)

blog_root = "http://www.xavierdupre.fr/app/sparkouille/helpsphinx/"

html_context = {
    'css_files': get_default_stylesheet() + ['_static/my-styles.css'],
}

html_logo = "project_ico.png"

html_sidebars = {}

language = "en"

mathdef_link_only = True

epkg_dictionary['pyspark'] = 'https://spark.apache.org/docs/latest/api/python/index.html'
epkg_dictionary['Spark'] = "https://spark.apache.org/"
epkg_dictionary['spark'] = "https://spark.apache.org/"
