
import abc

"""Contains the base Edge, Node, and Graph classes"""

class Traversable(abc.ABC):

    @abc.abstractmethod
    def traverse(self, t: int) -> int:
        """Returns how long it will take to traverse this object, given the current time `t`"""
        pass

class Edge(Traversable):

    def __init__(self, weight=1):
        self.weight = weight

    def traverse(self, t):
        return self.weight


class Node(Traversable):

    def __init__(self):
        self.neighbors = {} # self.neighbors is a dictionary mapping {neighbor: edge}
        self.parents = {} # self.parents is a dictionary mapping {parent: edge}

    def traverse(self, t):
        return 0

    def get_neighbors(self) -> list:
        """Returns a list of nodes that are directly accessible from this node"""
        return list(self.neighbors.keys())

    def get_edges(self) -> list:
        """Returns a list of edges that are directly accessible from this node"""
        return list(self.neighbors.values())

    def get_parents(self):
        """Returns a list of nodes that directly connect to this node"""
        return list(self.parents.keys())

    def get_input_edges(self):
        """Returns a list of edges that directly connect to this node"""
        return list(self.parents.values()) 

    def get_edge(self, node):
        """Returns the edge connecting `self` to `node`"""
        return self.neighbors[node]

    def connect_to(self, node, edge: Edge):
        """Creates a new connection or replaces an existing one from `self` to `node` using `edge`"""
        self.neighbors[node] = edge
        node.parents[self] = edge


class Graph:

    def __init__(self, nodes=[]):
        self.nodes = nodes

        self.computed_paths = {}    # This dictionary maps pairs of nodes to the path between them if it was computed previously
        self.connected_nodes = {}   # This dictionary maps nodes to a list of nodes they are connected to if it was computed previously
        # TODO: hash code for nodes to verify most up-to-date computed paths and connected_nodes

    def get_nodes(self) -> list:
        return self.nodes

    def get_edges(self) -> list:
        return list({edge : None for node in self.nodes for edge in node.get_edges()}.keys())

    def get_path(self, start: Node, end: Node) -> list:
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
                neighbors = [x for x in list(set(node.get_neighbors()) - set(closed_nodes))]
                for neighbor in neighbors:
                    parent_map[neighbor] = node
                    neighbor_score = cost + node.traverse(cost) + node.get_edge(neighbor).traverse(node.traverse(cost))

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

    def get_reachable_nodes(self, source: Node):
        """Returns a list of nodes that `source` is connected to.
           Caches calculated connected nodes so they don't have to be recalculated again."""
        if source in self.connected_nodes.keys():
            return self.connected_nodes[source]

        frontier_nodes = [source]   # stores a list of tuples of frontier nodes and their cost in the form (node, cost) sorted by cost
        closed_nodes = []           # stores a list of explored nodes

        while len(frontier_nodes) > 0:
            node = frontier_nodes.pop()
            closed_nodes.append(node)

            for neighbor in node.get_neighbors():
                if neighbor not in closed_nodes and neighbor not in frontier_nodes:
                    frontier_nodes.append(neighbor)
            
        self.connected_nodes[source] = closed_nodes
        return closed_nodes

    def connect(self, start: Node, end: Node, edge: Edge):
        """Connects `edge` from `start` to `edge`"""
        self.nodes = list(set(self.nodes + [start, end]))
        return start.connect_to(end, edge)