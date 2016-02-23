from __future__ import print_function
import unittest
import sys

trace = False

''' Extend str and overwrite one method so that
requests for characters beyond the last one
return a space'''
class mystr(str):
    def __getitem__(self, num):
        if num > len(self)-1: return " "
        return super(mystr, self).__getitem__(num)

class test_mystr(unittest.TestCase):
    def test_empty(self):
        self.assertEquals("", "")
    def test_simple(self):
        a = mystr("A")
        self.assertEquals(a[0], "A")
    def test_missing(self):
        a = mystr("A")
        self.assertEquals(a[10], " ")
    def test_longer(self):
        a = mystr("A")
        self.assertEquals(a[10], " ")

def radix_sort(list, longest):
    for position in range(longest-1, -1, -1):
        buckets = [[] for _ in range(128)]

        for word in list:
            where = ord(word[position])
            buckets[where].append(word)

        list = []
        for bucket in buckets:
            list.extend(bucket)

    return list

class test_radix_sort(unittest.TestCase):
    def test_simple(self):
        self.assertEquals(radix_sort([mystr("A")], 1), ["A"])
    def test_two(self):
        self.assertEquals(radix_sort([mystr("A"), mystr("A")], 1), ["A", "A"])
    def test_different(self):
        self.assertEquals(radix_sort([mystr("A"), mystr("B")], 1), ["A", "B"])
    def test_five(self):
        self.assertEquals(radix_sort([mystr("AA"), mystr("AB")], 2), \
            ["AA", "AB"])
    def test_six(self):
        self.assertEquals(radix_sort([mystr("AA"), mystr("BA")], 2), \
            ["AA", "BA"])
    def test_seven(self):
        self.assertEquals(radix_sort([mystr("AA"), mystr("A")], 2), \
            ["A", "AA"])

if "__main__" == __name__:
    words = []
    longest = 0
    for line in sys.stdin:
        l = line.strip()
        words.append(mystr(l))
        if len(l) > longest: longest = len(l)

    print(words)
    print(radix_sort(words, longest))
