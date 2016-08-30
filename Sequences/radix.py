from __future__ import print_function
import unittest
import sys

TRACE = False

class Mystr(str):
    ''' Extend str and overwrite one method so that
    requests for characters beyond the last one
    return a space'''
    def __getitem__(self, num):
        if num > len(self)-1: return " "
        return super(Mystr, self).__getitem__(num)

class TestMystr(unittest.TestCase):
    def setUp(self):
        self.string = Mystr("A")
    def test_empty(self):
        self.assertEquals("", "")
    def test_simple(self):
        self.assertEquals(self.string[0], "A")
    def test_missing(self):
        self.assertEquals(self.string[10], " ")
    def test_longer(self):
        self.assertEquals(self.string[10], " ")

def radix_sort(array, longest):
    for position in range(longest-1, -1, -1):
        buckets = [[] for _ in range(128)]

        for word in array:
            where = ord(word[position])
            buckets[where].append(word)

        array = []
        for bucket in buckets:
            array.extend(bucket)

    return array

class TestRadixSort(unittest.TestCase):
    def test_simple(self):
        self.assertEquals(radix_sort([Mystr("A")], 1), ["A"])
    def test_two(self):
        self.assertEquals(radix_sort([Mystr("A"), Mystr("A")], 1), ["A", "A"])
    def test_different(self):
        self.assertEquals(radix_sort([Mystr("A"), Mystr("B")], 1), ["A", "B"])
    def test_five(self):
        self.assertEquals(radix_sort([Mystr("AA"), Mystr("AB")], 2), \
            ["AA", "AB"])
    def test_six(self):
        self.assertEquals(radix_sort([Mystr("AA"), Mystr("BA")], 2), \
            ["AA", "BA"])
    def test_seven(self):
        self.assertEquals(radix_sort([Mystr("AA"), Mystr("A")], 2), \
            ["A", "AA"])


def run():
    words = []
    longest = 0
    for lines in sys.stdin:
        line = lines.strip()
        words.append(Mystr(line))
        if len(line) > longest: longest = len(line)

    print(words)
    print(radix_sort(words, longest))

if "__main__" == __name__: run()
