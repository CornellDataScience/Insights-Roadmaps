
from .graph import Edge, Node, Graph

class TrafficEdge(Edge):
    
    def __init__(self):
        super().__init__()
        self.start = None
        self.end = None

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def set_start(self, node):
        self.start = node
    
    def set_end(self, node):
        self.end = node


class TrafficNode(Node):
    
    def __init__(self):
        super().__init__()


    def traverse(self, t: int, parent) -> int:
        """Returns how long it will take to traverse this object, given the current time `t` and the previous node `parent`"""
        return 0

    def connect_to(self, node, edge: TrafficEdge):
        edge.set_start(self)
        edge.set_end(node)
        super().connect_to(node, edge)


class Network(Graph):
    pass


