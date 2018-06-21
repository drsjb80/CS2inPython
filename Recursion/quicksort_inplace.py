from __future__ import print_function
import unittest
import random

trace = False

def partition(thelist, low, high):
    # Due to C.A.R. Hoare
    if trace:
        print("partition from", low, "to", high)
    if trace:
        print(thelist)

    pivot = thelist[low]
    i = low
    j = high
    while True:
        while thelist[i] < pivot:
            if trace:
                print(thelist[i], "<", pivot)
            i += 1

        while thelist[j] > pivot:
            if trace:
                print(thelist[j], ">", pivot)
            j -= 1

        if i >= j:
            if trace:
                print("partition done")
            if trace:
                print(thelist)
            return j

        if trace:
            print("swapping", thelist[i], "and", thelist[j])

        thelist[i], thelist[j] = thelist[j], thelist[i]

        if trace:
            print(thelist)

def quick_sort_recurse(thelist, low, high):
    if low < high:
        part = partition(thelist, low, high)
        quick_sort_recurse(thelist, low, part)
        quick_sort_recurse(thelist, part + 1, high)

def quick_sort(thelist):
    if not thelist:
        return thelist

    quick_sort_recurse(thelist, 0, len(thelist)-1)

class TestQuickSort(unittest.TestCase):
    def test_both_none(self):
        self.assertEqual(quick_sort(None), None)
    def test_already_done(self):
        thelist = [1, 2, 3]
        quick_sort(thelist)
        self.assertEqual(thelist, [1, 2, 3])
    def test_no_movement(self):
        # pivot at end
        thelist = [1, 7, 3, 9]
        quick_sort(thelist)
        self.assertEqual(thelist, [1, 3, 7, 9])
    def test_move_one(self):
        # pivot in middle
        thelist = [1, 9, 3, 7]
        quick_sort(thelist)
        self.assertEqual(thelist, [1, 3, 7, 9])
    def test_reverse(self):
        # pivot at beginning
        thelist = [4, 3, 2, 1]
        quick_sort(thelist)
        self.assertEqual(thelist, [1, 2, 3, 4])
    def test_more(self):
        sorted = range(20)
        tosort = sorted[:]
        random.shuffle(tosort)
        quick_sort(tosort)
        self.assertEqual(tosort, sorted)

if "__main__" == __name__:
    unittest.main()
