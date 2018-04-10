#-*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
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
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_

from pyquickhelper.pycode import ExtTestCase
from src.sparkouille.fctmr import mapper, reducer


class TestFctMr(ExtTestCase):

    def test_mapper(self):
        res = mapper(lambda x: x + 1, [4, 5])
        self.assertNotIsInstance(res, list)
        self.assertEqual(list(res), [5, 6])

    def test_reducer(self):
        res = reducer(lambda x: x[0], [
                      ('a', 1), ('b', 2), ('a', 3)], asiter=False)
        self.assertEqual(
            list(res), [('a', [('a', 1), ('a', 3)]), ('b', [('b', 2)])])
        res2 = reducer(lambda x: x[0], [
                       ('a', 1), ('b', 2), ('a', 3)], asiter=False, sort=False)
        self.assertEqual(
            list(res2), [('a', [('a', 1)]), ('b', [('b', 2)]), ('a', [('a', 3)])])
        res3 = reducer(lambda x: x[0], [
                       ('a', 1), ('b', 2), ('a', 3)], asiter=True, sort=False)
        res4 = [(a, list(b)) for a, b in res3]
        self.assertEqual(
            list(res4), [('a', [('a', 1)]), ('b', [('b', 2)]), ('a', [('a', 3)])])
        res5 = reducer(lambda x: x[0], [
                       ('a', 1), ('b', 2), ('a', 3)], asiter=True, sort=True)
        res6 = [(a, list(b)) for a, b in res5]
        self.assertEqual(
            list(res6), [('a', [('a', 1), ('a', 3)]), ('b', [('b', 2)])])


if __name__ == "__main__":
    unittest.main()
