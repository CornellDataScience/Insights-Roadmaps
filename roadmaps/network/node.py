
from .edge import Edge

class Node:

    def __init__(self):
        self.neighbors = {} # self.neighbors is a dictionary mapping {neighbor: edge}

    def get_neighbors(self):
        """Returns a list of nodes that are directly accessible from this node"""
        return self.neighbors.keys()

    def get_cost(self, node):
        """Returns the weight of the edge connecting `self` to `node`"""
        return self.neighbors[node].get_weight()

    def connect_to(self, node, edge: Edge):
        """Creates a new connection or replaces an existing one from `self` to `node` using `edge`"""
        self.neighbors[node] = edge

