# -*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""
import unittest
from pyquickhelper.pycode import ExtTestCase
from sparkouille.fctmr.pyparallel_fctmr import pyparallel_mapper


class TestPyParallelFctMr(ExtTestCase):

    def test_pyparallel_mapper(self):
        res = pyparallel_mapper(lambda x: x + 1, [4, 5])
        self.assertNotIsInstance(res, list)
        self.assertEqual(list(res), [5, 6])


if __name__ == "__main__":
    unittest.main()
