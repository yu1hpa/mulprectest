# coding:utf-8

import unittest
from mulprectest import Mulprectest

class TestMulprectest(unittest.TestCase):
    def test_mulprectest(self):
        # len(pi) = 73
        # correct number of digits = 70
        pi = "3141592653589793238462643383279502884197169399375105820974944592307816396"

        mpt = Mulprectest(100, pi)
        expected = 70
        actual = mpt.mulprectest()
        self.assertEqual(actual, expected)

        pi1 = "3141592653589793238462"

        mpt = Mulprectest(100, pi1)
        expected = 22
        actual = mpt.mulprectest()
        self.assertEqual(actual, expected)

        pi2 = "3.1415926535897932384626433832795028841971693993751058209749445923"
        mpt = Mulprectest(100, pi2)
        expected = 65
        actual = mpt.mulprectest()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
