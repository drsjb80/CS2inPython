from __future__ import print_function, division
import unittest

_trace = False

def binary_search(value, in_list):
    if not in_list: return False
    if not value: return False
    if 1 == len(in_list): return value == in_list[0]

    if _trace: print("looking at:", in_list)

    middle = len(in_list)//2
    val = in_list[middle]

    if _trace: print("middle:", middle, "val:", val)

    if val == value:
        return True
    elif value < val:
        return binary_search(value, in_list[:middle])
    else:
        return binary_search(value, in_list[middle+1:])

class TestBinarySearch(unittest.TestCase):
    def test_both_none(self):
        self.assertFalse(binary_search(None, None))
    def test_value_none(self):
        self.assertFalse(binary_search(None, [1, 2, 3]))
    def test_list_none(self):
        self.assertFalse(binary_search(1, None))
    def test_empty_list(self):
        self.assertFalse(binary_search(1, []))
    def test_one(self):
        self.assertTrue(binary_search(1, [1]))
    def test_many(self):
        self.assertTrue(binary_search(5, [1, 3, 5, 7, 9]))
    def test_missing(self):
        self.assertFalse(binary_search(4, [1, 3, 5, 7, 9]))
    def test_string(self):
        self.assertTrue(binary_search('a', 'abcdefg'))

if "__main__" == __name__:
    _trace = True
    test_list = list(range(1, 40, 2))     # python 3
    print(test_list)
    print(binary_search(4, test_list))
    print(binary_search(39, test_list))
