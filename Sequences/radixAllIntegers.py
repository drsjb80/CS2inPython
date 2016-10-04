import unittest
import random
import math

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
    longest = 0
    position = 1

    while True:
        buckets = [[] for _ in range(10)]

        for integer in array:
            # find the number of digits in the longest number
            if position == 1:
                numDigits = 0 if integer == 0 else \
                    math.floor(math.log(integer, 10)) + 1
                longest = longest if numDigits < longest else numDigits

            thisDigit = digit(integer, position)
            buckets[thisDigit].append(integer)

        array = []
        for bucket in buckets:
            array.extend(bucket)

        position += 1
        if position > longest: break

    return array

class testRadix(unittest.TestCase):
    def testOne(self):
        self.assertEquals(radixSort([1]), [1])
    def testTwo(self):
        self.assertEquals(radixSort([2, 1]), [1, 2])
    def testMultiple(self):
        self.assertEquals(radixSort([20, 1, 99, 407, 70023, 1002]), \
            [1, 20, 99, 407, 1002, 70023])
    def test10000(self):
        a = [x for x in range(10000)]
        b = a[:]
        random.shuffle(a)
        self.assertEquals(radixSort(a), b)
