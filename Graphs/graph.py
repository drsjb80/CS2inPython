from __future__ import print_function
import unittest

''' A very simple graph class. Has sets of nodes and edges. '''
class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self._nodes = set()
        self._edges = set()

        if nodes:
            for node in nodes:
                self._nodes.add(node)

        if edges:
            for edge in edges:
                self._edges.add(edge)

    # return immutable tuples
    def nodes(self): return tuple(self._nodes)
    def edges(self): return tuple(self._edges)

    def add_node(self, node): self._nodes.add(node)
    def add_edge(self, edge): self._edges.add(edge)

    def adjacent(self, node):
        result = ()
        for edge in self._edges:
            if edge[0] in result or edge[1] in result: continue
            if edge[0] == node: result += (edge[1],)
            if edge[1] == node: result += (edge[0],)
        return result

    def depth_first_search(self, start, target):
        stack = [start]
        visited = []

        while stack:
            current = stack.pop()
            visited.append(current)

            if current == target: return visited

            for vertex in self.adjacent(current):
                if vertex not in visited and vertex not in stack:
                    stack.append(vertex)

        return None

    def breadth_first_search(self, start, target):
        queue = [start]
        visited = []

        while queue:
            current = queue.pop(0)
            visited.append(current)

            if current == target: return visited

            for vertex in self.adjacent(current):
                if vertex not in visited and vertex not in queue:
                    queue.append(vertex)

        return None

    def recursive_depth_first_search(self, start, target, visited):
        visited.append(start)

        if start == target: return visited

        for vertex in self.adjacent(start):
            if vertex not in visited:
                return self.recursive_depth_first_search(vertex, \
                    target, visited)

        return None

    def __str__(self):
        return "nodes:" + str(self.nodes()) + \
            ", edges:" + str(self.edges())

class TestGraph(unittest.TestCase):
    def setUp(self):
        r'''
          2---4
         /|\  |\
        1 | \ | 6
         \|  \|/
          3---5
        '''
        self.test_graph = Graph([1, 2, 3, 4, 5, 6], [(1, 2), (1, 3), \
            (2, 3), (2, 4), (2, 5), (3, 5), (4, 5), (4, 6), (5, 6)])

    def test_empty(self):
        self.assertEqual(len(Graph().nodes()), 0)

    def test_one(self):
        graph = Graph()
        graph.add_node(1)
        self.assertEqual(len(graph.nodes()), 1)

    def test_duplicate(self):
        graph = Graph()
        graph.add_node(1)
        graph.add_node(1)
        self.assertEqual(len(graph.nodes()), 1)

    def test_two(self):
        graph = Graph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge((1, 2))
        self.assertEqual(len(graph.nodes()), 2)
        self.assertEqual(len(graph.edges()), 1)
        self.assertEqual(str(graph), 'nodes:(1, 2), edges:((1, 2),)')

    def test_init(self):
        graph = Graph([1, 2], [(1, 2)])
        self.assertEqual(str(graph), 'nodes:(1, 2), edges:((1, 2),)')

    def test_adjacent(self):
        graph = Graph([1, 2], [(1, 2), (2, 1)])
        self.assertEqual(graph.adjacent(1), (2,))

    def test_more_adjacent(self):
        self.assertEqual(self.test_graph.adjacent(2), (1, 3, 5, 4,))

    def test_strings(self):
        graph = Graph(['Denver', 'Boulder'], [('Denver', 'Boulder')])
        self.assertEqual(str(graph), "nodes:('Boulder', 'Denver'), \
edges:(('Denver', 'Boulder'),)")
    def test_depth_first_search(self):
        self.assertEquals(self.test_graph.depth_first_search(1, 6), \
            [1, 3, 5, 6])
        self.assertEquals(self.test_graph.depth_first_search(3, 4), \
            [3, 5, 6, 4])
        self.assertEquals(self.test_graph.depth_first_search(1, 7), \
            None)

    def test_recursive_depth_first_search(self):
        self.assertEquals( \
            self.test_graph.recursive_depth_first_search(1, 6, []), \
                [1, 2, 3, 5, 4, 6])
        self.assertEquals( \
            self.test_graph.recursive_depth_first_search(3, 4, []), \
                [3, 1, 2, 5, 4])
        self.assertEquals(
            self.test_graph.recursive_depth_first_search(1, 7, []), \
                None)

    def test_breadth_first_search(self):
        self.assertEquals(self.test_graph.breadth_first_search(1, 2), \
            [1, 2])
        self.assertEquals(self.test_graph.breadth_first_search(1, 6), \
            [1, 2, 3, 5, 4, 6])
        self.assertEquals(self.test_graph.breadth_first_search(3, 4), \
            [3, 1, 2, 5, 4])
        self.assertEquals(self.test_graph.breadth_first_search(5, 1), \
            [5, 4, 6, 2, 3, 1])
        self.assertEquals(self.test_graph.breadth_first_search(1, 7), \
            None)
