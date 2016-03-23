from __future__ import print_function
from sys import stdin
import unittest

""" A more sophisticated graph class. Nodes can be any value, not just
    integers. Each node has a list of edges instead of the overall graph
    having single set of edges. """
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

        # Add edges in both directions.
        if not self.adjacent(to_node):
            self.append(self.__edge(to_node, weight))
        if not to_node.adjacent(self):
            to_node.append(self.__edge(self, weight))

    def adjacent(self, from_value, to_value):
        return(self.__find(from_value).adjacent(self.__find(to_value)))

    ''' Add an edge from one node to another. If either nodes does not
        exist, add it. If either edge already exists, don't add a new
        edge. '''
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

    def kruskal(self):
        forrest = []
        edges = []
        solution = []
        for node in self.__nodes:
            s = set()
            s.add(node)
            forrest.append(s)
            for edge in node.edges:
                edges.append((node, edge.to_node, edge.weight))

        while edges:

            # print(map(lambda y: map(lambda x: x.value, y), forrest))

            min_weight = float("inf")
            for edge in edges:
                if edge[2] < min_weight:
                    min_weight = edge[2]
                    min_edge = edge

            # print("min_edge:", min_edge[0].value, min_edge[1].value)
            edges.remove(min_edge)
            edges.remove((min_edge[1], min_edge[0], min_edge[2]))

            s0 = s1 = None
            for tree in forrest:
                if min_edge[0] in tree: s0 = tree
                if min_edge[1] in tree: s1 = tree
                if s0 and s1: break

            ''' If the two vertices are in two different trees. '''
            if s0 != s1:
                solution.append(min_edge)
                forrest.remove(s0)
                forrest.remove(s1)
                forrest.append(s0.union(s1))

            if len(solution) == len(self.__nodes) - 1: break
            # or: if len(forrest) == 1: break

        result = map(lambda x: str(x[0].value) + '->' + \
                    str(x[1].value), solution)
        return(result)

    def dijkstra(self, s):

        for node in self.__nodes:
            node.dist = float("inf")
            node.prev = None

        source = self.__find(s)
        source.dist = 0

        todo = set()
        todo.add(source)

        while todo:
            min_value = float("inf")
            for node in todo:
                if node.dist < min:
                    min_node = node
                    min_value = node.dist

            todo.remove(min_node)
    
            for edge in min_node.edges:
                new_dist = min_value + edge.weight
                if new_dist < edge.to_node.dist:
                    edge.to_node.dist = new_dist
                    edge.to_node.prev = min_node
                    todo.add(edge.to_node)

        result = []
        for node in self.__nodes:
            one = []
            one.append(node.dist)
            one.append(node.value)
            prev = node
            while prev != source:
                one.append(prev.prev.value)
                prev = prev.prev
            result.append(one)

        return(result)

class test_graph(unittest.TestCase):
    """
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

    """
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
        self.assertEquals(g.dijkstra(1), [[0, 1], [2, 2, 1], [1, 3, 1], \
            [3, 4, 2, 1], [4, 5, 2, 1], [5, 6, 5, 2, 1]])
    def test_kruskal(self):
        '''
        1--(7)--2--(8)--3
        |     /   \     |
       (5) (9)     (7) (5)
        | /           \ |
        4------(15)-----5
          \           / |
           (6)     (8) (9)
              \   /     |
                6 -(11)-7
        '''
        # FIXME
        g = graph([1,2,3,4,5,6,7], \
            [(1,2,7), (1,4,5), (2,3,8), (2,4,9), (2,5,7), (3,5,5), \
            (4,5,15), (4,6,6), (5,6,8), (5,7,9), (6,7,11)])
        self.assertEquals(g.kruskal(), \
            ['1->4', '3->5', '4->6', '1->2', '2->5', '5->7'])
    """
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
    def test_short_BFS(self):
        g = graph([1, 2, 3, 4, 5, 6], \
            [(1,2,1), (1,3,1), (2,3,1), (2,4,1), \
            (2,5,1), (3,5,1), (4,5,1), (4,6,1), (5,6,1)])
        self.assertEquals(g.BFS(1, 2), [1, 2])
    """

if '__main__' == __name__:
    g = graph()
    for line in stdin:
        a = line.strip().split(" ")
        g.add_edge(a[0], a[1], int(a[2]))
    result = g.dijkstra("Denver")
    for city in result:
        print(city[1], "is", city[0], 'miles from Denver, path:')
        for path in city[2:]:
            print("   ", path)
