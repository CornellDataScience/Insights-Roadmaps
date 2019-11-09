
import unittest

from random import choice, randint
from time import time_ns as now

from model.graph import Edge, Node, Graph
from model import factory

class TestGraph(unittest.TestCase):

    def test_random_graph(self):
        nodes, edges, max_weight = 100, 200, 10
        random_graph = factory.random_graph(nodes, edges, max_weight)
        self.assertEqual(nodes, len(set(random_graph.get_nodes())))
        self.assertEqual(edges, len(set(random_graph.get_edges())))

if __name__ == '__main__':
    unittest.main()