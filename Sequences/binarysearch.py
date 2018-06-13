import unittest

class TestEmpty(unittest.TestCase):
    def test(self):
        self.assertFalse(binary_search([], 1))

class TestOne(unittest.TestCase):
    def test(self):
        self.assertTrue(binary_search([1], 1))
        self.assertFalse(binary_search([1], 2))

class TestMiddle(unittest.TestCase):
    def test(self):
        self.assertTrue(binary_search([1, 2, 3], 2))

class TestEnds(unittest.TestCase):
    def test(self):
        self.assertTrue(binary_search([1, 2, 3], 1))
        self.assertTrue(binary_search([1, 2, 3], 3))

class TestMissing(unittest.TestCase):
    def test(self):
        self.assertFalse(binary_search([1, 2, 3], 4))

def binary_search(list, value):
    if not list:
        return False

    if len(list) == 1:
        return list[0] == value

    left = 0
    right = len(list) - 1
    while True:
        if left > right:
            return False

        middle = (left + right) // 2

        if list[middle] == value:
            return True
        elif list[middle] > value:
            right = middle - 1
        else:
            left = middle + 1
