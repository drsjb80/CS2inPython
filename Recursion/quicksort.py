import unittest
import random

TRACE = False

def quick_sort(thelist):
    if TRACE:
        print('input: ', thelist)
    if not thelist:
        return thelist
    if 1 == len(thelist):
        return thelist

    pivot = thelist.pop()

    lt, ge = [], []
    for i in thelist:
        if i < pivot:
            lt.append(i)
        else:
            ge.append(i)

    if TRACE: print('lt:', lt)
    if TRACE: print('pivot:', pivot)
    if TRACE: print('ge:', ge)

    return quick_sort(lt) + [pivot] + quick_sort(ge)

class TestQuickSort(unittest.TestCase):
    def test_both_none(self):
        self.assertEqual(quick_sort(None), None)
    def test_already_done(self):
        self.assertEqual(quick_sort([1, 2, 3]), [1, 2, 3])
    def test_no_movement(self):
        self.assertEqual(quick_sort([1, 7, 3, 9]), [1, 3, 7, 9])
    def test_move_one(self):
        # pivot in middle
        self.assertEqual(quick_sort([1, 9, 3, 7]), [1, 3, 7, 9])
    def test_reverse(self):
        # pivot at beginning
        self.assertEqual(quick_sort([4, 3, 2, 1]), [1, 2, 3, 4])
    def test_twenty(self):
        a = list(range(20))
        b = list(a)
        random.shuffle(a)
        self.assertEqual(quick_sort(a), b)

if "__main__" == __name__:
    unittest.main()
