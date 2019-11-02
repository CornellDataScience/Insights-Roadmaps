
from network.edge import Edge
from network.node import Node

class Graph:

    def __init__(self, nodes=[]):
        self.nodes = nodes

        self.computed_paths = {}    # This dictionary maps pairs of nodes to the path between them if it was computed previously

    def get_nodes(self) -> list:
        return self.nodes

    def get_path(self, start: Node, end: Node) -> list:
        """Returns a list of nodes that constitute the optimal path from `start` to `end`. Returns None if a path does not exist. """

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
                neighbors = [x for x in node.get_neighbors() if x not in closed_nodes]
                for neighbor in neighbors:
                    parent_map[neighbor] = node
                    neighbor_score = cost + node.get_cost(neighbor)

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


#{'Car1': {'coordinates': [(5, 6), (7, 8)], 'speed': 2}}
