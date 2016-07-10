from __future__ import print_function
import unittest
from weighted_digraph import WeightedDigraph

def depth_first_search(graph, start_value, target_value):
    target_node = graph.find(target_value)
    start_node = graph.find(start_value)
    if not target_node or not start_node: return None

    stack = [start_node]
    visited = []

    while stack:
        current = stack.pop()
        visited.append(current)

        if current.value == target_value:
            return [node.value for node in visited]

        for edge in current.edges:
            if edge.to_node not in stack and edge.to_node not in visited:
                stack.append(edge.to_node)

    return None

def breadth_first_search(graph, start_value, target_value):
    start_node = graph.find(start_value)
    target_node = graph.find(target_value)
    if not target_node or not start_node: return None

    queue = [start_node]
    visited = []

    while queue:
        current = queue.pop(0)
        visited.append(current)

        if current.value == target_value:
            return [node.value for node in visited]

        for edge in current.edges:
            if edge.to_node not in queue and edge.to_node not in visited:
                queue.append(edge.to_node)

    return None

def _recursive_depth_first_search(graph, start_node, target_node, visited):
    visited.append(start_node)

    if start_node.value == target_node.value:
        return [node.value for node in visited]

    for edge in start_node.edges:
        if edge.to_node not in visited:
            return _recursive_depth_first_search(graph, edge.to_node, \
                target_node, visited)

    return None

def recursive_depth_first_search(graph, start_value, target_value):
    start_node = graph.find(start_value)
    target_node = graph.find(target_value)
    if not target_node or not start_node: return None

    return _recursive_depth_first_search(graph, start_node, target_node, [])

class TestSearches(unittest.TestCase):
    r'''
       2---->4
      ^|\    |\
     / | \   | V
    1  |  \  | 6
     \ |   \ | ^
      VV    VV/
       3---->5
    '''

    def setUp(self):
        self.test_graph = WeightedDigraph()
        self.test_graph.add_edges([(1, 2, 1), (1, 3, 1), (2, 3, 1), \
            (2, 4, 1), (2, 5, 1), (3, 5, 1), (4, 5, 1), (4, 6, 1), (5, 6, 1)])

    def test_depth_first_search(self):
        self.assertEquals(depth_first_search(self.test_graph, 1, 6), \
            [1, 3, 5, 6])
        self.assertEquals(depth_first_search(self.test_graph, 3, 4), None)
        self.assertEquals(depth_first_search(self.test_graph, 1, 7), None)

    def test_recursive_depth_first_search(self):
        self.assertEquals( \
            recursive_depth_first_search(self.test_graph, 1, 6), \
            [1, 2, 3, 5, 6])
        self.assertEquals( \
            recursive_depth_first_search(self.test_graph, 3, 4), None)
        self.assertEquals( \
            recursive_depth_first_search(self.test_graph, 1, 7), None)

    def test_breadth_first_search(self):
        self.assertEquals(breadth_first_search(self.test_graph, 1, 6), \
            [1, 2, 3, 4, 5, 6])
        self.assertEquals(breadth_first_search(self.test_graph, 5, 1), None)
        self.assertEquals(breadth_first_search(self.test_graph, 1, 7), None)

    def test_short_breadth_first_search(self):
        self.assertEquals(breadth_first_search(self.test_graph, 1, 2), [1, 2])
