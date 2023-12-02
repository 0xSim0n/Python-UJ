import random
import unittest


class ZeroOneIterator:
    def __init__(self):
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.value
        self.value = 1 - self.value
        return result


class RandomIterator:
    def __init__(self):
        self.list = ["N", "W", "S", "E"]

    def __iter__(self):
        return self

    def __next__(self):
        random_element = random.choice(self.list)
        return random_element


class DaysIterator:
    def __init__(self):
        self.value = 6

    def __iter__(self):
        return self

    def __next__(self):
        while self.value > -1:
            result = 6 - self.value
            self.value -= 1
            return result
        else:
            self.value = 5
            return 0


class TestIterators(unittest.TestCase):

    def setUp(self):
        self.first_iterator = ZeroOneIterator()
        self.second_iterator = RandomIterator()
        self.third_iterator = DaysIterator()

    def test_ZeroOneIterator(self):
        expected_values = [0, 1, 0, 1, 0, 1, 0, 1]
        actual_values = [next(self.first_iterator) for _ in range(len(expected_values))]
        self.assertEqual(actual_values, expected_values)

    def test_RandomIterator(self):
        expected_values = ["N", "W", "S", "E"]
        actual_values = [next(self.second_iterator) for _ in range(len(expected_values))]

        for value in actual_values:
            self.assertIn(value, expected_values)

    def test_DaysIterator(self):
        expected_values = [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0]
        actual_values = [next(self.third_iterator) for _ in range(len(expected_values))]
        self.assertEqual(actual_values, expected_values)


if __name__ == '__main__':
    unittest.main()
