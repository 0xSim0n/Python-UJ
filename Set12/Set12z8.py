import random
import unittest


class RandomQueue:

    def __init__(self, size=10):
        self.data = []
        self.size = size

    def insert(self, item):
        if self.is_full():
            raise OverflowError()
        self.data.append(item)

    def remove(self):
        if self.is_empty():
            raise IndexError()
        index = random.randint(0, len(self.data) - 1)
        self.data[index], self.data[-1] = self.data[-1], self.data[index]
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0

    def is_full(self):
        return len(self.data) == self.size

    def clear(self):
        self.data = []


class TestRandomQueue(unittest.TestCase):

    def test_insert_and_remove(self):
        queue = RandomQueue(size=5)
        elements = [1, 2, 3, 4, 5]
        for el in elements:
            queue.insert(el)
        removed_elements = [queue.remove() for _ in range(5)]
        self.assertEqual(sorted(removed_elements), elements)

    def test_is_empty(self):
        queue = RandomQueue()
        self.assertTrue(queue.is_empty())
        queue.insert(1)
        self.assertFalse(queue.is_empty())

    def test_is_full(self):
        queue = RandomQueue(size=2)
        self.assertFalse(queue.is_full())
        queue.insert(1)
        queue.insert(2)
        self.assertTrue(queue.is_full())

    def test_overflow(self):
        queue = RandomQueue(size=1)
        queue.insert(1)
        with self.assertRaises(OverflowError):
            queue.insert(2)

    def test_remove_from_empty(self):
        queue = RandomQueue()
        with self.assertRaises(IndexError):
            queue.remove()

    def test_clear(self):
        queue = RandomQueue()
        for el in [1, 2, 3]:
            queue.insert(el)
        queue.clear()
        self.assertTrue(queue.is_empty())

if __name__ == "__main__":
    unittest.main()
