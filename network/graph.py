
from network.node import Node
from network.edge import Edge

class PathNode(Node):

    def __init__(self, node: Node, parent: PathNode):
        self.node = node
        self.parent = parent

    def backtrack(self):
        return self.parent

class Graph:

    def __init__(self, nodes=[], edges=[]):
        """Represents a traffic network.
        Abstraction Function: The lists [N0, ..., Nn] and [E0, ..., En] represents a network of nodes N0 .. Nn and edges E0 .. En.
        Representation Invariant: There are no duplicate nodes or edges."""
        self.nodes = nodes
        self.edges = edges

    def get_nodes(self) -> list:
        return self.nodes

    def get_edges(self) -> list:
        return self.edges

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
        
        frontier_edges = start.get_output_edges()
        frontier_nodes = []
        for edge in frontier_edges:
            node = PathNode(edge.get_destination(), start)
            frontier_nodes.append(node)

        



