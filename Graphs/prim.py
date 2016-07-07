from __future__ import print_function
from weighted_digraph import weighted_digraph
import unittest

def prim(graph):
  remaining = graph.get_nodes()
  length = len(remaining)
  tree = [remaining[0]]
  result = []

  while True:
    # find the min edge not in tree
    min_value = float("inf")
    for node in tree:
      for edge in node.edges:
        if edge.to_node in tree: continue
        if edge.weight < min_value:
          min_value = edge.weight
          min_node = edge.to_node

    result.append(str(node.value) + '->' + str(min_node.value))
    tree.append(min_node)
    remaining.remove(min_node)

    if len(tree) == length: break;

  return result

class test_prim(unittest.TestCase):
  '''
  1--(7)--2--(8)--3
  |     /   \     |
 (5) (9)     (7) (5)
  | /          \  |
  4------(15)-----5
    \           / |
     (6)    (8)  (9)
       \  /       |
        6 --(11)- 7
  '''

  def test_prim(self):
    g = weighted_digraph()
    g.add_edges([(1,2,7), (1,4,5), (2,3,8), (2,4,9), (2,5,7), (3,5,5), \
      (4,5,15), (4,6,6), (5,6,8), (5,7,9), (6,7,11)])
    self.assertEquals(prim(g), \
      ['1->4', '4->6', '6->2', '2->5', '5->3', '3->7'])
