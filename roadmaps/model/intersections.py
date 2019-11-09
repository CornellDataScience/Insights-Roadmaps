
from .graph import Edge
from .network import TrafficEdge, TrafficNode, TrafficNetwork

class Intersection(TrafficNode):

    def __init__(self, edge_mapping):
        super().__init__()
        
        self.paths = {} # self.paths maps parent nodes to a set-like list of valid neighbor nodes if their paths are connected internally by the intersection

    def map_nodes(self, parent: TrafficNode, neighbor: TrafficNode):
        """Create an internal path from the input node `parent` to the output node `neighbor`"""
        if neighbor in super().get_neighbors() and parent in super().get_parents():
            if parent in self.paths.keys():
                if neighbor not in self.paths[parent]: self.paths[parent].append(neighbor)
            else:
                self.paths[parent] = [neighbor]

    def get_neighbors(self, input_node):
        """Returns a list of nodes that are directly accessible from this node when coming from the node `input_node`"""
        return self.paths[input_node]

    def get_edges(self, input_node):
        """Returns a list of edges that are directly accessible from this node when coming from the node `input_node`"""
        return [self.neighbors[node] for node in self.paths[input_node]]


class LightIntersection(Intersection):

    def __init__(self):
        super().__init__()

    