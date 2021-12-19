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

        pi_p = "3.141592653589793238462643383279502884197169399375105820974944592307816396"
        mpt = Mulprectest(100, pi_p, False)
        expected = 70
        actual = mpt.mulprectest()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
