# -*- coding: utf-8 -*-
"""
@brief      test log(time=121s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
from pyquickhelper.pycode import add_missing_development_version


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src


import src.sparkouille


class TestFunctionTestNotebookSql(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["jyquickhelper", "pymyinstall"], __file__, hide=True)

    def test_notebook_example_sql(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        import pymyinstall
        self.assertTrue(src.sparkouille is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "sql")
        test_notebook_execution_coverage(__file__, "sql", folder,
                                         this_module_name="sparkouille", fLOG=fLOG,
                                         copy_files=["README.txt"], modules=[pymyinstall])

    def test_notebook_example_timeseries(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        import pymyinstall
        self.assertTrue(src.sparkouille is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "sql")
        test_notebook_execution_coverage(__file__, "sql", folder,
                                         this_module_name="sparkouille", fLOG=fLOG,
                                         copy_files=["README.txt"], modules=[pymyinstall])


if __name__ == "__main__":
    unittest.main()
