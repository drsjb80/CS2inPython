from __future__ import print_function
import unittest
import sys

TRACE = False

'''A set class implemented by chaining. The set is
represented internally by a list of lists. When
multiple values hash to the same location (a
collision), new values are appended to the list at
that location. The list is rehashed when ~75% full.
The size starts at 10 and doubles with each rehash'''
class Set(object):
    def __init__(self, init=None):
        self.__limit = 10
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0

        if init:
            for i in init:
                self.add(i)

    def __len__(self): return self.__count

    def __flattened(self):
        return [item for inner in self.__items for item in inner]

    def __iter__(self): return iter(self.__flattened())
    def __str__(self): return str(self.__flattened())

    # DRY refactoring
    def _hash(self, item): return hash(item) % self.__limit

    # DRY refactoring
    def _add(self, item):
        self.__items[self._hash(item)].append(item)

    def add(self, item):
        if item in self: return

        self._add(item)
        self.__count += 1

        if (0.0 + self.__count) / self.__limit > .75: self.__rehash()

    def __rehash(self):
        old_items = self.__flattened()

        self.__limit *= 2
        self.__items = [[] for _ in range(self.__limit)]

        for i in old_items:
            self._add(i)

    def __contains__(self, item):
        hash1 = self._hash(item)
        for i in self.__items[hash1]:
            if i == item: return True
        return False

    def remove(self, item):
        if item not in self: raise KeyError(item)

        hash1 = self._hash(item)
        self.__items[hash1].remove(item)

        self.__count -= 1

    def __ior__(self, other):
        for i in other:
            self.add(i)
        return self

    def __or__(self, other):
        return self.union(other)

    def union(self, other):
        ret = Set(self)
        for i in other:
            ret.add(i)
        return ret

    def __iand__(self, other):
        for i in self:
            if i not in other:
                self.remove(i)
        return self

    def __and__(self, other):
        return self.intersection(other)

    def intersection(self, other):
        ret = Set()
        for i in self:
            for j in other:
                if i == j: ret.add(i)
        return ret

    def __isub__(self, other):
        for i in self:
            if i in other:
                self.remove(i)
        return self

    def __sub__(self, other):
        return self.difference(other)

    def difference(self, other):
        ret = Set(self)
        for i in other:
            ret.remove(i)
        return ret

    def __eq__(self, other):
        if len(self) != len(other): return False

        for i in self:
            if i not in other:
                return False
        return True

class TestSet(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(len(Set()), 0)
    def test_add_one(self):
        set1 = Set()
        set1.add("one")
        self.assertEquals(len(set1), 1)
    def test_add_twice(self):
        set1 = Set()
        set1.add("one")
        set1.add("one")
        self.assertEquals(len(set1), 1)
    def test_remove(self):
        set1 = Set()
        set1.add("one")
        self.assertRaises(KeyError, lambda: set1.remove("two"))
        set1.remove("one")
        self.assertEquals(len(set1), 0)
    def test_one_in(self):
        set1 = Set()
        set1.add("one")
        self.assertTrue("one" in set1)
    def test_none(self):
        set1 = Set()
        set1.add(None)
        self.assertTrue(None in set1)
    def test_collide(self):
        set1 = Set()
        set1.add(0)
        set1.add(10)
        self.assertEquals(len(set1), 2)
        self.assertTrue(0 in set1)
        self.assertTrue(10 in set1)
        self.assertFalse(20 in set1)
    def test_rehash(self):
        set1 = Set()
        set1.add(0); set1.add(10); set1.add(1); set1.add(2); set1.add(3)
        set1.add(4); set1.add(5); set1.add(6); set1.add(7); set1.add(8)
        set1.add(9); set1.add(11)
        self.assertEquals(len(set1), 12)
        self.assertEquals(str(set1), '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]')
        set2 = Set(set1)
        self.assertEquals(str(set2), '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]')
    def test_eq(self):
        set1 = Set([1, 3, 5, 7, 9])
        set2 = Set([2, 4, 6, 8])
        self.assertTrue(set1 == set1)
        self.assertFalse(set1 == set2)
        set3 = Set([1, 3, 5, 7, 9, 11])
        self.assertFalse(set1 == set3)
    def test_union(self):
        set1 = Set([1, 3, 5, 7, 9])
        set2 = Set([2, 4, 6, 8])
        set3 = set1.union(set2)
        set4 = Set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEquals(set3, set4)
    def test_or(self):
        set1 = Set([1, 3, 5, 7, 9])
        set2 = Set([2, 4, 6, 8])
        set3 = set1 | set2
        self.assertEquals(set3, Set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    def test_ior(self):
        set1 = Set([1, 3, 5, 7, 9])
        set2 = Set([2, 4, 6, 8])
        set1 |= set2
        self.assertEquals(set1, Set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    def test_intersection(self):
        set1 = Set([1, 3, 5, 7, 9])
        set2 = Set([3, 5, 7])
        set3 = set1.intersection(set2)
        self.assertEquals(set3, Set([3, 5, 7]))
    def test_and(self):
        set1 = Set([1, 3, 5, 7, 9])
        set2 = Set([3, 5, 7])
        set3 = set1 & set2
        self.assertEquals(set3, Set([3, 5, 7]))
    def test_iand(self):
        set1 = Set([1, 3, 5, 7, 9])
        set2 = Set([3, 5, 7])
        set1 &= set2
        self.assertEquals(set1, Set([3, 5, 7]))
    def test_difference(self):
        set1 = Set([1, 3, 5, 7, 9])
        set2 = Set([3, 5, 7])
        set3 = set1.difference(set2)
        self.assertEquals(set3, Set([1, 9]))
    def test_sub(self):
        set1 = Set([1, 3, 5, 7, 9])
        set2 = Set([3, 5, 7])
        set3 = set1 - set2
        self.assertEquals(set3, Set([1, 9]))
    def test_isub(self):
        set1 = Set([1, 3, 5, 7, 9])
        set2 = Set([3, 5, 7])
        set1 -= set2
        self.assertEquals(set1, Set([1, 9]))

if "__main__" == __name__:
    total = Set()   # pylint: disable=C0103
    for line in sys.stdin:
        l = line.strip()
        total.add(l)

    print(total)
