from __future__ import print_function
import unittest

def fact(n):
    '''"Pretend" to do recursion via a stack and iteration'''
    if n < 0: raise ValueError("Less than zero")
    if 0 == n or 1 == n: return 1

    stack = []
    while n > 1:
        stack.append(n)
        n -= 1

    result = 1
    while stack:
        result *= stack.pop()

    return result

class TestFactorial(unittest.TestCase):
    def test_less_than_zero(self):
        self.assertRaises(ValueError, lambda: fact(-1))
    def test_zero(self):
        self.assertEquals(fact(0), 1)
    def test_one(self):
        self.assertEquals(fact(1), 1)
    def test_two(self):
        self.assertEquals(fact(2), 2)
    def test_10(self):
        self.assertEquals(fact(10), 10*9*8*7*6*5*4*3*2*1)

if "__main__" == __name__:
    print(fact(1))
    print(fact(2))
    print(fact(100))
