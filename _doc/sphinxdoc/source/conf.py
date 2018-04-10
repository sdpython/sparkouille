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

epkg_dictionary['C#'] = 'https://fr.wikipedia.org/wiki/C_sharp'
epkg_dictionary['Cloudera'] = 'https://www.cloudera.com/'
epkg_dictionary['ENSAE'] = 'http://www.ensae.fr/'
epkg_dictionary['Eurostat'] = 'https://data.europa.eu/euodp/fr/data/publisher/estat'
epkg_dictionary['hadoop'] = 'https://fr.wikipedia.org/wiki/Hadoop'
epkg_dictionary['HortonWorks'] = 'https://fr.hortonworks.com/'
epkg_dictionary['HIVE'] = 'https://fr.wikipedia.org/wiki/Apache_Hive'
epkg_dictionary['Hive'] = 'https://fr.wikipedia.org/wiki/Apache_Hive'
epkg_dictionary['map/reduce'] = 'https://fr.wikipedia.org/wiki/MapReduce'
epkg_dictionary['PIG'] = 'https://fr.wikipedia.org/wiki/Apache_Pig'
epkg_dictionary['pyenbc'] = 'http://www.xavierdupre.fr/app/pyenbc/helpsphinx/index.html'
epkg_dictionary['presto'] = 'https://prestodb.io/'
epkg_dictionary['programmation fonctionnelle'] = 'https://fr.wikipedia.org/wiki/Programmation_fonctionnelle'
epkg_dictionary['pyspark'] = 'https://spark.apache.org/docs/latest/api/python/index.html'
epkg_dictionary['Spark'] = "https://spark.apache.org/"
epkg_dictionary['spark'] = "https://spark.apache.org/"
epkg_dictionary['sqlite3'] = "https://docs.python.org/3.6/library/sqlite3.html"
epkg_dictionary['SQL'] = 'https://fr.wikipedia.org/wiki/Structured_Query_Language'
epkg_dictionary['U-SQL'] = 'https://docs.microsoft.com/en-us/azure/data-lake-analytics/data-lake-analytics-u-sql-programmability-guide'
epkg_dictionary['Yahoo'] = 'https://fr.yahoo.com/'
