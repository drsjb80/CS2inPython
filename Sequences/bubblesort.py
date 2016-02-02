import unittest
import random

main = '__main__' == __name__

class bubble_sort:
  """This class implements the classic bubble sort."""
  def sort(self, a):
    """Sort the list."""
    if not a: return a
    if 1 == len(a): return a

    result = list(a)
    steps = 0

    if main: print ("start:", result)

    for i in range(len(result)-1):
      swapped = False
      for j in range (len(result)-1-i):
        steps += 1
        if result[j] > result[j+1]:
          if main: print ("moving", result[j], "up one")
          result[j], result[j+1] = result[j+1], result[j]
          swapped = True
          if main: print ("  now:", result)

      if not swapped: break

    if main: print ("done in", steps, "steps")
    return result

class test_bubble_sort (unittest.TestCase):
  def test_none(self):
    self.assertEquals(bubble_sort().sort(None), None)
  def test_one(self):
    self.assertEquals(bubble_sort().sort([1]), [1])
  def test_two(self):
    self.assertEquals(bubble_sort().sort([2, 1]), [1, 2])
  def test_10(self):
    a = range(10)
    random.shuffle(a)
    b = a[:]
    b.sort()  # in place, bleah
    self.assertEquals(bubble_sort().sort(a), b)

if main:
    print (bubble_sort().sort([9,4,2,3,6,7,1]))
    print (bubble_sort().sort([1,2,3,4,5,6,7]))
