from __future__ import print_function, division
import unittest

trace =  False

def binary_search(value, list):
  if not list: return False
  if 1 == len(list): return value == list[0]

  if trace: print("looking at:", list)

  middle = len(list)//2
  val = list[middle]
  if trace: print("middle:", middle, "val:", val)
  
  if val == value:
    return True
  elif value < val:
    return binary_search(value, list[:middle])
  else:
    return binary_search(value, list[middle+1:])

class test_binary_search(unittest.TestCase):
  def test_none(self):
    self.assertFalse(binary_search(None, None))
  def test_one(self):
    self.assertTrue(binary_search(1, [1]))
  def test_many(self):
    self.assertTrue(binary_search(5, [1, 3, 5, 7, 9]))
  def test_missing(self):
    self.assertFalse(binary_search(4, [1, 3, 5, 7, 9]))
  def test_string(self):
    self.assertTrue(binary_search('a', 'abcdefg'))

if "__main__" == __name__:
  trace = True
  a = list(range(1,40,2))   # python 3
  print(a)
  print(binary_search(4, a))
  print(binary_search(39, a))
