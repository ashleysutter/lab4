import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_add(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(10)
        t_list.add(4)
        t_list.add(4)
        self.assertEqual(t_list.python_list(), [1, 4, 10])
        self.assertEqual(t_list.python_list_reversed(), [10, 4, 1])
        self.assertTrue(t_list.remove(10))
        self.assertEqual(t_list.python_list(), [1, 4])
        self.assertFalse(t_list.remove(99))
        self.assertEqual(t_list.index(4), 1)
        self.assertEqual(t_list.index(-5), None)

    def test_error(self):
        t_list = OrderedList()
        try:
            t_list.pop(-4)
        except IndexError:
            pass
        t_list.add(1)
        t_list.add(5)
        t_list.add(6)
        t_list.add(7)
        t_list.add(4)
        self.assertEqual(t_list.pop(4),7)
        try:
            t_list.pop(5)
        except IndexError:
            pass
        self.assertEqual(t_list.search(11), False)
        self.assertEqual(t_list.search(5), True)



         

if __name__ == '__main__': 
    unittest.main()
