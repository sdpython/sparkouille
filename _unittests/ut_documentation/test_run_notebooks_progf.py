#-*- coding: utf-8 -*-
"""
@brief      test log(time=121s)
"""

import sys
import os
import unittest


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


try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..", "..", "pyquickhelper", "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_


try:
    import pymyinstall as skip__
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..", "..", "pymyinstall", "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pymyinstall as skip__


import src.sparkouille
from pyquickhelper.loghelper import fLOG
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
from pyquickhelper.pycode import add_missing_development_version


class TestFunctionTestNotebookProgf(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["jyquickhelper"], __file__, hide=True)

    def test_notebook_example_progf_reservoir(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertTrue(src.sparkouille is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "progf")
        test_notebook_execution_coverage(__file__, "reservoir", folder,
                                         this_module_name="sparkouille", fLOG=fLOG)

    def test_notebook_example_progf_skewed(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertTrue(src.sparkouille is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "progf")
        test_notebook_execution_coverage(__file__, "skewed", folder,
                                         this_module_name="sparkouille", fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
