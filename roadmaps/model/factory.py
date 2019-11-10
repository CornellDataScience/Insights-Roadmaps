
from random import randint, choice
from .graph import Edge, Node, Graph

def random_graph(n: int, v: int, max_edge_weight: int = 10, directed: bool = True) -> Graph:
    """Generates a random graph with n nodes and at most v edges"""

    # Build connected nodes
    nodes = [Node()]
    for _ in range(n - 1):
        new = Node()
        nodes.append(new)
        old = choice(nodes)

        weight = randint(0, max_edge_weight) 
        old.connect_to(new, Edge(weight))
        if not directed:
            new.connect_to(old, Edge(weight))
    
    # Add random connections
    missing_connections = [(n1, n2) for n1 in nodes for n2 in list(set(nodes) - set(n1.get_neighbors()))]
    for i in range(v - (n - 1)):
        a, b = missing_connections.pop(randint(0, len(missing_connections)-1))
        weight = randint(0, max_edge_weight) 
        a.connect_to(b, Edge(weight))
        if not directed:
            b.connect_to(a, Edge(weight))

    # Return the graph
    return Graph(nodes)