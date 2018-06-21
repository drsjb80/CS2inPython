import unittest

def reverse(iteratable):
    if 1 == len(iteratable):
        return iteratable

    return reverse(iteratable[1:]) + iteratable[:1]

class TestReverse(unittest.TestCase):
    def test_string(self):
        self.assertEqual(reverse("hello"), "olleh")
    def test_list(self):
        self.assertEqual(reverse([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
    def test_nested(self):
        self.assertEqual(reverse([[1, ["one", "two"], 2], [3, 4], 5]), \
            [5, [3, 4], [1, ['one', 'two'], 2]])

if '__main__' == __name__:
    unittest.main()
