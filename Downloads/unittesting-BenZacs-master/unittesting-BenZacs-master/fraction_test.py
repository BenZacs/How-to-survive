import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_init(self):
        f = Fraction(3)
        self.assertEqual(1, f.denominator)
        f = Fraction(1, -2)
        self.assertEqual(-1, f.numerator)
        f = Fraction(-5, -6)
        self.assertEqual(5, f.numerator)
        f = Fraction(0, 7)
        self.assertEqual(0, f.numerator)
        f = Fraction(2, 5)
        self.assertEqual(5, f.denominator)
        f = Fraction(5, -7)
        self.assertEqual(7, f.denominator)

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

    # TODO Write tests for __init__, __eq__, +, *.
    # Here is an example, but you must add more test cases.  
    # The test requires that your __eq__ is correct.
    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        # 5/6 = 1/2 + 8/24
        self.assertEqual(Fraction(5, 6), Fraction(1, 2) + Fraction(8, 24))
        # 1 = 1/2 + -40/-80
        self.assertEqual(Fraction(1), Fraction(1, 2) + Fraction(-40, -80))

    def test_sub(self):
        # 1/2 = 3/4 - 2/8
        self.assertEqual(Fraction(1, 2), Fraction(3, 4) - Fraction(2, 8))
        # 5/8 = 12/16 - 4/32
        self.assertEqual(Fraction(5, 8), Fraction(12, 16) - Fraction(4, 32))
        # -91/144 = 5/16 - 17/18
        self.assertEqual(Fraction(-91, 144), Fraction(5, 16) - Fraction(17, 18))

    def test_mul(self):
        # 1/4 = 1/2 * 1/2
        self.assertEqual(Fraction(1, 4), Fraction(1, 2) * Fraction(1, 2))
        # 5/24 = 5/8 * 1/3
        self.assertEqual(Fraction(5, 24), Fraction(5, 8) * Fraction(1, 3))
        # 36/37 = -1 * -36/37
        self.assertEqual(Fraction(36, 37), Fraction(-1) * Fraction(-36, 37))

    def test_gt(self):
        a = Fraction(1, 2)
        b = Fraction(5, 6)
        c = Fraction(1, 9)
        self.assertFalse(a.__gt__(b))
        self.assertFalse(c.__gt__(b))
        self.assertTrue(a.__gt__(c))
        self.assertTrue(b.__gt__(a))

    def test_neg(self):
        self.assertEqual("-1", Fraction(1,1).__neg__())
        self.assertEqual("-3/5", Fraction(9, 15).__neg__())
        self.assertEqual("0", Fraction(0).__neg__())
        self.assertEqual("2/3",Fraction(-2, 3).__neg__())

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)  # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        # Consider special values like 0, 1/0, -1/0
        i = Fraction(0)
        self.assertFalse(i.__eq__(f))
        j = Fraction(1, 0)  # ZeroDivisionError: division by zero
        self.assertFalse(j.__eq__(i))
