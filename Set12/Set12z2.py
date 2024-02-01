class StackOverflowError(Exception):
    pass

class StackUnderflowError(Exception):
    pass

class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def push(self, item):
        if len(self.stack) >= self.limit:
            raise StackOverflowError("Stack overflow")
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise StackUnderflowError("Stack underflow")
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            raise StackUnderflowError("Stack underflow")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

import unittest

class TestStack(unittest.TestCase):
    def test_push_pop(self):
        s = Stack(limit=3)
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_underflow(self):
        s = Stack()
        with self.assertRaises(StackUnderflowError):
            s.pop()

    def test_overflow(self):
        s = Stack(limit=2)
        s.push(1)
        s.push(2)
        with self.assertRaises(StackOverflowError):
            s.push(3)

    def test_peek(self):
        s = Stack()
        s.push('top')
        self.assertEqual(s.peek(), 'top')
        s.pop()
        with self.assertRaises(StackUnderflowError):
            s.peek()

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(1)
        self.assertFalse(s.is_empty())

if __name__ == "__main__":
    unittest.main()
