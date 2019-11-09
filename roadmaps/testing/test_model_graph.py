
import unittest

from random import choice, randint
from time import time_ns as now

from model.graph import Edge, Node, Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        # Hyperparameters
        num_nodes = 100
        num_edges = 500
        weight_max = 100

        self.edges = []
        self.nodes = [Node()]

        # Build connected nodes
        for _ in range(num_nodes - 1):
            new = Node()
            self.nodes.append(new)
            old = choice(self.nodes)

            edge = Edge(randint(0, weight_max))
            self.edges.append(edge)
            old.connect_to(new, edge)
        
        # Add random connections
        missing_connections = [(n1, n2) for n1 in self.nodes for n2 in list(set(self.nodes) - set(n1.get_neighbors()))]
        for i in range(num_edges - (num_nodes - 1)):
            a, b = missing_connections.pop(randint(0, len(missing_connections)))
            edge = Edge(randint(0, weight_max))
            self.edges.append(edge)
            a.connect_to(b, edge)

        self.edges = list(set(self.edges))
        self.graph = Graph(self.nodes)
    
    def test_get_nodes(self):
        self.assertEqual(set(self.nodes), set(self.graph.get_nodes()))

    def test_get_edges(self):
        self.assertEqual(set(self.edges), set(self.graph.get_edges()))

    def test_connect(self):
        graph = Graph()
        self.assertEqual([], graph.get_nodes())
        self.assertEqual([], graph.get_edges())

        n1, n2, e = Node(), Node(), Edge(1)
        graph.connect(n1, n2, e)
        self.assertEqual(n1.get_neighbors(), [n2])
        self.assertEqual(n1.get_edges(), [e])
        self.assertEqual(set((n1, n2)), set(graph.get_nodes()))
        self.assertEqual([e], graph.get_edges())


if __name__ == '__main__':
    unittest.main()