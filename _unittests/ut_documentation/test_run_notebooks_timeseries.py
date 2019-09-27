# -*- coding: utf-8 -*-
"""
@brief      test log(time=134s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
from pyquickhelper.pycode import add_missing_development_version, skipif_circleci
import sparkouille


class TestFunctionTestNotebookTimeSeries(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["jyquickhelper", "pymyinstall"], __file__, hide=True)

    @skipif_circleci("does not end on circleci")
    def test_notebook_map_reduce_timeseries(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        import pymyinstall  # pylint: disable=C0415
        self.assertTrue(sparkouille is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "sql")
        test_notebook_execution_coverage(__file__, "map_reduce_timeseries", folder,
                                         this_module_name="sparkouille", fLOG=fLOG,
                                         copy_files=["README.txt"], modules=[pymyinstall])


if __name__ == "__main__":
    unittest.main()
