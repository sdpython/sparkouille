# -*- coding: utf-8 -*-
"""
@brief      test log(time=18s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
from pyquickhelper.pycode import add_missing_development_version
import sparkouille


class TestFunctionTestNotebookExpose(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["jyquickhelper"], __file__, hide=True)

    def test_notebook_expose_reduce(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertTrue(sparkouille is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "expose")
        test_notebook_execution_coverage(__file__, "reduce", folder,
                                         this_module_name="sparkouille", fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
