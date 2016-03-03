from __future__ import print_function
import unittest

class binary_tree:
  def __init__ (self, value = None, parent = None):
    self.__left = self.__right = self.__value = None
    self.__parent = parent

    try:
      for i in value:
        self.add(i)
    except TypeError:
      self.add(value)

  def __iter__(self):
    if self.__left:
      for node in self.__left:
        yield(node)

    yield(self.__value)

    if self.__right:
      for node in self.__right:
        yield(node)

  def __str__(self): 
    return(','.join(str(node) for node in self))

  def add(self, value):
    if self.__value == None:
      self.__value = value
      return

    if value < self.__value:
      if not self.__left:
        self.__left = binary_tree(value, self)
      else:
        self.__left.add(value)
    else:
      if not self.__right:
        self.__right = binary_tree(value, self)
      else:
        self.__right.add(value)
    
  def __replace_me(self, new):
      if self.__parent.__left == self:
        self.__parent.__left = new
      elif self.__parent.__right == self:
        self.__parent.__right = new
      else:
        assert(True)
  
  def __find_leftmost(self):
    t = self
    while t.__left:
      t = t.__left
    return(t)
  
  def __find_rightmost(self):
    t = self
    while t.__right:
      t = t.__right
    return(t)

  def remove(self, value):
    if self.__value == value:
      if not self.__left and not self.__right:
        self.__replace_me(None)
      elif not self.__left:
        self.__replace_me(self.__right)
      elif not self.__right:
        self.__replace_me(self.__left)
      else:
        # find the right-most of the left hand tree
        rightmost = self.__left.__find_rightmost()

        # remove it
        rightmost.__replace_me(None)

        # set its right and left to my right and left
        rightmost.__left = self.__left
        rightmost.__right = self.__right

        # ticky bit: if it's the root, don't change
        # the refenence but only the value
        if not self.__parent:
          self.__value = rightmost.__value
        else:
          self.__replace_me(rightmost)

    elif self.__value > value:
      self.__left.remove(value)
    else:
      self.__right.remove(value)

class test_binary_tree (unittest.TestCase):
  '''
   20
  /  \
10    30
     /  \
    25  35
  '''


  def test_remove_root(self):
    bt = binary_tree([20, 10, 30, 25, 35])
    bt.remove(20)
    self.assertEquals(str(bt), '10,25,30,35')

  def test_empty(self):
    self.assertEquals(str(binary_tree()), 'None')

  def test_add(self):
    bt = binary_tree()
    bt.add(20)
    bt.add(10)
    bt.add(30)
    bt.add(25)
    bt.add(35)
    self.assertEquals(str(bt), '10,20,25,30,35')

  def test_remove_left_leaf(self):
    bt = binary_tree([20, 10, 30, 25, 35])
    bt.remove(25)
    self.assertEquals(str(bt), '10,20,30,35')

  def test_remove_leaf_right(self):
    bt = binary_tree([20, 10, 30, 25, 35])
    bt.remove(35)
    self.assertEquals(str(bt), '10,20,25,30')

  def test_remove_only_left(self):
    bt = binary_tree([20, 10, 5, 30, 25, 35])
    bt.remove(10)
    self.assertEquals(str(bt), '5,20,25,30,35')

  def test_remove_only_right(self):
    bt = binary_tree([20, 10, 15, 30, 25, 35])
    bt.remove(10)

  def test_remove_both(self):
    bt = binary_tree([20, 10, 15, 30, 25, 35])
    bt.remove(30)
    self.assertEquals(str(bt), '10,15,20,25,35')

  def test_init(self):
    bt = binary_tree([20, 10, 30, 25, 35])
    self.assertEquals(str(bt), '10,20,25,30,35')

if '__main__' == __name__:
  pass
