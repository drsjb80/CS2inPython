import unittest

class convert:
    def f2c_one (self, f):
        return (f * 5/9 - 32)

    def f2c_two (self, f):
        return ((f - 32) * 5/9)

class test_convert (unittest.TestCase):
    def test_f2c_one (self):
        self.assertEquals(convert().f2c_one (212), 100)

    def test_f2c_two (self):
        self.assertEquals(convert().f2c_two (212), 100)

if __name__ == '__main__':
    unittest.main()
