from __future__ import print_function, division
import unittest

trace = True

def merge(one, two):
    '''Merge two already sorted lists and return a single list.'''
    if trace: print("merging:", one, "and:", two)
    if not one: return two
    if not two: return one

    # shallow copy
    first = list(one)
    second = list(two)

    result = []
    while first and second:
        if first[0] < second[0]:
            result.append(first.pop(0))
        else:
            result.append(second.pop(0))

    if not first: result.extend(second)
    if not second: result.extend(first)

    if trace: print("returning:", result)

    return result

def sort(array):
    if trace: print("sorting:", array)
    if not array: return array
    if 1 == len(array): return array

    half = len(array)//2
    return merge(sort(array[:half]), sort(array[half:]))

class TestMerge(unittest.TestCase):
    def test_both_none(self):
        self.assertEquals(merge(None, None), None)
    def test_one_none(self):
        self.assertEquals(merge(None, [1, 2, 3]), [1, 2, 3])
    def test_two_none(self):
        self.assertEquals(merge([1, 2, 3], None), [1, 2, 3])
    def test_one_zero(self):
        self.assertEquals(merge([], [1, 2, 3]), [1, 2, 3])
    def test_two_zero(self):
        self.assertEquals(merge([1, 2, 3], []), [1, 2, 3])
    def test_one_one(self):
        self.assertEquals(merge([1], []), [1])
    def test_two_one(self):
        self.assertEquals(merge([], [1]), [1])
    def test_one_other_one(self):
        self.assertEquals(merge([1], [1]), [1, 1])
    def test_one_two(self):
        self.assertEquals(merge([1], [1, 2]), [1, 1, 2])
    def test_float(self):
        self.assertEquals(merge([1.0], [2, 3]), [1.0, 2, 3])

class TestSort(unittest.TestCase):
    def test_none(self):
        self.assertEquals(sort([]), [])
    def test_one(self):
        self.assertEquals(sort([1]), [1])
    def test_two(self):
        self.assertEquals(sort([2, 1]), [1, 2])
    def test_four(self):
        self.assertEquals(sort([4, 3, 2, 1]), [1, 2, 3, 4])

if '__main__' == __name__:
    trace = True
    # print((merge_sort().sort([[4], [3], [2], [1]])))
    print(sort([[5], [4], [3], [2], [1]]))
    print(sort([5, 4, 3, 2, 1]))
    print(sort(["This", "Is", "A", "Test"]))
