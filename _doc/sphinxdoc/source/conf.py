# -*- coding: utf-8 -*-
import sys
import os
# import sphinx_redactor_theme
# import karma_sphinx_theme
import pydata_sphinx_theme
from pyquickhelper.helpgen.default_conf import set_sphinx_variables


sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
local_template = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "phdoc_templates")

set_sphinx_variables(__file__, "sparkouille", "Xavier Dupré", 2023,
                     "pydata_sphinx_theme", ['_static'],
                     locals(), extlinks=dict(issue=(
                         'https://github.com/sdpython/sparkouille/issues/%s',
                         'issue %s')),
                     title="sparkouille", book=True)

blog_root = "http://www.xavierdupre.fr/app/sparkouille/helpsphinx/"

html_css_files = ['my-styles.css']

html_logo = "_static/project_ico.png"

language = "fr"

mathdef_link_only = True

epkg_dictionary['cacher'] = 'https://fr.wikipedia.org/wiki/Algorithmes_de_remplacement_des_lignes_de_cache'
epkg_dictionary['C'] = 'https://fr.wikipedia.org/wiki/C'
epkg_dictionary['C#'] = 'https://fr.wikipedia.org/wiki/C_sharp'
epkg_dictionary['Cloudera'] = 'https://www.cloudera.com/'
epkg_dictionary['ENSAE'] = 'http://www.ensae.fr/'
epkg_dictionary['Eurostat'] = 'https://data.europa.eu/euodp/fr/data/publisher/estat'
epkg_dictionary[
    'générateur'] = 'https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rateur_(informatique)'
epkg_dictionary['GIL'] = 'http://www.xavierdupre.fr/app/teachpyx/helpsphinx/notebooks/gil_example.html'
epkg_dictionary['Hadoop'] = 'https://fr.wikipedia.org/wiki/Hadoop'
epkg_dictionary['hadoop'] = 'https://fr.wikipedia.org/wiki/Hadoop'
epkg_dictionary['HortonWorks'] = 'https://fr.hortonworks.com/'
epkg_dictionary['HortonWork'] = 'https://fr.hortonworks.com/'
epkg_dictionary['HIVE'] = 'https://fr.wikipedia.org/wiki/Apache_Hive'
epkg_dictionary['Hive'] = 'https://fr.wikipedia.org/wiki/Apache_Hive'
epkg_dictionary['itérateur'] = 'https://fr.wikipedia.org/wiki/It%C3%A9rateur'
epkg_dictionary['joblib'] = 'https://joblib.readthedocs.io/en/latest/'
epkg_dictionary['Kaggle'] = 'https://www.kaggle.com/'
epkg_dictionary['map/reduce'] = 'https://fr.wikipedia.org/wiki/MapReduce'
epkg_dictionary['numba'] = 'https://numba.pydata.org/'
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
