
from edge import Edge

class Node:
    """Represents a point in the network where the car is required to stop or make a decision on how to continue"""

    def __init__(self):
        self.in_edges = []
        self.out_edges = []

    def add_input_edge(self, edge):
        if edge not in self.in_edges:
            self.in_edges.append(edge)

    def add_output_edge(self, edge):
        if edge not in self.out_edges:
            self.out_edges.append(edge)

    def get_output_edges(self, edge) -> list:
        """Returns a list of edges a vehicle can take from this node"""
        return self.out_edges
