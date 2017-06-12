from __future__ import print_function
import unittest


def matches(string, begin, end):
    stack = list()

    for character in string:
        if character in begin:
            stack.append(character)
        elif character in end:
            if len(stack) == 0:
                return False
            char = stack.pop()
            whereInBegin = begin.find(char)
            whereInEnd = end.find(character)

            if not whereInBegin == whereInEnd:
                return False

    if not len(stack) == 0:
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
