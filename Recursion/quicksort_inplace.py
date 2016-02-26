from __future__ import print_function
import unittest
import random

trace = True

def partition(A, lo, hi):
  '''Due to C.A.R. Hoare'''
  if trace: print("partition from", lo, "to", hi)
  if trace: print(A)
  pivot = A[lo]
  i = lo
  j = hi
  while True:
    while A[i] < pivot:
      if trace: print(A[i], "<", pivot)
      i += 1

    while A[j] > pivot:
      if trace: print(A[j], ">", pivot)
      j -= 1

    if i >= j:
      if trace: print("partition done")
      if trace: print(A)
      return j

    if trace: print("swapping", A[i], "and", A[j])
    A[i], A[j] = A[j], A[i]
    if trace: print(A)

def quick_sort_recurse(A, lo, hi):
  if lo < hi:
    p = partition(A, lo, hi)
    quick_sort_recurse(A, lo, p)
    quick_sort_recurse(A, p + 1, hi)

def quick_sort(A):
  quick_sort_recurse(A, 0, len(A)-1)

class test_quick_sort (unittest.TestCase):
  def test_both_none(self):
    self.assertEquals(quick_sort(None), None)
  def test_already_done(self):
    a = [1, 2, 3]
    quick_sort(a)
    self.assertEquals(a, [1, 2, 3])
  def test_no_movement(self):
    # pivot at end
    a = [1, 7, 3, 9]
    quick_sort(a)
    self.assertEquals(a, [1, 3, 7, 9])
  def test_move_one(self):
    # pivot in middle
    a = [1, 9, 3, 7]
    quick_sort(a)
    self.assertEquals(a, [1, 3, 7, 9])
  def test_reverse(self):
    # pivot at beginning
    a = [4, 3, 2, 1]
    quick_sort(a)
    self.assertEquals(a, [1, 2, 3, 4])

if "__main__" == __name__:
  a = range(20)
  random.shuffle(a)
  print(a)
  quick_sort(a)
  print(a)
