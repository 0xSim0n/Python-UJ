import unittest


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):
        if self.y == 1:
            return str(self.x)
        else:
            return str(self.x) + "/" + str(self.y)

    def __repr__(self):
        return Frac(self.x, self.y)

    def __cmp__(self, other):
        if self.__eq__(other) is True:
            return 0
        elif self.__lt__(other) is True:
            return -1
        else:
            return 1

    def __eq__(self, other):
        if self.__float__() == other.__float__():
            return True
        else:
            return False

    def __ne__(self, other):
        if self.__float__() != other.__float__():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__float__() < other.__float__():
            return True
        else:
            return False

    def __le__(self, other):
        if self.__float__() <= other.__float__():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__float__() > other.__float__():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.__float__() >= other.__float__():
            return True
        else:
            return False

    def __add__(self, other):
        return Frac((self.x * other.y + other.x * self.y), (self.y * other.y))

    def __sub__(self, other):
        return Frac((self.x * other.y - other.x * self.y), (self.y * other.y))

    def __mul__(self, other):
        return Frac((self.x * other.x), (self.y * other.y))

    def __div__(self, other):
        return Frac((self.x * other.y) / (self.y * other.x))

    def __truediv__(self, other):
        return Frac((self.x * other.y) / (self.y * other.x))

    def __floordiv__(self, other):
        return Frac((self.x * other.y) // (self.y * other.x))

    def __mod__(self, other):
        return Frac((self.x * other.y) % (self.y * other.x), self.y * other.y)

    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __float__(self):
        return self.x/self.y

    def __hash__(self):
        return hash(float(self))


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.Frac_1 = Frac(1, 3)
        self.Frac_2 = Frac(1, 2)
        self.Frac_3 = Frac(3, 1)

    def test_str_frac(self):
        self.assertEqual(self.Frac_1.__str__(), "1/3")
        self.assertEqual(self.Frac_3.__str__(), "3")

    def test_repr_frac(self):
        self.assertEqual(self.Frac_2.__repr__(), Frac(1, 2))

    def test_add_frac(self):
        self.assertEqual(self.Frac_1.__add__(self.Frac_2), 5/6)

    def test_sub_frac(self):
        self.assertEqual(self.Frac_1.__sub__(self.Frac_2), -1/6)

    def test_mul_frac(self):
        self.assertEqual(self.Frac_2.__mul__(self.Frac_1), 1/6)

    def test_div_frac(self):
        self.assertEqual((self.Frac_1.__div__(self.Frac_2)), 2/3)
        self.assertEqual(self.Frac_1.__truediv__(self.Frac_2), 2/3)

    def test_floordiv_frac(self):
        self.assertEqual(self.Frac_1.__floordiv__(self.Frac_2), 0)

    def test_mod_frac(self):
        self.assertEqual(self.Frac_1.__mod__(self.Frac_2), 1/3)
        self.assertEqual((self.Frac_3.__mod__(self.Frac_2)), 0)
        self.assertEqual(self.Frac_2.__mod__(self.Frac_3), 1/2)

    def test_cmp_frac(self):
        self.assertEqual(self.Frac_1.__cmp__(self.Frac_2), -1)
        self.assertEqual(self.Frac_1.__cmp__(self.Frac_1), 0)
        self.assertEqual(self.Frac_1.__cmp__(0), 1)

    def test_cmpfunctions_frac(self):
        self.assertTrue(self.Frac_1.__lt__(self.Frac_2))
        self.assertTrue(self.Frac_1.__le__(self.Frac_2))
        self.assertFalse(self.Frac_1.__gt__(self.Frac_2))
        self.assertFalse(self.Frac_1.__eq__(self.Frac_2))
        self.assertTrue(self.Frac_1.__ne__(self.Frac_2))
        self.assertFalse(self.Frac_1.__ge__(self.Frac_2))

    def test_pos_frac(self):
        self.assertEqual(self.Frac_1.__pos__(), 1/3)

    def test_neg_frac(self):
        self.assertEqual(self.Frac_1.__neg__(), -1/3)

    def test_invert_frac(self):
        self.assertEqual(self.Frac_1.__invert__(), 3)

    def test_flot_frac(self):
        self.assertAlmostEqual(self.Frac_1.__float__(), 0.33333, 5)

    def test_hash_frac(self):
        self.assertAlmostEqual(float(3/9), self.Frac_1.__float__(), 5)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
