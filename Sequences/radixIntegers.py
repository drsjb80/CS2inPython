import unittest

# position = digits from the RHS. e.g.: 1002, 1 returns 2
def digit(number, position):
    number /= 10 ** (position-1)
    return int(number % 10)

class testDigit(unittest.TestCase):
    def testOne(self):
        self.assertEquals(digit(1234, 1), 4)
    def testTwo(self):
        self.assertEquals(digit(1234, 2), 3)
    def testThree(self):
        self.assertEquals(digit(1234, 3), 2)
    def testFour(self):
        self.assertEquals(digit(1234, 4), 1)
    def testFive(self):
        self.assertEquals(digit(1234, 5), 0)

def radixSort(array):
    for i in range(len(array)):
        buckets = [[] for _ in range(10)]

        for integer in array:
            where = digit(integer, i+1)
            buckets[where].append(integer)

        array = []
        for bucket in buckets:
            array.extend(bucket)

    return array

class testRadix(unittest.TestCase):
    def testOne(self):
        self.assertEquals(radixSort([1]), [1])
    def testTwo(self):
        self.assertEquals(radixSort([2, 1]), [1, 2])
    def testTen(self):
        self.assertEquals(radixSort([2, 1, 9, 4, 7, 10, 5, 6, 3, 8]), \
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
