import unittest
import random

def merge(one, two):
    '''Merge two already sorted lists and return a single list.'''
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

    return result

class TestMerge(unittest.TestCase):
    def test_both_none(self):
        self.assertEqual(merge(None, None), None)
    def test_one_none(self):
        self.assertEqual(merge(None, [1, 2, 3]), [1, 2, 3])
    def test_two_none(self):
        self.assertEqual(merge([1, 2, 3], None), [1, 2, 3])
    def test_one_zero(self):
        self.assertEqual(merge([], [1, 2, 3]), [1, 2, 3])
    def test_two_zero(self):
        self.assertEqual(merge([1, 2, 3], []), [1, 2, 3])
    def test_one_one(self):
        self.assertEqual(merge([1], []), [1])
    def test_two_one(self):
        self.assertEqual(merge([], [1]), [1])
    def test_one_another_one(self):
        self.assertEqual(merge([1], [1]), [1, 1])
    def test_one_two(self):
        self.assertEqual(merge([1], [1, 2]), [1, 1, 2])
    def test_float(self):
        self.assertEqual(merge([1.0], [2, 3]), [1.0, 2, 3])

def merge_sort(array):
    '''Do the actual sorting:
        Start with combining every other sublist as each individual element
        is, by definition, sorted. That gives us sorted lists of length
        two. Continue combining into 4, 8, etc. until the entire list is
        sorted.'''
    if not array:
        return array
    if 1 == len(array):
        return array

    # listify a
    result = [[array[i]] for i in range(len(array))]

    while len(result) != 1:
        result.append(merge(result.pop(0), result.pop(0)))

    return result[0]

class TestSort(unittest.TestCase):
    def test_none(self):
        self.assertEqual(merge_sort([]), [])
    def test_one(self):
        self.assertEqual(merge_sort([1]), [1])
    def test_two(self):
        self.assertEqual(merge_sort([2, 1]), [1, 2])
    def test_four(self):
        self.assertEqual(merge_sort([4, 3, 2, 1]), [1, 2, 3, 4])
    def test_99(self):
        a = random.sample(range(99), k=99)
        b = a[:]
        b.sort()
        self.assertEqual(merge_sort(a), b)
    def test_100(self):
        a = random.sample(range(100), k=100)
        b = a[:]
        b.sort()
        self.assertEqual(merge_sort(a), b)

if "__main__" == __name__:
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    print(merge_sort(lines))

