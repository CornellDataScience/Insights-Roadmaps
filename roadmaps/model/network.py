
from .graph import Edge, Node, Graph

class TrafficEdge(Edge):
    
    def __init__(self):
        super().__init__()


class TrafficNode(Node):
    
    def __init__(self):
        super().__init__()
        self.parents = {} # self.neighbors is a dictionary mapping {parent: edge}

    def get_parents(self):
        """Returns a list of nodes that directly connect to this node"""
        return list(self.parents.keys())

    def get_input_edges(self):
        """Returns a list of edges that directly connect to this node"""
        return list(self.parents.values()) 

    def connect_to(self, node, edge: Edge):
        super().connect_to(node, edge)
        node.parents[self] = edge


class TrafficNetwork(Graph):
    pass


