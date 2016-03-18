from __future__ import print_function
import unittest
import sys

class graph:
  def __init__(self, nodes=None, edges=None):
    self.__nodes = set()
    self.__edges = set()

    if nodes:
      for node in nodes:
        self.__nodes.add(node)

    if edges:
      for edge in edges:
        self.__edges.add(edge)

  # return immutable tuples
  def nodes(self): return(tuple(self.__nodes))
  def edges(self): return(tuple(self.__edges))

  def add_node(self, node): self.__nodes.add(node) 
  def add_edge(self, edge): self.__edges.add(edge)
  
  def adjacent(self, node):
    result = ()
    for edge in self.__edges:
      if edge[0] in result or edge[1] in result: continue
      if edge[0] == node: result += (edge[1],)
      if edge[1] == node: result += (edge[0],)
    return(result)

  """Find a path through a graph"""
  def DFS(self, start, target):
    stack = [start]
    visited = []

    while stack:
      current = stack.pop()
      visited.append(current)

      if current == target: return visited

      for v in self.adjacent(current):
        if v not in visited:
          stack.append(v)

    return None

  def rDFS(self, start, target, visited):
    visited.append(start)

    if start == target: return visited

    for v in self.adjacent(start):
      if v not in visited:
        return(self.rDFS(v, target, visited))

    return None

  def BFS(self, start, target):
    queue = [start]
    visited = []

    while queue:
      current = queue.pop(0)

      if current in visited: continue

      visited.append(current)

      if current == target: return visited

      for v in self.adjacent(current):
        if v not in visited and v not in queue:
          queue.append(v)
      
    return None

  def __str__(self):
    return("nodes:" + str(self.nodes()) + ", edges:" + str(self.edges()))

class test_graph(unittest.TestCase):
  def test_empty(self):
    self.assertEqual(len(graph().nodes()), 0)
  def test_one(self):
    g = graph()
    g.add_node(1)
    self.assertEqual(len(g.nodes()), 1)
  def test_duplicate(self):
    g = graph()
    g.add_node(1)
    g.add_node(1)
    self.assertEqual(len(g.nodes()), 1)
  def test_two(self):
    g = graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge((1, 2))
    self.assertEqual(len(g.nodes()), 2)
    self.assertEqual(len(g.edges()), 1)
    self.assertEqual(str(g), 'nodes:(1, 2), edges:((1, 2),)')
  def test_init(self):
    g = graph([1, 2], [(1, 2)])
    self.assertEqual(str(g), 'nodes:(1, 2), edges:((1, 2),)')
  def test_adjacent(self):
    g = graph([1, 2], [(1, 2), (2, 1)])
    self.assertEqual(g.adjacent(1), (2,))
  def test_more_adjacent(self):
    g = graph([1, 2, 3, 4, 5, 6], [(1,2), (1,3), (2,3), (2,4), (2,5), \
      (3,5), (4,5), (4,6), (5,6)])
    self.assertEqual(g.adjacent(2), (1, 3, 5, 4,))
  def test_strings(self):
    g = graph(['Denver', 'Boulder'], [('Denver', 'Boulder')])
    self.assertEqual(str(g), "nodes:('Boulder', 'Denver'), \
edges:(('Denver', 'Boulder'),)")
  def test_DFS(self):
    '''
      2---4
     /|\  |\
    1 | \ | 6
     \|  \|/
      3---5
    '''
    g = graph([1, 2, 3, 4, 5, 6], [(1,2), (1,3), (2,3), (2,4), (2,5), \
      (3,5), (4,5), (4,6), (5,6)])
    self.assertEquals(g.DFS(1, 6), [1, 3, 5, 2, 4, 6])
    self.assertEquals(g.DFS(3, 4), [3, 5, 2, 4])
    self.assertEquals(g.DFS(1, 7), None)
  def test_rDFS(self):
    g = graph([1, 2, 3, 4, 5, 6], [(1,2), (1,3), (2,3), (2,4), (2,5), \
      (3,5), (4,5), (4,6), (5,6)])
    self.assertEquals(g.rDFS(1, 6, []), [1, 2, 3, 5, 4, 6])
    self.assertEquals(g.rDFS(3, 4, []), [3, 1, 2, 5, 4])
    self.assertEquals(g.rDFS(1, 7, []), None)
  def test_BFS(self):
    g = graph([1, 2, 3, 4, 5, 6], [(1,2), (1,3), (2,3), (2,4), (2,5), \
      (3,5), (4,5), (4,6), (5,6)])
    self.assertEquals(g.BFS(1, 6), [1, 2, 3, 5, 4, 6])
    self.assertEquals(g.BFS(5, 1), [5, 4, 6, 2, 3, 1])
    self.assertEquals(g.BFS(1, 7), None)
