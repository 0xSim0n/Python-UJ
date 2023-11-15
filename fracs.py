import unittest


def add_frac(x, y):
    result = [y[1] * x[0] + y[0] * x[1], x[1] * y[1]]
    return result


def sub_frac(x, y):
    result = [y[1] * x[0] - y[0] * x[1], x[1] * y[1]]
    return result


def mul_frac(x, y):
    result = [x[0] * y[0], x[1] * y[1]]
    return result


def div_frac(x, y):
    result = [x[0] * y[1], x[1] * y[0]]
    return result


def is_positive(x):
    if (x[0] >= 0 and x[1] > 0) or (x[0] <= 0 and x[1] < 0):
        return True
    else:
        return False


def is_zero(x):
    if x[0] == 0:
        return True
    else:
        return False


def cmp_frac(x, y):
    def nwd(a, b):
        while b:
            a, b = b, a % b
        return a

    nwd_x = nwd(x[0], x[1])
    nwd_y = nwd(y[0], y[1])

    if((x[0] / nwd_x) == (y[0] / nwd_y)) and ((x[1] / nwd_x) == (y[1] / nwd_y)):
        return 0
    elif (((x[0] / nwd_x) > (y[0] / nwd_y)) and ((x[1] / nwd_x) <= (y[1] / nwd_y)) or
          ((x[0] / nwd_x) >= (y[0] / nwd_y)) and ((x[1] / nwd_x) < (y[1] / nwd_y))):
        return -1
    else:
        return 1


def frac2float(x):
    result = x[0] / x[1]
    return result


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.A = [1, 2]
        self.B = [1, 3]

    def test_add_frac(self):
        self.assertEqual(add_frac(self.A, self.B), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.A, self.B), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac(self.A, self.B), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac(self.A, self.B), [3, 2])

    def test_is_positive(self):
        self.assertTrue(is_positive(self.A))
        self.assertFalse(is_positive([1, -2]))
        self.assertTrue(is_positive([-1, -2]))
        self.assertFalse(is_positive([-1, 2]))

    def test_is_zero(self):
        self.assertFalse(is_zero(self.A))
        self.assertTrue(is_zero(self.zero))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.A, self.B), -1)
        self.assertEqual(cmp_frac(self.B, self.A), 1)
        self.assertEqual(cmp_frac(self.A, self.A), 0)
        self.assertEqual(cmp_frac(self.A, [2, 4]), 0)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float(self.B), 0.33333, places=5)
        self.assertEqual(frac2float(self.zero), 0)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
