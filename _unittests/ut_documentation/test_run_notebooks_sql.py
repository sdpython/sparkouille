# -*- coding: utf-8 -*-
"""
@brief      test log(time=80s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
from pyquickhelper.pycode import add_missing_development_version
import sparkouille


class TestFunctionTestNotebookSql(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["jyquickhelper", "pymyinstall"], __file__, hide=True)

    def test_notebook_sql_map_reduce(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        import pymyinstall  # pylint: disable=C0415
        self.assertTrue(sparkouille is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "sql")
        test_notebook_execution_coverage(__file__, "sql_map_reduce", folder,
                                         this_module_name="sparkouille", fLOG=fLOG,
                                         copy_files=["README.txt"], modules=[pymyinstall])


if __name__ == "__main__":
    unittest.main()
