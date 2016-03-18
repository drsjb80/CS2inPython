from __future__ import print_function
import unittest
import sys

""" Values are what the user sees, nodes are our internals """
class weighted_digraph:

  """ An internal representation of an edge """
  class __edge(object):
    def __init__(self, to_node, weight):
      self.to_node = to_node
      self.weight = weight

  """ An internal representation of a node """
  class __node(object):
    def __init__(self, value):
      self.value = value
      self.edges = set()

    def __str__(self):
      result = str(self.value)
      for edge in self.edges:
        result += "->" + str(edge.to_node.value) + \
          "(" + str(edge.weight) + ")"
      return(result)

    def add_edge(self, new_edge):
      self.edges.add(new_edge)

    def is_adjacent(self, node):
      for edge in self.edges:
        if edge.to_node == node:
          return(True)
      return(False)

  """ The directed, weighted, graph class itself """
  def __init__(self, nodes=None, edges=None):
    """ Could be a set if we define both __eq__ and
        __hash__ """
    self.__nodes = []

    if nodes:
      for node in nodes:
        self.add_node(node)

    if edges:
      for edge in edges:
        self.add_edge(edge[0], edge[1], edge[2])

  def __len__(self): return(len(self.__nodes))

  def __str__(self):
    result = ""
    for node in self.__nodes:
      result += str(node) + ';'
    return(result)

  def __find(self, value):
    for node in self.__nodes:
      if node.value == value:
        return(node)

    return(None)

  def add_node(self, value):
    if not self.__find(value):
      self.__nodes.append(self.__node(value))

  """ Add an edge between two values. If the nodes
      for those values aren't already in the graph,
      add them. """
  def add_edge(self, from_value, to_value, weight):
    fn = self.__find(from_value)
    tn = self.__find(to_value)

    if not fn:
      self.add_node(from_value)
      fn = self.__find(from_value)
    if not tn:
      self.add_node(to_value)
      tn = self.__find(to_value)

    fn.add_edge(self.__edge(tn, weight))
  
  def are_adjacent(self, value1, value2):
    return(self.__find(value1).is_adjacent(self.__find(value2)))

class test_weighted_digraph(unittest.TestCase):
  def test_empty(self):
    self.assertEqual(len(weighted_digraph()), 0)

  def test_one(self):
    g = weighted_digraph()
    g.add_node(1)
    self.assertEqual(len(g), 1)

  def test_duplicate(self):
    g = weighted_digraph()
    g.add_node(1)
    g.add_node(1)
    self.assertEqual(len(g), 1)

  def test_two(self):
    g = weighted_digraph()
    g.add_node(1)
    g.add_node(2)
    self.assertEqual(len(g), 2)

  def test_edge(self):
    g = weighted_digraph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2, 3)
    self.assertEqual(str(g), '1->2(3);2;')

  def test_init(self):
    g = weighted_digraph([1, 2], [(1, 2, 3), (2, 1, 3)])
    self.assertEqual(str(g), '1->2(3);2->1(3);')

  def test_init(self):
    g = weighted_digraph(['Denver', 'Boston'], \
      [('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
    self.assertEqual(str(g), 'Denver->Boston(1971.8);Boston->Denver(1971.8);')

  def test_are_adjacent(self):
    g = weighted_digraph(['Denver', 'Boston'], \
      [('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
    self.assertTrue(g.are_adjacent('Denver', 'Boston'))

  def test_arent_adjacent(self):
    g = weighted_digraph(['Denver', 'Boston', 'Milano'], \
      [('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
    self.assertFalse(g.are_adjacent('Denver', 'Milano'))

  def test_add_edges_without_nodes(self):
    g = weighted_digraph([], \
      [('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
    self.assertEqual(str(g), 'Denver->Boston(1971.8);Boston->Denver(1971.8);')
