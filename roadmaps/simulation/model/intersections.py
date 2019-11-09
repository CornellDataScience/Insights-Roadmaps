
from .graph import Edge, Node, Graph
from .network import TrafficEdge, TrafficNode, TrafficNetwork

class Intersection(Node):

    def __init__(self):
        super().__init__()
        self.paths = {} # self.paths maps parent nodes to a set-like list of valid neighbor nodes if their paths are connected internally by the intersection

    def get_neighbors(self, input_node):
        """Returns a list of nodes that are directly accessible from this node when coming from the node `input_node`"""
        return self.paths[input_node]

    def get_edges(self, input_node):
        """Returns a list of edges that are directly accessible from this node when coming from the node `input_node`"""
        return [self.neighbors[node] for node in self.paths[input_node]]

    def map_all_nodes(self):
        """Creates an internal path between all parent and neighbor nodes"""
        self.paths = {}
        for parent in self.get_parents():
            self.path[parent] = super().get_neighbors()

    def map_nodes(self, parent: TrafficNode, neighbor: TrafficNode):
        """Creates an internal path from the input node `parent` to the output node `neighbor`"""
        if neighbor in super().get_neighbors() and parent in self.get_parents():
            if parent in self.paths.keys():
                if neighbor not in self.paths[parent]: self.paths[parent].append(neighbor)
            else:
                self.paths[parent] = [neighbor]


class TrafficLight(Intersection):

    def __init__(self):
        super().__init__()
        self.sequence = [[()],[]] # self.sequence is a list of lists of pairs that represent paths from (parent, neighbor)

    def traverse(self, t):
        #TODO: redefine
        pass
    