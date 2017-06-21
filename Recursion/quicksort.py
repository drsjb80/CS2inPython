from __future__ import print_function
import unittest
import random

TRACE = False

def quick_sort(thelist):
    if TRACE: print('input: ', thelist)
    if not thelist: return thelist
    if 1 == len(thelist): return thelist

    pivot = thelist[len(thelist)-1]

    lt = []
    ge = []
    for i in range(len(thelist)-1):
        if thelist[i] < pivot:
            lt.append(thelist[i])
        else:
            ge.append(thelist[i])

    if TRACE: print('lt:', lt)
    if TRACE: print('pivot:', pivot)
    if TRACE: print('ge:', ge)
    result = []
    if lt: result += quick_sort(lt)
    result.append(pivot)
    if ge: result += quick_sort(ge)

    return result

class TestQuickSort(unittest.TestCase):
    def test_both_none(self):
        self.assertEquals(quick_sort(None), None)
    def test_already_done(self):
        self.assertEquals(quick_sort([1, 2, 3]), [1, 2, 3])
    def test_no_movement(self):
        # pivot at end
        self.assertEquals(quick_sort([1, 7, 3, 9]), [1, 3, 7, 9])
    def test_move_one(self):
        # pivot in middle
        self.assertEquals(quick_sort([1, 9, 3, 7]), [1, 3, 7, 9])
    def test_reverse(self):
        # pivot at beginning
        self.assertEquals(quick_sort([4, 3, 2, 1]), [1, 2, 3, 4])

if "__main__" == __name__:
    TRACE = True
    a = list(range(20))
    random.shuffle(a)
    print((quick_sort(a)))
