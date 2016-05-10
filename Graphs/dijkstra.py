from __future__ import print_function
from weighted_digraph import weighted_digraph, weighted_graph
from sys import stdin
import unittest

track_prev = False

def dijkstra(graph, start):

  nodes = graph.get_nodes()
  for node in nodes:
    node.dist = float("inf")
    node.prev = None

  source = graph.find(start)
  source.dist = 0

  todo = set()
  todo.add(source)

  results = []

  while todo:
    min_node = min(todo, key=lambda node: node.dist)
    todo.remove(min_node)

    result = [min_node.dist, min_node.value]

    if track_prev:
      prev = min_node.prev
      while prev and prev != start:
        result.append(prev.value)
        prev = prev.prev

    results.append(result)

    for edge in min_node.edges:
      new_dist = min_node.dist + edge.weight
      if new_dist < edge.to_node.dist:
        edge.to_node.dist = new_dist
        edge.to_node.prev = min_node
        todo.add(edge.to_node)

  return(results)

class test_dijkstra(unittest.TestCase):
  def test_dijkstra(self):
    '''
        2---1---4
       /|\      |\
      2 | \     | 6
     /  |  \    |  \
    1   1   2   3   6
     \  |    \  |  /
      1 |     \ | 1
       \|      \|/
        3---5---5
    '''
    g = weighted_digraph()
    g.add_edges([(1,2,2), (1,3,1), (2,3,1), (2,4,1), \
      (2,5,2), (3,5,5), (4,5,3), (4,6,6), (5,6,1)])
    if not track_prev:
      self.assertEquals(dijkstra(g, 1), [[0, 1], [1, 3], [2, 2], \
        [3, 4], [4, 5], [5, 6]])
    else:
      self.assertEquals(dijkstra(g, 1), [[0, 1], [1, 3, 1], [2, 2, 1], \
        [3, 4, 2, 1], [4, 5, 2, 1], [5, 6, 5, 2, 1]])

if '__main__' == __name__:
  g = weighted_graph()
  for line in stdin:
    a = line.strip().split(" ")
    g.add_edge(a[0], a[1], int(a[2]))
  result = dijkstra(g, "Denver")
  for city in result:
    print(city[1], "is", city[0], 'miles from Denver')
    if track_prev:
      for path in city[2:]:
        print("   ", path)
