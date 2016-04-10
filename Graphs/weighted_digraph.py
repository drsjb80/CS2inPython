from __future__ import print_function
from sys import stdin
import unittest

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
      self.edges = []

    def __str__(self):
      result = str(self.value)
      for edge in self.edges:
        result += "->" + str(edge.to_node.value) + \
          "(" + str(edge.weight) + ")"
      return(result)

    def add_edge(self, new_edge):
      if not self.is_adjacent(new_edge.to_node):
          self.edges.append(new_edge)

    def remove_edge(self, to_node):
      for edge in self.edges:
        if edge.to_node == to_node:
          self.edges.remove(edge)

    def is_adjacent(self, node):
      for edge in self.edges:
        if edge.to_node == node:
          return(True)
      return(False)

  """ The directed, weighted, graph class itself """
  def __init__(self, directed=True):
    """ Could be a set if we define both __eq__ and __hash__ """
    self.__nodes = []
    self.__directed = directed

  def __len__(self): return(len(self.__nodes))

  def __str__(self):
    result = ""
    for node in self.__nodes:
      result += str(node) + '\n'
    return(result)

  def get_nodes(self): return self.__nodes[:]

  def find(self, value):
    for node in self.__nodes:
      if node.value == value:
        return(node)

    return(None)

  def add_nodes(self, nodes):
    for node in nodes:
      self.add_node(node)

  def add_node(self, value):
    if not self.find(value):
      self.__nodes.append(self.__node(value))

  def add_edges(self, edges):
    for edge in edges:
      self.add_edge(edge[0], edge[1], edge[2])

  """ Add an edge between two values. If the nodes
      for those values aren't already in the graph,
      add those. """
  def add_edge(self, from_value, to_value, weight):
    from_node = self.find(from_value)
    to_node = self.find(to_value)

    if not from_node:
      self.add_node(from_value)
      from_node = self.find(from_value)
    if not to_node:
      self.add_node(to_value)
      to_node = self.find(to_value)

    from_node.add_edge(self.__edge(to_node, weight))
    if not self.__directed:
      to_node.add_edge(self.__edge(from_node, weight))

  def remove_edge(self, from_value, to_value, weight):
    from_node = self.find(from_value)
    to_node = self.find(to_value)

    from_node.remove_edge(to_node)
    if not self.directed:
      to_node.remove_edge(from_node)
  
  def are_adjacent(self, value1, value2):
    return(self.find(value1).is_adjacent(self.find(value2)))

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
    self.assertEqual(str(g), '1->2(3)\n2\n')

  def test_adding_ints(self):
    g = weighted_digraph()
    g.add_nodes([1, 2])
    g.add_edges([(1, 2, 3), (2, 1, 3)])
    self.assertEqual(str(g), '1->2(3)\n2->1(3)\n')

  def test_adding_strings(self):
    g = weighted_digraph()
    g.add_nodes(['Denver', 'Boston'])
    g.add_edges([('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
    self.assertEqual(str(g), 'Denver->Boston(1971.8)\nBoston->Denver(1971.8)\n')

  def test_are_adjacent(self):
    g = weighted_digraph()
    g.add_nodes(['Denver', 'Boston'])
    g.add_edges([('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
    self.assertTrue(g.are_adjacent('Denver', 'Boston'))

  def test_arent_adjacent(self):
    g = weighted_digraph()
    g.add_nodes(['Denver', 'Boston', 'Milano'])
    g.add_edges([('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
    self.assertFalse(g.are_adjacent('Denver', 'Milano'))

  def test_arent_adjacent_directed(self):
    g = weighted_digraph()
    g.add_edges([('Denver', 'Boston', 1971.8)])
    self.assertFalse(g.are_adjacent('Denver', 'Milano'))
    self.assertFalse(g.are_adjacent('Boston', 'Denver'))
    self.assertTrue(g.are_adjacent('Denver', 'Boston'))

  def test_arent_adjacent_undirected(self):
    g = weighted_digraph(False)
    g.add_edges([('Denver', 'Boston', 1971.8)])
    self.assertTrue(g.are_adjacent('Boston', 'Denver'))
    self.assertTrue(g.are_adjacent('Denver', 'Boston'))

  def test_add_edges_without_nodes(self):
    g = weighted_digraph()
    g.add_edges([('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
    self.assertEqual(str(g), \
      'Denver->Boston(1971.8)\nBoston->Denver(1971.8)\n')
