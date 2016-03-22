from __future__ import print_function
from sys import stdin
import unittest

""" Values are what the user sees, nodes are our internals """
class graph:

    class __node:
        def __init__(self, value):
            self.value = value
            self.edges = []

        def __str__(self):
            result = str(self.value)
            for edge in self.edges:
                result += "->" + str(edge.to_node.value) + \
                   '(' + str(edge.weight) + ')'
            return(result)

        def adjacent(self, other):
            for edge in self.edges:
                if edge.to_node.value == other.value:
                    return(True)

            return(False)

    class __edge:
        def __init__(self, to_node, weight):
            self.to_node = to_node
            self.weight = weight

    def __init__(self, nodes=None, adjacent=None):
        self.__nodes = []
        self.__edges = []

        if nodes:
            for node in nodes:
                self.add_node(node)

        if adjacent:
            for a in adjacent:
                self.add_edge(a[0], a[1], a[2])

    def __find(self, value):
        for node in self.__nodes:
            if value == node.value:
                return node
        return None

    def add_node(self, value):
        if not self.__find(value):
            self.__nodes.append(self.__node(value))

    def add_edge(self, to_value, weight):
        to_node = self.__find(to_value)

        if not to_node:
            to_node = self.__node()
            self.__nodes.append(to_node)

        if not self.adjacent(to_node):
            self.append(self.__edge(to_node, weight))
        if not to_node.adjacent(self):
            to_node.append(self.__edge(self, weight))

    def adjacent(self, from_value, to_value):
        return(self.__find(from_value).adjacent(self.__find(to_value)))

    ''' Add an edge from one node to another. If either nodes does not
    exist, add it. If either edge already exists, don't add a new edge. '''
    def add_edge(self, from_value, to_value, weight):
        from_node = self.__find(from_value)
        to_node = self.__find(to_value)

        if not from_node:
            from_node = self.__node(from_value)
            self.__nodes.append(from_node)
        if not to_node:
            to_node = self.__node(to_value)
            self.__nodes.append(to_node)

        if not from_node.adjacent(to_node):
            from_node.edges.append(self.__edge(to_node, weight))
        if not to_node.adjacent(from_node):
            to_node.edges.append(self.__edge(from_node, weight))

    def __len__(self): return(len(self.__nodes))

    def __str__(self):
        result = ""
        for node in self.__nodes:
            result += str(node) + '\n'
        return(result)

    def DFS(self, start_value, target_value):
        stack = [self.__find(start_value)]
        target = self.__find(target_value)
        visited = []

        while stack:
            current = stack.pop()
            visited.append(current)

            if current == target:
                return(map(lambda x: x.value, visited))

            for v in current.edges:
                if v.to_node not in visited:
                    stack.append(v.to_node)

        return None

    def rDFS(self, start_value, target_value, visited):
        start_node = self.__find(start_value)
        target_node = self.__find(target_value)

        visited.append(start_node)

        if start_node == target: return visited

        for v in self.adjacent(start):
            if v not in visited:
                return(self.rDFS(v, target, visited))

        return None

    def BFS(self, start_value, target_value):
        queue = [self.__find(start_value)]
        target = self.__find(target_value)
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

    def dijkstra(self, s):

        q = []
        for node in self.__nodes:
            node.__dist = float("inf")
            node.__prev = None
            q.append(node)

        source = self.__find(s)
        source.__dist = 0

        while q:
            min = float("inf")
            for node in q:
                if node.__dist < min:
                    min_node = node
                    min = node.__dist

            q.remove(min_node)
    
            for edge in min_node.edges:
                new_dist = min + edge.weight
                if new_dist < edge.to_node.__dist:
                    edge.to_node.__dist = new_dist
                    edge.to_node.__prev = min_node

        for node in self.__nodes:
            print(node.value, node.__dist)
            while node != source:
                print('\t', node.__prev.value)
                node = node.__prev

