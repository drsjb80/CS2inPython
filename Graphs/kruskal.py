from __future__ import print_function
import unittest
from weighted_digraph import WeightedGraph

def kruskal(graph):
    forrest, edges, solution, result = [], [], [], []
    nodes = graph.get_nodes()
    total = 0

    for node in nodes:
        single = set()
        single.add(node)
        forrest.append(single)
        for edge in node.edges:
            edges.append((node, edge.to_node, edge.weight))

    edges = sorted(edges, key=lambda edge: edge[2])

    while edges:
        min_edge = edges.pop(0)

        # find the two trees of the edge
        tree0 = tree1 = None
        for tree in forrest:
            if min_edge[0] in tree: tree0 = tree
            if min_edge[1] in tree: tree1 = tree
            if tree0 and tree1: break

        if tree0 != tree1:
            solution.append(min_edge)
            total += min_edge[2]
            result.append(str(min_edge[0].value) + '->' + \
                str(min_edge[1].value))
            forrest.remove(tree0)
            forrest.remove(tree1)
            forrest.append(tree0.union(tree1))

    return result, total

class TestKruskal(unittest.TestCase):
    r'''
    1--(7)--2--(8)--3
    |         /     \         |
 (5) (9)         (7) (5)
    | /                    \    |
    4------(15)-----5
        \                     / |
         (6)        (8)    (9)
             \    /             |
                6 --(11)- 7
    '''
    def test_kruskal(self):
        graph = WeightedGraph()
        graph.add_edges([(1, 2, 7), (1, 4, 5), (2, 3, 8), (2, 4, 9), \
            (2, 5, 7), (3, 5, 5), (4, 5, 15), (4, 6, 6), (5, 6, 8), \
            (5, 7, 9), (6, 7, 11)])
        self.assertEquals(kruskal(graph), \
            (['1->4', '3->5', '4->6', '1->2', '2->5', '5->7'], 39))
