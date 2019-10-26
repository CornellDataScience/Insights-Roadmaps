
from node import Node
from edge import Edge

class Graph:

    def __init__(self, nodes=[], edges=[]):
        """Represents a traffic network.
        Abstraction Function: The lists [N0, ..., Nn] and [E0, ..., En] represents a network of nodes N0 .. Nn and edges E0 .. En.
        Representation Invariant: There are no duplicate nodes or edges."""
        self.nodes = nodes
        self.edges = edges

    def add_edge(self, edge:Edge):
        """Adds `edge` and its associated node endpoints to the existing network"""
        start_node = edge.get_origin()
        end_node = edge.get_destination()
        if start_node not in self.nodes:
            self.nodes.append(start_node)
        if end_node not in self.nodes:
            self.nodes.append(end_node)  
        if edge not in self.edges:
            self.edges.append(edge)

    def get_shortest_path(self, start: Node, end: Node) -> list:
        """Returns a list of edges that constitutes the shortest path from `start` to `end`"""
        pass

