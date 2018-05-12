# -*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase


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


from src.sparkouille.datasets import table_mortalite_euro_stat


class TestEuroStat(ExtTestCase):

    def test_mortalite_euro_stat(self):
        temp = get_temp_folder(__file__, "temp_table_mortalite_euro_stat")
        outfile = os.path.join(temp, "mortalite_table.txt")
        table_mortalite_euro_stat(
            whereTo=temp, final_name=outfile, fLOG=fLOG, stop_at=100)
        self.assertExists(outfile)


if __name__ == "__main__":
    unittest.main()
