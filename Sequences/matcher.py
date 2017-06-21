from __future__ import print_function
import unittest
import sys

TRACE = False

def matches(string, begin, end):
    stack = list()

    for character in string:
        if TRACE:
            print(character)
        if character in begin:
            if TRACE:
                print("pushing: ", character)
            stack.append(character)
        elif character in end:
            if len(stack) == 0:
                if TRACE:
                    print("empty stack, no opening ", character)
                return False
            char = stack.pop()
            whereInBegin = begin.find(char)
            whereInEnd = end.find(character)
            if TRACE:
                print("popping: ", char)
                print("whereInBegin: ", whereInBegin)
                print("whereInEnd: ", whereInEnd)

            if not whereInBegin == whereInEnd:
                return False

    if not len(stack) == 0:
        if TRACE:
            print("non-empty stack, too many opens")
        return False
    return True

class TestMatches(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(matches("", "", ""))
        self.assertTrue(matches("", "<", ">"))
    def test_nomatch(self):
        self.assertTrue(matches("a", "", ""))
        self.assertTrue(matches("a", "<", ">"))
        self.assertTrue(matches("a", "({[", ")}]"))
    def test_simple(self):
        self.assertTrue(matches("<>", "<", ">"))
        self.assertTrue(matches("()", "({[", ")}]"))
        self.assertFalse(matches("(", "({[", ")}]"))
        self.assertFalse(matches(")", "({[", ")}]"))
    def test_nested(self):
        self.assertTrue(matches("(())", "({[", ")}]"))
        self.assertTrue(matches("({})", "({[", ")}]"))
        self.assertTrue(matches("This(is{a}test)", "({[", ")}]"))

for line in sys.stdin:
    print (matches(line, "<", ">"))
