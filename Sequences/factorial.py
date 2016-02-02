import unittest

main = "__main__" == __name__

'''"Pretend" to do recursion via a stack and iteration'''
class factorial:
    def fact(self, a):
        if a < 0: raise ValueError("Less than zero")
        if 0 == a or 1 == a: return 1

        stack = []
        while a > 1:
            stack.append(a)
            a -= 1

        result = 1
        while stack:
            result *= stack.pop()

        return result

class test_factorial (unittest.TestCase):
    def test_less_than_zero(self):
        self.assertRaises(ValueError, lambda: factorial().fact(-1))
    def test_zero(self):
        self.assertEquals(factorial().fact(0), 1)
    def test_one(self):
        self.assertEquals(factorial().fact(1), 1)
    def test_two(self):
        self.assertEquals(factorial().fact(2), 2)
    def test_10(self):
        self.assertEquals(factorial().fact(10), 10*9*8*7*6*5*4*3*2*1)

if main:
        print (factorial().fact(1))
        print (factorial().fact(2))
        print (factorial().fact(100))
