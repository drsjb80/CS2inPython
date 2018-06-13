import unittest

class TestEmpty(unittest.TestCase):
    def test(self):
        self.assertFalse(sequential_search([], 1))

class TestOne(unittest.TestCase):
    def test(self):
        self.assertTrue(sequential_search([1], 1))
        self.assertFalse(sequential_search([1], 2))

class TestMiddle(unittest.TestCase):
    def test(self):
        self.assertTrue(sequential_search([1, 2, 3], 2))

class TestEnds(unittest.TestCase):
    def test(self):
        self.assertTrue(sequential_search([1, 2, 3], 1))
        self.assertTrue(sequential_search([1, 2, 3], 3))

class TestMissing(unittest.TestCase):
    def test(self):
        self.assertFalse(sequential_search([1, 2, 3], 4))

def sequential_search(list, value):
    if not list:
        return False

    if len(list) == 1:
        return list[0] == value

    for item in list:
        if item == value:
            return True

    return False
