# -*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
from pyquickhelper.pycode import ExtTestCase


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


from src.sparkouille.fctmr.pyparallel_fctmr import pyparallel_mapper


class TestPyParallelFctMr(ExtTestCase):

    def test_pyparallel_mapper(self):
        res = pyparallel_mapper(lambda x: x + 1, [4, 5])
        self.assertNotIsInstance(res, list)
        self.assertEqual(list(res), [5, 6])


if __name__ == "__main__":
    unittest.main()
