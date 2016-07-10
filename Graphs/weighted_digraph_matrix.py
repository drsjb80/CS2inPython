from __future__ import print_function
import unittest

class WeightedDigraphMatrix(object):

    class Node(object):
        def __init__(self, value):
            # nested class variables are already hidden
            self.value = value

    def __init__(self, nodes=None, edges=None):
        self.nodes = []
        self.__edges = {}

        if nodes:
            for node in nodes:
                self.addnode(node)

        if edges:
            for edge in edges:
                self.add_edge(edge[0], edge[1], edge[2])

    def __len__(self): return len(self.nodes)

    def find(self, value):
        for node in self.nodes:
            if node.value == value:
                return node

        return None

    def addnode(self, value):
        if not self.find(value):
            self.nodes.append(self.Node(value))

    def add_edge(self, from_value, to_value, weight):
        """ Add an edge between two values. If the nodes
        for those values aren't already in the graph,
        add them. """

        if from_value not in self.nodes: self.addnode(from_value)
        if to_value not in self.nodes: self.addnode(to_value)

        if from_value not in self.__edges:
            self.__edges[from_value] = [[to_value, weight]]
        else:
            self.__edges[from_value].append([to_value, weight])

    def are_adjacent(self, value1, value2):
        if value1 in self.__edges:
            for i in self.__edges[value1]:
                if i[0] == value2:
                    return True

        return False

    def __str__(self):
        result = ""
        for i in self.nodes:
            result += str(i.value)
            try:
                if self.__edges[i.value]:
                    for j in self.__edges[i.value]:
                        result += '->' + str(j[0]) + '(' + str(j[1]) + ')'
            except KeyError:
                pass

            result += ';'
        return result

class TestWeightedDigraphMatrix(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(len(WeightedDigraphMatrix()), 0)

    def test_one(self):
        graph = WeightedDigraphMatrix()
        graph.addnode(1)
        self.assertEqual(len(graph), 1)

    def test_duplicate(self):
        graph = WeightedDigraphMatrix()
        graph.addnode(1)
        graph.addnode(1)
        self.assertEqual(len(graph), 1)

    def test_two(self):
        graph = WeightedDigraphMatrix()
        graph.addnode(1)
        graph.addnode(2)
        self.assertEqual(len(graph), 2)

    def test_edge(self):
        graph = WeightedDigraphMatrix()
        graph.addnode(1)
        graph.addnode(2)
        graph.add_edge(1, 2, 3)
        self.assertEqual(str(graph), '1->2(3);2;')

    def test_init_ints(self):
        graph = WeightedDigraphMatrix([1, 2], [(1, 2, 3), (2, 1, 3)])
        self.assertEqual(str(graph), '1->2(3);2->1(3);')

    def test_init(self):
        graph = WeightedDigraphMatrix(['Denver', 'Boston'], \
            [('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
        self.assertEqual(str(graph), \
            'Denver->Boston(1971.8);Boston->Denver(1971.8);')

    def test_are_adjacent(self):
        graph = WeightedDigraphMatrix(['Denver', 'Boston'], \
            [('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
        self.assertTrue(graph.are_adjacent('Denver', 'Boston'))

    def test_are_adjacent_more(self):
        graph = WeightedDigraphMatrix([], \
            [('Denver', 'Boston', 1971.8), ('Denver', 'Seattle', 1316.7)])
        self.assertTrue(graph.are_adjacent('Denver', 'Boston'))
        self.assertTrue(graph.are_adjacent('Denver', 'Seattle'))

    def test_arent_adjacent(self):
        graph = WeightedDigraphMatrix(['Denver', 'Boston', 'Milano'], \
            [('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
        self.assertFalse(graph.are_adjacent('Denver', 'Milano'))

    def test_add_edges_withoutnodes(self):
        graph = WeightedDigraphMatrix([], \
            [('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
        self.assertEqual(str(graph), \
            'Denver->Boston(1971.8);Boston->Denver(1971.8);')
