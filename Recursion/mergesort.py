from __future__ import print_function, division
import unittest

trace = False

class merge_sort:
  '''This class implements the classic merge sort.'''

  def merge(self, one, two):
    '''Merge two already sorted lists and return a single list.'''
    if trace: print("merging:", one, "and:", two)
    if not one: return two
    if not two: return one

    # shallow copy
    a = list(one)
    b = list(two)

    result = []
    while a and b:
      if a[0] < b[0]:
        result.append(a.pop(0))
      else:
        result.append(b.pop(0))

    if not a: result.extend(b)
    if not b: result.extend(a)

    if trace: print("returning:", result)

    return result

  def sort(self, a):
    if trace: print("sorting:", a)
    if not a: return a
    if 1 == len(a): return a

    half = len(a)//2
    return self.merge(self.sort(a[:half]), self.sort(a[half:]))

class test_merge (unittest.TestCase):
  def setUp(self): self.m = merge_sort()
  def test_both_none(self):
    self.assertEquals(self.m.merge(None, None), None)
  def test_one_none(self):
    self.assertEquals(self.m.merge(None, [1, 2, 3]), [1, 2, 3])
  def test_two_none(self):
    self.assertEquals(self.m.merge([1, 2, 3], None), [1, 2, 3])
  def test_one_zero(self):
    self.assertEquals(self.m.merge([], [1, 2, 3]), [1, 2, 3])
  def test_two_zero(self):
    self.assertEquals(self.m.merge([1, 2, 3], []), [1, 2, 3])
  def test_one_one(self):
    self.assertEquals(self.m.merge([1], []), [1])
  def test_two_one(self):
    self.assertEquals(self.m.merge([], [1]), [1])
  def test_one_one(self):
    self.assertEquals(self.m.merge([1], [1]), [1, 1])
  def test_one_two(self):
    self.assertEquals(self.m.merge([1], [1, 2]), [1, 1, 2])
  def test_float(self):
    self.assertEquals(self.m.merge([1.0], [2, 3]), [1.0, 2, 3])

class test_sort (unittest.TestCase):
  def test_none(self):
    self.assertEquals(merge_sort().sort([]), [])
  def test_one(self):
    self.assertEquals(merge_sort().sort([1]), [1])
  def test_two(self):
    self.assertEquals(merge_sort().sort([2, 1]), [1, 2])
  def test_four(self):
    self.assertEquals(merge_sort().sort([4, 3, 2, 1]), [1, 2, 3, 4])

if '__main__' == __name__:
  trace = True
  print((merge_sort().sort([[4], [3], [2], [1]])))
  print((merge_sort().sort([[5], [4], [3], [2], [1]])))
