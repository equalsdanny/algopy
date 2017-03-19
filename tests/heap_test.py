import unittest
from heap import Heap

class HeapTest(unittest.TestCase):
    def test_create_empty(self):
        h = Heap([])
        self.assertEqual(len(h), 0)

    def test_add_then_extract(self):
        h = Heap([])
        h.add(1)
        h.add(2)
        h.add(3)
        self.assertEqual(h.extract(), 3)
        self.assertEqual(h.extract(), 2)
        self.assertEqual(h.extract(), 1)

if __name__ == '__main__':
    unittest.main()