# -*- coding: utf-8 -*-
"""
@brief      test log(time=51s)
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


class TestFunctionTestNotebookProgf(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["jyquickhelper"], __file__, hide=True)

    def test_notebook_progf_reservoir(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertTrue(src.sparkouille is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "progf")
        test_notebook_execution_coverage(__file__, "reservoir", folder,
                                         this_module_name="sparkouille", fLOG=fLOG)

    def test_notebook_progf_skewed(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertTrue(src.sparkouille is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "progf")
        test_notebook_execution_coverage(__file__, "skewed", folder,
                                         this_module_name="sparkouille", fLOG=fLOG)

    def test_notebook_progf_reducers(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertTrue(src.sparkouille is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "progf")
        test_notebook_execution_coverage(__file__, "reducers", folder,
                                         this_module_name="sparkouille", fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
