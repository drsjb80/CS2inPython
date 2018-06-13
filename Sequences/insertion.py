import unittest

'''
Description:
Author:
Version:
Help provided to:
Help received from:
'''

class TestEmpty(unittest.TestCase):
    def test(self):
        ll = LinkedList()
        ll.insert(1)
        self.assertEqual(str(ll), '[1]')

class TestBeforeFirst(unittest.TestCase):
    def test(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(1)
        self.assertEqual(str(ll), '[1, 10]')

class TestAfterLast(unittest.TestCase):
    def test(self):
        ll = LinkedList()
        ll.insert(1)
        ll.insert(10)
        self.assertEqual(str(ll), '[1, 10]')

class TestBetween(unittest.TestCase):
    def test(self):
        ll = LinkedList()
        ll.insert(1)
        ll.insert(10)
        ll.insert(5)
        self.assertEqual(str(ll), '[1, 5, 10]')

class TestMore(unittest.TestCase):
    def test(self):
        ll = LinkedList()
        ll.insert(1)
        ll.insert(10)
        ll.insert(5)
        ll.insert(4)
        ll.insert(6)
        self.assertEqual(str(ll), '[1, 4, 5, 6, 10]')

class LinkedList(object):
    class Node(object):
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self, initial=None):
        self.front = self.back = None

    def empty(self):
        return self.front is None and self.back is None

    def __iter__(self):
        self.current = self.front
        return self

    def __next__(self):
        if self.current:
            tmp = self.current.value
            self.current = self.current.next
            return tmp
        else:
            raise StopIteration()

    def __str__(self):
        return str([item for item in self])

    def insert(self, value):
        if self.empty():
            self.front = self.back = self.Node(value)
        elif value < self.front.value:
            self.front = self.Node(value, self.front)
        elif value > self.back.value:
            self.back.next = self.Node(value)
            self.back = self.back.next
            '''
            This works:
            self.back.next = self.back = node
            This doesn't:
            self.back = self.back.next = node
            Hmmm.
            '''
        else:
            current = self.front

            while value < current.value or value > current.next.value:
                current = current.next

            current.next = self.Node(value, current.next)
