from __future__ import print_function
import unittest
from weighted_digraph import WeightedGraph

def prim(graph):
    remaining = graph.get_nodes()
    for node in remaining:
        node.distance = float('inf')
    remaining[0].distance = 0
    remaining[0].from_node = None

    result = []
    total = 0

    while remaining:
        remaining.sort(key=lambda node: node.distance)
        choice = remaining.pop(0)

        if choice.from_node:
            result.append(str(choice.from_node.value) + \
                '->' + str(choice.value))
            total += choice.from_node.get_edge(choice).weight

        for edge in choice.edges:
            if edge.to_node in remaining and \
                edge.weight < edge.to_node.distance:
                edge.to_node.distance = edge.weight
                edge.to_node.from_node = choice

    return result, total

class TestPrim(unittest.TestCase):
    r'''
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
        graph = WeightedGraph()
        graph.add_edges([(1, 2, 7), (1, 4, 5), (2, 3, 8), (2, 4, 9), \
            (2, 5, 7), (3, 5, 5), (4, 5, 15), (4, 6, 6), (5, 6, 8), \
            (5, 7, 9), (6, 7, 11)])
        self.assertEquals(prim(graph), \
            (['1->4', '4->6', '1->2', '2->5', '5->3', '5->7'], 39))
