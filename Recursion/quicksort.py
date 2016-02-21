from __future__ import print_function
import unittest
import random

trace =  False

def quick_sort(list):
  if trace: print(list)
  if not list: return list
  if 1 == len(list): return list

  pivot = list[len(list)-1]

  gt = []
  lt = []
  for i in range(len(list)-1):
    if list[i] < pivot:
      lt.append(list[i])
    else:
      gt.append(list[i])

  result = []
  if lt: result += quick_sort(lt)
  result.append(pivot)
  if gt: result += quick_sort(gt)

  return result

class test_quick_sort (unittest.TestCase):
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
  trace = True
  a = list(range(20))
  random.shuffle(a)
  print((quick_sort(a)))
