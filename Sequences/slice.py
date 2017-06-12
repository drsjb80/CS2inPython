import unittest

string="This is a test"

class TestSlice(unittest.TestCase):
    def test_postive(self):
        self.assertEqual(string[0], "T")
        # [included:excluded]
        self.assertEqual(string[0:1], "T")
        self.assertEqual(string[0:2], "Th")
        self.assertEqual(string[0:], "This is a test")
        self.assertEqual(string[:], "This is a test")
        self.assertEqual(string[:4], "This")
        self.assertEqual(string[2:4], "is")
    def test_step(self):
        self.assertEqual(string[::2], "Ti sats")
    def test_negative(self):
        self.assertEqual(string[-4], "t")
        self.assertEqual(string[-4:], "test")
        self.assertEqual(string[-4:100], "test")
        self.assertEqual(string[4:-4], " is a ")
