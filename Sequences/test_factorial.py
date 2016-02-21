import unittest
from factorial import factorial

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

unittest.main()
