import unittest
import random

main = __name__ == "__main__"

class selection_sort:
  def sort(self, a):
    if not a: return a
    if len(a) == 1: return a
    if main: print a

    steps = 0
    b = a
    result = []
    while len(b) != 0:
      min = b[0]
      index = 0
      for i in range(1, len(b)):
        steps += 1
        if b[i] < min:
          min = b[i]
          index = i

      result.append(b[index])
      if main: print "min:", min, "result:", result
      del b[index]

    if main: print "steps:", steps
    if main: print result

    return result

class test_selection_sort (unittest.TestCase):
  def test_none(self):
    self.assertEquals(selection_sort().sort(None), None)
  def test_one(self):
    self.assertEquals(selection_sort().sort([1]), [1])
  def test_two(self):
    self.assertEquals(selection_sort().sort([2, 1]), [1, 2])
  def test_10(self):
    a = range(10)
    random.shuffle(a)
    b = a[:]
    b.sort()  # in place, bleah
    self.assertEquals(selection_sort().sort(a), b)

if main:
    selection_sort().sort([9,4,2,3,6,7,1])
    selection_sort().sort([1,2,3,4,5,6,7])
