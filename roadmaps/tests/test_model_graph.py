
import unittest

from random import choice, randint

from model.graph import Edge, Node, Graph

class TestEdge(unittest.TestCase):

    def setUp(self):
        self.weight = 10
        self.e = Edge(self.weight)

    def test_traverse(self):
        self.assertEqual(self.e.traverse(0), self.weight)


class TestNode(unittest.TestCase):

    def setUp(self):
        self.n1, self.n2, self.e = Node(), Node(), Edge()
        self.n1.connect_to(self.n2, self.e)

    def test_traverse(self):
        self.assertEqual(self.n1.traverse(0), 0)
        self.assertEqual(self.n2.traverse(0), 0)

    def test_get_neighbors(self):
        self.assertEqual(self.n1.get_neighbors(), [self.n2])
        self.assertEqual(self.n2.get_neighbors(), [])

    def test_get_edges(self):
        self.assertEqual(self.n1.get_edges(), [self.e])
        self.assertEqual(self.n2.get_edges(), [])

    def test_get_parents(self):
        self.assertEqual(self.n1.get_parents(), [])
        self.assertEqual(self.n2.get_parents(), [self.n1])
    
    def test_get_input_edges(self):
        self.assertEqual(self.n1.get_input_edges(), [])
        self.assertEqual(self.n2.get_input_edges(), [self.e])

    def test_replace_edge(self):
        new_edge = Edge()
        self.n1.connect_to(self.n2, new_edge)

        self.assertEqual(self.n1.get_edges(), [new_edge])
        self.assertEqual(self.n2.get_input_edges(), [new_edge])

        

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
            a, b = missing_connections.pop(randint(0, len(missing_connections)-1))
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

        n1, n2, e = Node(), Node(), Edge()
        graph.connect(n1, n2, e)
        self.assertEqual(set((n1, n2)), set(graph.get_nodes()))
        self.assertEqual([e], graph.get_edges())

    def test_no_path(self):
        n1 = Node()
        self.assertEqual(self.graph.get_path(n1, self.nodes[0]), None)


if __name__ == '__main__':
    unittest.main()