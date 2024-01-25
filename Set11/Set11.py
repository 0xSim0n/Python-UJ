import unittest

class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def find_max(self):
        if not self.head:
            return None

        max_node = self.head
        current = self.head
        while current:
            if current.key > max_node.key:
                max_node = current
            current = current.next
        return max_node

    def find_min(self):
        if not self.head:
            return None

        min_node = self.head
        current = self.head
        while current:
            if current.key < min_node.key:
                min_node = current
            current = current.next
        return min_node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def clear(self):
        self.head = None
        self.tail = None


class TestDoubleList(unittest.TestCase):

    def setUp(self):
        self.list = DoubleList()

    def test_empty_list_max(self):
        self.assertIsNone(self.list.find_max())

    def test_empty_list_min(self):
        self.assertIsNone(self.list.find_min())

    def test_find_max(self):
        for i in [3, 1, 4, 1, 5]:
            node = Node(i)
            if self.list.tail:
                self.list.tail.next = node
                node.prev = self.list.tail
            else:
                self.list.head = node
            self.list.tail = node

        self.assertEqual(self.list.find_max().key, 5)

    def test_find_min(self):
        for i in [3, 1, 4, 1, 5]:
            node = Node(i)
            if self.list.tail:
                self.list.tail.next = node
                node.prev = self.list.tail
            else:
                self.list.head = node
            self.list.tail = node

        self.assertEqual(self.list.find_min().key, 1)

    def test_remove(self):
        nodes = [Node(i) for i in range(5)]
        for node in nodes:
            if self.list.tail:
                self.list.tail.next = node
                node.prev = self.list.tail
                self.list.tail = node
            else:
                self.list.head = node
                self.list.tail = node

        self.list.remove(nodes[2])

        current = self.list.head
        while current:
            self.assertNotEqual(current.key, 2)
            current = current.next

        self.assertEqual(nodes[1].next, nodes[3])
        self.assertEqual(nodes[3].prev, nodes[1])

    def test_clear(self):
        for i in [3, 1, 4, 1, 5]:
            node = Node(i)
            if self.list.tail:
                self.list.tail.next = node
                node.prev = self.list.tail
            else:
                self.list.head = node
            self.list.tail = node

        self.list.clear()
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)

if __name__ == '__main__':
    unittest.main()