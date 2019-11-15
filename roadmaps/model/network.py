
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
        self.paths = {} # self.paths maps parent nodes to a set-like list of valid neighbor nodes if their paths are connected internally by the intersection

    def traverse(self, t: int, behind, ahead) -> int:
        """Returns how long it will take to traverse this object, given the current time `t`, the previous node `behind`, and
           the destination node `ahead`"""
        return 0

    def get_neighbors(self, input_node):
        """Returns a list of nodes that are directly accessible from this node when coming from the node `input_node`"""
        return self.paths[input_node]

    def get_edges(self, input_node):
        """Returns a list of edges that are directly accessible from this node when coming from the node `input_node`"""
        return [self.neighbors[node] for node in self.paths[input_node]]

    def connect_to(self, node, edge: TrafficEdge):
        edge.set_start(self)
        edge.set_end(node)
        super().connect_to(node, edge)

    def map_all_paths(self):
        """Creates an internal path between all parent and neighbor nodes"""
        self.paths = {}
        for parent in self.get_parents():
            self.path[parent] = super().get_neighbors()

    def map_path(self, parent: TrafficNode, neighbor: TrafficNode):
        """Creates an internal path from the input node `parent` to the output node `neighbor`"""
        if neighbor in super().get_neighbors() and parent in self.get_parents():
            if parent in self.paths.keys():
                if neighbor not in self.paths[parent]: self.paths[parent].append(neighbor)
            else:
                self.paths[parent] = [neighbor]


class Network(Graph):
    
    def get_path(self, start: TrafficNode, end: TrafficNode) -> list:
        """Returns a list of nodes that constitute the optimal path from `start` to `end`.
            Path is optimal with regard to the traversal times of all nodes and edges in the path. 
            Returns None if a path does not exist.
            Caches calculated paths so they don't have to be recalculated again."""
    
        if (start, end) in self.computed_paths.keys():
            return self.computed_paths[(start, end)]

        frontier_nodes = [(start, 0)]   # stores a list of tuples of frontier nodes and their cost in the form (node, cost) sorted by cost
        closed_nodes = []               # stores a list of explored nodes
        parent_map = {start : None}     # maps nodes to their parent nodes in the search path in the form {node: parent}

        while len(frontier_nodes) > 0:
            node, cost = frontier_nodes.pop(0)
            closed_nodes.append(node)

            if node is end: # Backtrack
                path = []
                while node is not start:
                    path.insert(0, node)
                    node = parent_map[node]
                self.computed_paths[(start, end)] = path
                return path

            else: # Insert new frontier nodes
                neighbors = [x for x in list(set(node.get_neighbors(node)) - set(closed_nodes))]
                for neighbor in neighbors:
                    parent_map[neighbor] = node
                    neighbor_score = cost + node.traverse(cost) + node.get_edge(neighbor).traverse(cost + node.traverse(cost))

                    # Insert in sorted order - binary search to find insert index
                    i, j = 0, max(0, len(frontier_nodes) - 1)
                    while i < j:
                        k = (i + j) // 2
                        _, median = frontier_nodes[k]

                        if neighbor_score < median:
                            j = k - 1
                        elif neighbor_score > median:
                            i = k + 1
                        else:
                            i = j = k

                    frontier_nodes.insert(i, (neighbor, neighbor_score))

        return None