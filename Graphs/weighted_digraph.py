from __future__ import print_function
import unittest

class WeightedDigraph(object):

    class _edge(object):
        def __init__(self, to_node, weight):
            self.to_node = to_node
            self.weight = weight

        def __str__(self):
            return 'To:' + str(self.to_node.value) + \
                ', weight:' + str(self.weight)

    class _node(object):
        def __init__(self, value):
            self.value = value
            self.edges = []

        def __str__(self):
            result = str(self.value)
            for edge in self.edges:
                result += "->" + str(edge.to_node.value) + \
                    "(" + str(edge.weight) + ")"
            return result

        def add_edge(self, to_node, weight):
            if not self.is_adjacent(to_node):
                self.edges.append(WeightedDigraph._edge(to_node, weight))

        def remove_edge(self, to_node):
            for edge in self.edges:
                if edge.to_node == to_node:
                    self.edges.remove(edge)

        def is_adjacent(self, node):
            for edge in self.edges:
                if edge.to_node == node:
                    return True
            return False

        def get_edge(self, node):
            for edge in self.edges:
                if edge.to_node == node:
                    return edge
            return None

    def __init__(self, nodes=None, edges=None):
        self._nodes = []

        if nodes: self.add_nodes(nodes)
        if edges: self.add_edges(edges)

    def __len__(self): return len(self._nodes)

    def __str__(self):
        result = ""
        for node in self._nodes:
            result += str(node) + '\n'
        return result

    def get_nodes(self): return self._nodes[:]

    def find(self, value):
        for node in self._nodes:
            if node.value == value:
                return node

        return None

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def add_node(self, value):
        if not self.find(value):
            self._nodes.append(self._node(value))

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1], edge[2])

    def add_edge(self, from_value, to_value, weight):
        """ Add an edge between two values. If the nodes
        for those values aren't already in the graph,
        add those. """

        from_node = self.find(from_value)
        to_node = self.find(to_value)

        if not from_node:
            self.add_node(from_value)
            from_node = self.find(from_value)
        if not to_node:
            self.add_node(to_value)
            to_node = self.find(to_value)

        from_node.add_edge(to_node, weight)

    def remove_edge(self, from_value, to_value):
        from_node = self.find(from_value)
        to_node = self.find(to_value)

        from_node.remove_edge(to_node)

    def are_adjacent(self, value1, value2):
        return self.find(value1).is_adjacent(self.find(value2))

class WeightedGraph(WeightedDigraph):
    ''' A graph instead of a digraph. '''
    def add_edge(self, from_value, to_value, weight):
        from_node = self.find(from_value)
        to_node = self.find(to_value)

        if not from_node:
            self.add_node(from_value)
            from_node = self.find(from_value)
        if not to_node:
            self.add_node(to_value)
            to_node = self.find(to_value)

        from_node.add_edge(to_node, weight)
        to_node.add_edge(from_node, weight)

    def remove_edge(self, from_value, to_value):
        from_node = self.find(from_value)
        to_node = self.find(to_value)

        from_node.remove_edge(to_node)
        to_node.remove_edge(from_node)

class TestWeightedDigraph(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(len(WeightedDigraph()), 0)

    def test_one(self):
        graph = WeightedDigraph()
        graph.add_node(1)
        self.assertEqual(len(graph), 1)

    def test_duplicate(self):
        graph = WeightedDigraph()
        graph.add_node(1)
        graph.add_node(1)
        self.assertEqual(len(graph), 1)

    def test_two(self):
        graph = WeightedDigraph()
        graph.add_node(1)
        graph.add_node(2)
        self.assertEqual(len(graph), 2)

    def test_edge(self):
        graph = WeightedDigraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(1, 2, 3)
        self.assertEqual(str(graph), '1->2(3)\n2\n')

    def test_adding_ints(self):
        graph = WeightedDigraph([1, 2], [(1, 2, 3), (2, 1, 3)])
        self.assertEqual(str(graph), '1->2(3)\n2->1(3)\n')

    def test_adding_strings(self):
        graph = WeightedDigraph(['Denver', 'Boston'], \
            [('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
        self.assertEqual(str(graph), \
            'Denver->Boston(1971.8)\nBoston->Denver(1971.8)\n')

    def test_are_adjacent(self):
        graph = WeightedDigraph()
        graph.add_nodes(['Denver', 'Boston'])
        graph.add_edges([('Denver', 'Boston', 1971.8), \
            ('Boston', 'Denver', 1971.8)])
        self.assertTrue(graph.are_adjacent('Denver', 'Boston'))

    def test_arent_adjacent(self):
        graph = WeightedDigraph()
        graph.add_nodes(['Denver', 'Boston', 'Milano'])
        graph.add_edges([('Denver', 'Boston', 1971.8), \
            ('Boston', 'Denver', 1971.8)])
        self.assertFalse(graph.are_adjacent('Denver', 'Milano'))

    def test_arent_adjacent_directed(self):
        graph = WeightedDigraph()
        graph.add_edges([('Denver', 'Boston', 1971.8)])
        self.assertFalse(graph.are_adjacent('Denver', 'Milano'))
        self.assertFalse(graph.are_adjacent('Boston', 'Denver'))
        self.assertTrue(graph.are_adjacent('Denver', 'Boston'))

    def test_arent_adjacent_undirected(self):
        graph = WeightedGraph()
        graph.add_edges([('Denver', 'Boston', 1971.8)])
        self.assertTrue(graph.are_adjacent('Boston', 'Denver'))
        self.assertTrue(graph.are_adjacent('Denver', 'Boston'))

    def test_add_edges_without_nodes(self):
        graph = WeightedDigraph()
        graph.add_edges([('Denver', 'Boston', 1971.8), \
            ('Boston', 'Denver', 1971.8)])
        self.assertEqual(str(graph), \
            'Denver->Boston(1971.8)\nBoston->Denver(1971.8)\n')
