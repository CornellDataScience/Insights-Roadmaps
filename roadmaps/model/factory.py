
from random import randint, choice
from .graph import Edge, Node, Graph
from .network import TrafficEdge, TrafficNode, Network
from .intersections import TrafficLight

def random_graph(n: int, v: int, max_edge_weight: int = 10, directed: bool = True) -> Graph:
    """Generates a random graph with `n` nodes and at most `v` edges"""

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


def random_network(n: int, v: int, max_edge_weight: int = 10, directed: bool = True) -> Graph:
    """Generates a random network with `n` nodes and at most `v` edges"""

    # Build connected nodes
    nodes = [TrafficNode()]
    for _ in range(n - 1):
        new = TrafficNode() if randint(0, 1) == 0 else TrafficLight()   # Generates traffic light with 0.5 probability
        nodes.append(new)
        old = choice(nodes)

        weight = randint(0, max_edge_weight) 
        old.connect_to(new, TrafficEdge(weight))
        if not directed:
            new.connect_to(old, TrafficEdge(weight))
    
    # Add random connections
    missing_connections = [(n1, n2) for n1 in nodes for n2 in list(set(nodes) - set(n1.get_neighbors()))]
    for i in range(v - (n - 1)):
        a, b = missing_connections.pop(randint(0, len(missing_connections)-1))
        weight = randint(0, max_edge_weight) 
        a.connect_to(b, TrafficEdge(weight))
        if not directed:
            b.connect_to(a, TrafficEdge(weight))

    # Return the graph
    return Network(nodes)


# TODO: make better... MUCH better (dont use this method except for webapp)
def planar_graph():
    #
    # Generate a random directed planar graph
    #

    # Hyperparameters
    num_nodes = 20
    num_connections = 50
    max_weight = 100

    # Planar hyperparameters
    min_x, max_x = 42.44, 42.45
    min_y, max_y = -76.49, -76.5

    # Build connected nodes
    nodes = [PlanarNode((uniform(min_x, max_x), uniform(min_y, max_y)))]
    for i in range(num_nodes - 1):
        new_node = PlanarNode((uniform(min_x, max_x), uniform(min_y, max_y)))
        old_node = choice(nodes)
        old_node.connect_to(new_node)
        nodes.append(new_node)

    # Create more connections
    for i in range(num_connections - (num_nodes - 1)):
        a, b = choice(nodes), choice(nodes)
        i, max_iterations = 0, 100
        while i < max_iterations and (a is b or b in a.get_neighbors() or a in b.get_neighbors()):
            a, b = choice(nodes), choice(nodes)
            i += 1
        a.connect_to(b)

    # A PlanarGraph object that represents the traffic network
    return PlanarGraph(nodes)