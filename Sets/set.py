from __future__ import print_function
import unittest
import sys

trace = False

class set:
    def __init__(self, init=None):
        self.limit = 10
        self.items = [[] for _ in range(self.limit)]
        self.count = 0
        if init:
            for i in init:
                self.add(i)

    def empty(self):
        return count == 0

    def add(self, item):
        if item in self: return
        h = hash(item) % self.limit
        self.items[h].append(item)
        self.count += 1
        print(self.items)

    def remove(self, item):
        if item not in self: return False
        h = hash(item) % self.limit
        self.items[h].remove(item)
        self.count -= 1
        return True

    def __contains__(self, item):
        h = hash(item) % self.limit
        for i in self.items[h]:
            if i == item: return True
        return False

class test_set(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(set().empty)
    def test_add_one(self):
        s = set()
        s.add("one")
        self.assertEquals(s.count, 1)
    def test_add_twice(self):
        s = set()
        s.add("one")
        s.add("one")
        self.assertEquals(s.count, 1)
    def test_remove(self):
        s = set()
        s.add("one")
        self.assertFalse(s.remove("two"))
        self.assertTrue(s.remove("one"))
        self.assertEquals(s.count, 0)
    def test_one_in(self):
        s = set()
        s.add("one")
        self.assertTrue("one" in s)
    def test_collide(self):
        s = set()
        s.add(0)
        s.add(10)
        self.assertEquals(s.count, 2)
        print(0 in s)
        print(10 in s)
    '''
    def test_missing(self):
        a = mystr("A")
        self.assertEquals(a[10], " ")
    def test_longer(self):
        a = mystr("A")
        self.assertEquals(a[10], " ")
    '''

if "__main__" == __name__:
    words = []
    longest = 0
    for line in sys.stdin:
        l = line.strip()
        words.append(mystr(l))
        if len(l) > longest: longest = len(l)

    print(words)
    print(radix_sort(words, longest))
