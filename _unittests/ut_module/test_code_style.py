"""
@brief      test log(time=0s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import check_pep8, ExtTestCase, add_missing_development_version


class TestCodeStyle(ExtTestCase):

    def setUp(self):
        add_missing_development_version(
            ["jyquickhelper", "pymyinstall"], __file__, hide=True)

    def test_style_src(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        src_ = os.path.normpath(os.path.join(thi, "..", "..", "src"))
        check_pep8(src_, fLOG=fLOG,
                   skip=["Non-iterable value prange"])

    def test_style_test(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=fLOG, neg_pattern="temp_.*",
                   pylint_ignore=('C0103', 'C1801', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'C0412', 'C0411'),
                   skip=["Redefining built-in 'input'",
                         "Non-iterable value prange",
                         ])


if __name__ == "__main__":
    unittest.main()
