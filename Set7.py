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

    def SetUp(self):
        self.n = 10
        self.first_iterator = ZeroOneIterator
        self.second_iterator = RandomIterator
        self.third_iterator = DaysIterator

    def TestZeroOneIterator(self):
        for _ in range(self.n): self.first_iterator.__next__()
