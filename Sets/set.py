from __future__ import print_function
import unittest
import sys

trace = False

'''A set class implemented by chaining. The set is
represented internally by a list of lists. When
multiple values hash to the same location (a
collision), new values are appended to the list at
that location. The list is rehashed when ~75% full.
The size starts at 10 and doubles with each rehash'''
class my_set:
  def __init__(self, init=None):
    self.__limit = 10
    self.__none = object();
    self.__items = [self.__none] * self.__limit
    self.__count = 0

    if init:
      for i in init:
        self.add(i)

  def __len__(self): return(self.__count)

  def __flattened(self):
    flattened = filter(lambda x: x != self.__none, self.__items)
    flattened = [item for inner in flattened for item in inner]
    return(flattened)

  def __iter__(self): return(iter(self.__flattened()))
  def __str__(self): return(str(self.__flattened()))

  # DRY refactoring
  def __hash(self, item): return(hash(item) % self.__limit)

  # DRY refactoring
  def __add(self, item):
    assert item != self.__none

    if trace: print("__add before:", self.__items)
    h = self.__hash(item)

    if self.__items[h] == self.__none:
      self.__items[h] = [item]
    else:
      self.__items[h].append(item)
    if trace: print("__add after:", self.__items)

  def add(self, item):
    if item in self: return

    self.__add(item)
    self.__count += 1

    if (0.0 + self.__count) / self.__limit > .75: self.__rehash()

  def __rehash(self):
    if trace: print("rehashing before:", self.__items)

    old_items = self.__flattened()

    self.__limit *= 2
    self.__items = [self.__none] * self.__limit

    for i in old_items: self.__add(i)

    if trace: print("rehashing after:", self.__items)

  def __contains__(self, item):
    h = self.__hash(item)
    if self.__items[h] != self.__none:
      for i in self.__items[h]:
        if i == item: return True
    return False

  def remove(self, item):
    if item not in self: raise(KeyError(item))

    h = self.__hash(item)
    self.__items[h].remove(item)

    # not strictly necessary, but for consistency
    if self.__items[h] == []:
      self.__items[h] = self.__none

    self.__count -= 1

  def __ior(self, other):
    for i in other:
      if i not in self:
        self.add(i)
    return(self)

  def __or__(self, other):
    return(self.union(other))

  def union(self, other):
    ret = my_set(self)
    for i in other: ret.add(i)
    return(ret)

  def __iand__(self, other):
    for i in self:
      if i not in other:
        self.remove(i)
    return(self)

  def __and__(self, other):
    return(self.intersection(other))

  def intersection(self, other):
    ret = my_set()
    for i in self:
      for j in other:
        if i == j: ret.add(i)
    return(ret)

  def __isub__(self, other):
    for i in self:
      if i in other:
        self.remove(i)
    return(self)

  def __sub__(self, other):
    return(self.difference(other))

  def difference(self, other):
    ret = my_set(self)
    for i in other:
      if i: ret.remove(i)
    return(ret)

  def __eq__(self, other):
    for i in self:
      if i not in other:
        return(False)
    return(True)

class test_my_set(unittest.TestCase):
  def test_empty(self):
    self.assertEqual(len(my_set()), 0)
  def test_add_one(self):
    s = my_set()
    s.add("one")
    self.assertEquals(len(s), 1)
  def test_add_twice(self):
    s = my_set()
    s.add("one")
    s.add("one")
    self.assertEquals(len(s), 1)
  def test_remove(self):
    s = my_set()
    s.add("one")
    self.assertRaises(KeyError, lambda: s.remove("two"))
    s.remove("one")
    self.assertEquals(len(s), 0)
  def test_one_in(self):
    s = my_set()
    s.add("one")
    self.assertTrue("one" in s)
  def test_none(self):
    s = my_set()
    s.add(None)
    self.assertTrue(None in s)
  def test_collide(self):
    s = my_set()
    s.add(0)
    s.add(10)
    self.assertEquals(len(s), 2)
    self.assertTrue(0 in s)
    self.assertTrue(10 in s)
    self.assertFalse(20 in s)
  def test_rehash(self):
    s = my_set()
    s.add(0), s.add(10), s.add(1), s.add(2), s.add(3), s.add(4)
    s.add(5), s.add(6), s.add(7), s.add(8), s.add(9), s.add(11)
    self.assertEquals(len(s), 12)
    self.assertEquals(str(s), '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]')
    t = my_set(s)
    self.assertEquals(str(t), '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]')
  def test_eq(self):
    s = my_set([1, 3, 5, 7, 9])
    t = my_set([2, 4, 6, 8])
    self.assertTrue(s == s)
    self.assertFalse(s == t)
  def test_union(self):
    s = my_set([1, 3, 5, 7, 9])
    t = my_set([2, 4, 6, 8])
    u = s.union(t)
    e = my_set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    self.assertEquals(u, e)
  def test_or(self):
    s = my_set([1, 3, 5, 7, 9])
    t = my_set([2, 4, 6, 8])
    u = s | t
    self.assertEquals(u, my_set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
  def test_ior(self):
    s = my_set([1, 3, 5, 7, 9])
    t = my_set([2, 4, 6, 8])
    s |= t
    self.assertEquals(s, my_set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
  def test_intersection(self):
    s = my_set([1, 3, 5, 7, 9])
    t = my_set([3, 5, 7])
    u = s.intersection(t)
    self.assertEquals(u, my_set([3, 5, 7]))
  def test_and(self):
    s = my_set([1, 3, 5, 7, 9])
    t = my_set([3, 5, 7])
    u = s & t
    self.assertEquals(u, my_set([3, 5, 7]))
  def test_iand(self):
    s = my_set([1, 3, 5, 7, 9])
    t = my_set([3, 5, 7])
    s &= t
    self.assertEquals(s, my_set([3, 5, 7]))
  def test_difference(self):
    s = my_set([1, 3, 5, 7, 9])
    t = my_set([3, 5, 7])
    u = s.difference(t)
    self.assertEquals(u, my_set([1, 9]))
  def test_sub(self):
    s = my_set([1, 3, 5, 7, 9])
    t = my_set([3, 5, 7])
    u = s - t
    self.assertEquals(u, my_set([1, 9]))
  def test_isub(self):
    s = my_set([1, 3, 5, 7, 9])
    t = my_set([3, 5, 7])
    s -= t
    self.assertEquals(s, my_set([1, 9]))

if "__main__" == __name__:
  s = my_set()
  for line in sys.stdin:
    l = line.strip()
    s.add(l)

  print(s)
