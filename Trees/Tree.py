from __future__ import print_function
import unittest

TRACE = False

class BinaryTree:
    # create a unique empty value so None can be stored
    _empty = {}

    def __init__ (self, value = None, parent = None):
        self._left = self._right = None
        self._value = self._empty
        self._parent = parent

        if value:
            try:
                for i in value:
                    self.add(i)
            except TypeError:
                self.add(value)

    def __iter__(self):
        if self._left:
            for node in self._left:
                yield(node)

        yield(self._value)

        if self._right:
            for node in self._right:
                yield(node)

    def empty(self): return self._value == self._empty

    def __str__(self): 
        return(','.join(str(node) for node in self))

    def add(self, value):
        if self.empty():
            self._value = value
            return

        if value < self._value:
            if not self._left:
                self._left = BinaryTree(value, self)
            else:
                self._left.add(value)
        else:
            if not self._right:
                self._right = BinaryTree(value, self)
            else:
                self._right.add(value)
        
    def _find_leftmost(self):
        t = self
        while t._left:
            t = t._left
        return(t)
    
    def _find_rightmost(self):
        t = self
        while t._right:
            t = t._right
        return(t)

    def _parent_replace_me_with(self, new):
        if TRACE:
            print("in:", self._parent._value, "replacing:", \
                self._value, "with:",)
            if new:
                print(new._value,)
            else:
                print(new,)

        if self._parent._left == self:
            if TRACE: print("on the left")
            self._parent._left = new
        elif self._parent._right == self:
            if TRACE: print("on the right")
            self._parent._right = new
        else:
            assert(True)

    def __remove_both(self):
        # find the right-most of the left hand tree
        rightmost = self._left._find_rightmost()
        if TRACE: print("rightmost:", rightmost._value)

        # remove it
        self.remove(rightmost._value)

        # tricky bit: if it's the root, don't change
        # the refenence but only the value
        if not self._parent:
            self._value = rightmost._value
        else:
            rightmost._left = self._left
            rightmost._right = self._right
            self._parent_replace_me_with(rightmost)

    def remove(self, value):
        if self._value == value:
            if not self._left and not self._right:
                self._parent_replace_me_with(None)
            elif not self._left:
                self._parent_replace_me_with(self._right)
            elif not self._right:
                self._parent_replace_me_with(self._left)
            else:
                self.__remove_both()
        elif self._value > value:
            self._left.remove(value)
        else:
            self._right.remove(value)

class TestBinaryTree (unittest.TestCase):
    '''
      20
     /  \
    10  30
       /  \
      25  35
    '''

    def test_empty(self):
        self.assertTrue(BinaryTree().empty())

    def test_add(self):
        bt = BinaryTree()
        bt.add(20)
        bt.add(10)
        bt.add(30)
        bt.add(25)
        bt.add(35)
        self.assertEquals(str(bt), '10,20,25,30,35')

    def test_remove_left_leaf(self):
        bt = BinaryTree([20, 10, 30, 25, 35])
        bt.remove(25)
        self.assertEquals(str(bt), '10,20,30,35')

    def test_remove_leaf_right(self):
        bt = BinaryTree([20, 10, 30, 25, 35])
        bt.remove(35)
        self.assertEquals(str(bt), '10,20,25,30')

    def test_remove_only_left(self):
        bt = BinaryTree([20, 10, 5, 30, 25, 35])
        bt.remove(10)
        self.assertEquals(str(bt), '5,20,25,30,35')

    def test_remove_only_right(self):
        bt = BinaryTree([20, 10, 15, 30, 25, 35])
        bt.remove(10)

    def test_remove_both(self):
        bt = BinaryTree([20, 10, 15, 30, 25, 35])
        bt.remove(30)
        self.assertEquals(str(bt), '10,15,20,25,35')

    '''
      20
     /  \
    10  30
       /  \
      25  35
     /
    24
    '''

    def test_remove_both_again(self):
        bt = BinaryTree([20, 10, 30, 25, 24, 35])
        bt.remove(30)
        self.assertEquals(str(bt), '10,20,24,25,35')

    '''
      20
     /  \
    10  30
       /  \
      25  35
     / \
    24 27
    '''

    def test_double_recursion(self):
        bt = BinaryTree([20, 10, 30, 25, 24, 27, 35])
        bt.remove(30)
        self.assertEquals(str(bt), '10,20,24,25,27,35')

    def test_remove_root(self):
        bt = BinaryTree([20, 10, 30, 25, 35])
        bt.remove(20)
        self.assertEquals(str(bt), '10,25,30,35')

    def test_init(self):
        bt = BinaryTree([20, 10, 30, 25, 35])
        self.assertEquals(str(bt), '10,20,25,30,35')

if '__main__' == __name__:
    pass
