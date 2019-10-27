
from edge import Edge

class Node:
    """Represents a point in the network where the car is required to stop or make a decision on how to continue"""

    def __init__(self):
        self.in_edges = []
        self.out_edges = []

    def add_input_edge(self, edge: Edge):
        if edge not in self.in_edges:
            self.in_edges.append(edge)

    def add_output_edge(self, edge: Edge):
        if edge not in self.out_edges:
            self.out_edges.append(edge)

    def get_edge_to(self, destination: Node) -> Edge:
        """Return the edge that connects this Node to the `destination` Node"""
        for edge in self.get_output_edges():
            if edge.get_destination() is destination:
                return edge
        return None

    def get_output_edges(self) -> list:
        """Returns a list of edges a that can be taken from this node"""
        return self.out_edges

    def get_output_nodes(self) -> list:
        """Returns a list of nodes that can be reached by traversing an outward edge from this node"""
        children = [edge.get_destination() for edge in self.get_output_edges()]
        return children