# https://github.com/iiTzFreddy/lab11-FR-JW
# Partner 1: Freddy Rives
# Partner 2: John Watson
import math
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5, 3), 15)
        self.assertEqual(mul(-5, 3), -15)
        self.assertEqual(mul(-5, -3), 15)
        self.assertEqual(mul(0, 10), 0)
        self.assertAlmostEqual(mul(2.5, 4), 10.0)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(3, 10), 3.3333333333333335)
        self.assertEqual(div(-5, 20), -4)
        self.assertAlmostEqual(div(3.0, 10.0), 3.3333333333333335)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # Log base (a) <= 0
        with self.assertRaises(ValueError):
            log(0, 5)
        with self.assertRaises(ValueError):
            log(-2, 5)
        # Log base (a) == 1
        with self.assertRaises(ValueError):
            log(1, 5)
        # Log argument (b) <= 0
        with self.assertRaises(ValueError):
            log(2, 0)
        with self.assertRaises(ValueError):
            log(2, -5)

        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(-3, 4), 5.0)
        self.assertEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(1, 1), math.sqrt(2))

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(9), 3.0)
        self.assertEqual(square_root(0), 0.0)
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)
        # Test ValueError for negative input
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, -2), -1)

    def test_subtract(self):
        self.assertEqual(sub(1, 2), -1)
        self.assertEqual(sub(2, 1), 1)

    def divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(2 / 0)

    def test_logarith(self):
        self.assertEqual(log(3, 9), 2)
        self.assertEqual(log(2, 8), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(8, 1)
        with self.assertRaises(ValueError):
            log(0, 3)
        with self.assertRaises(ValueError):
            log(-1, 3)

    ##########################
#
# Do not touch this
if __name__ == "__main__":
    unittest.main()