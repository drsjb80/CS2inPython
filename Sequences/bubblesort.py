''' An implementation of the classis bubble sort. '''
from __future__ import print_function
import unittest
import random

TRACE = True

def bubble_sort(array):
    ''' A bubble sort with the usual early exit. '''
    if not array: return array
    if 1 == len(array): return array

    result = list(array)
    steps = 0

    if TRACE: print("start:", result)

    # we compare i and i+1 so we only go to the penultimate
    for i in range(len(result)-1):
        swapped = False
        for j in range(len(result)-1-i):
            steps += 1
            if result[j] > result[j+1]:
                if TRACE: print("moving", result[j], "up one")
                result[j], result[j+1] = result[j+1], result[j]
                swapped = True

            if TRACE: print("    now:", result)

        if not swapped: break

    if TRACE: print ("done in", steps, "steps")
    return result

class TestBubbleSort(unittest.TestCase):
    ''' Unit tests for bubble sort. '''
    def test_none(self):
        ''' Make sure a sort on None doesn't blow up. '''
        self.assertEquals(bubble_sort(None), None)
    def test_one(self):
        ''' An easy one-element sort. '''
        self.assertEquals(bubble_sort([1]), [1])
    def test_two(self):
        ''' An easy two-element sort. '''
        self.assertEquals(bubble_sort([2, 1]), [1, 2])
    def test_10(self):
        ''' Make sure this sort agrees with the builtin sort. '''
        a = range(10)
        random.shuffle(a)
        b = a[:]
        b.sort()    # in place, bleah
        self.assertEquals(bubble_sort(a), b)

if '__main__' == __name__:
    print(bubble_sort([9, 4, 2, 3, 6, 7, 1]))
    print(bubble_sort([1, 2, 3, 4, 5, 6, 7]))