class test_graph(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(len(graph()), 0)

    def test_one(self):
        g = graph()
        g.add_node(1)
        self.assertEqual(len(g), 1)

    def test_duplicate(self):
        g = graph()
        g.add_node(1)
        g.add_node(1)
        self.assertEqual(len(g), 1)

    def test_two(self):
        g = graph()
        g.add_node(1)
        g.add_node(2)
        self.assertEqual(len(g), 2)

    def test_edge(self):
        g = graph()
        g.add_node(1)
        g.add_node(2)
        g.add_edge(1, 2, 3)
        self.assertEqual(str(g), '1->2(3)\n2->1(3)\n')

    def test_init(self):
        g = graph([1, 2], [(1, 2, 3), (2, 1, 3)])
        self.assertEqual(str(g), '1->2(3);2->1(3);')

    def test_init(self):
        g = graph(['Denver', 'Boston'], \
            [('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
        self.assertEqual(str(g),
            'Denver->Boston(1971.8)\nBoston->Denver(1971.8)\n')

    def test_are_adjacent(self):
        g = graph(['Denver', 'Boston'], \
            [('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
        self.assertTrue(g.adjacent('Denver', 'Boston'))

    def test_arent_adjacent(self):
        g = graph(['Denver', 'Boston', 'Milano'], \
            [('Denver', 'Boston', 1971.8), ('Boston', 'Denver', 1971.8)])
        self.assertFalse(g.adjacent('Denver', 'Milano'))

    def test_add_edges_without_nodes(self):
        g = graph([], [('Denver', 'Boston', 1971.8)])
        self.assertEqual(str(g), \
           'Denver->Boston(1971.8)\nBoston->Denver(1971.8)\n')

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
        g = graph([1, 2, 3, 4, 5, 6], \
            [(1,2,2), (1,3,1), (2,3,1), (2,4,1), (2,5,2), (3,5,5), \
             (4,5,3), (4,6,6), (5,6,1)])
        # g.dijkstra(1)
    def test_DFS(self):
        g = graph([1, 2, 3, 4, 5, 6], \
            [(1,2,1), (1,3,1), (2,3,1), (2,4,1), \
            (2,5,1), (3,5,1), (4,5,1), (4,6,1), (5,6,1)])
        self.assertEquals(g.DFS(1, 6), [1, 3, 5, 6])
        self.assertEquals(g.DFS(3, 4), [3, 5, 6, 4])
    def test_rDFS(self):
        g = graph([1, 2, 3, 4, 5, 6], \
            [(1,2,1), (1,3,1), (2,3,1), (2,4,1), \
            (2,5,1), (3,5,1), (4,5,1), (4,6,1), (5,6,1)])
        self.assertEquals(g.rDFS(1, 6, []), [1, 2, 3, 5, 4, 6])
        self.assertEquals(g.rDFS(3, 4, []), [3, 1, 2, 5, 4])
        self.assertEquals(g.rDFS(1, 7, []), None)
    def test_BFS(self):
        g = graph([1, 2, 3, 4, 5, 6], \
            [(1,2,1), (1,3,1), (2,3,1), (2,4,1), \
            (2,5,1), (3,5,1), (4,5,1), (4,6,1), (5,6,1)])
        self.assertEquals(g.BFS(1, 6), [1, 2, 3, 5, 4, 6])
        self.assertEquals(g.BFS(5, 1), [5, 4, 6, 2, 3, 1])
        self.assertEquals(g.BFS(1, 7), None)
    '''
    def test_short_BFS(self):
        g = graph([1, 2, 3, 4, 5, 6], \
            [(1,2,1), (1,3,1), (2,3,1), (2,4,1), \
            (2,5,1), (3,5,1), (4,5,1), (4,6,1), (5,6,1)])
        self.assertEquals(g.BFS(1, 2), [1, 2])
    '''

if '__main__' == __name__:
    g = graph()
    for line in stdin:
        a = line.strip().split(" ")
        g.add_edge(a[0], a[1], int(a[2]))
    print(g)
    g.dijkstra("Denver")
