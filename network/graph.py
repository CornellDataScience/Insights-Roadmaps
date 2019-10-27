
class Edge:
    """Represents a road in the network that a car must traverse in its entirety."""

    def __init__(self, start, end, weight: int, speed: int):
        self.start = start
        self.end = end
        self.weight = weight
        self.speed_limit = speed
        
        # Adds the edge to the node endpoints
        self.start.add_output_edge(self)
        self.end.add_input_edge(self)

    def get_origin(self):
        """Returns the node from which this edge originates"""
        return self.start

    def get_destination(self):
        """Returns the node at the endpoint of traversing this edge"""
        return self.end

    def get_time(self):
        """Returns the traversal time of this edge using the length and speed limit"""
        return self.weight / self.speed_limit

    def get_speed(self):
        """Returns the speed a vehicle travels on this edge"""
        return self.speed_limit

    def get_weight(self):
        """Returns the length of this edge"""
        return self.weight

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

    def get_edge_to(self, destination) -> Edge:
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
        
        frontier_nodes = [(start, 0)]   # stores a list of tuples of frontier nodes and their weight in the form (Node, weight)
        closed_nodes = []               # stores a list of explored nodes
        node_map = {start : None}       # stores key-value pairs of Node objects to their parent Node objects

        while len(frontier_nodes) > 0:
            node, weight = frontier_nodes.pop(0)
            closed_nodes.append(node)

            if node is end:
                path = []
                while node is not start:
                    parent = node_map[node]
                    edge = parent.get_edge_to(node)
                    path.insert(0, edge)
                    node = parent
                return path

            else:
                for edge in node.get_output_edges():
                    frontier_node = edge.get_destination()
                    if frontier_node not in closed_nodes:
                        node_map[frontier_node] = node
                        frontier_weight = weight + edge.get_time()

                        # Insert frontier node into list in sorted order
                        i = 0
                        while i < len(frontier_nodes):
                            _, compare_weight = frontier_nodes[i]
                            if frontier_weight < compare_weight:
                                break
                            i += 1
                        frontier_nodes.insert(i, (frontier_node, frontier_weight))

if __name__ == '__main__':

    # 
    # 0 -> 1 -> 2
    #      |
    #      V
    #      3

    nodes = [Node(), Node(), Node(), Node()]

    edge0 = Edge(nodes[0], nodes[1], weight=10, speed=5)
    edge1 = Edge(nodes[1], nodes[2], weight=200, speed=10)
    edge2 = Edge(nodes[3], nodes[2], weight=10, speed=15)
    edge3 = Edge(nodes[1], nodes[3], weight=30, speed=15)

    edges = [edge0, edge1, edge2, edge3]
    graph = Graph(nodes, edges)

    print(edges)
    print(graph.get_shortest_path(nodes[0], nodes[2]))