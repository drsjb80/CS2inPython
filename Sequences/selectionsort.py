from __future__ import print_function
import unittest
import random

TRACE = True

def selection_sort(array):
    if not array: return array
    if 1 == len(array): return array
    if TRACE: print (array)

    copy = list(array)
    result = []
    while copy:
        minimum = copy[0]
        index = 0
        for i in range(1, len(copy)):
            if copy[i] < minimum:
                minimum = copy[i]
                index = i

        result.append(copy[index])
        del copy[index]
        if TRACE: print ("minimum:", minimum, "result:", result)

    if TRACE: print (result)

    return result

class TestSelectionSort(unittest.TestCase):
    def test_none(self):
        self.assertEquals(selection_sort(None), None)
    def test_one(self):
        self.assertEquals(selection_sort([1]), [1])
    def test_two(self):
        self.assertEquals(selection_sort([2, 1]), [1, 2])
    def test_10(self):
        array = range(10)
        random.shuffle(array)
        copy = array[:]
        copy.sort()    # in place, bleah
        self.assertEquals(selection_sort(array), copy)

if "__main__" == __name__:
    selection_sort([9, 4, 2, 3, 6, 7, 1])
    selection_sort([1, 2, 3, 4, 5, 6, 7])
