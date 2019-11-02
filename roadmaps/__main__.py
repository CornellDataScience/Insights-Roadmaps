
from random import choice, randint

from network.edge import Edge
from network.node import Node
from network.graph import Graph

if __name__ == '__main__':
    #
    # Generate a random directed graph
    #

    # Hyperparameters
    num_nodes = 20
    num_connections = 50
    max_weight = 100

    # Build connected nodes
    nodes = [Node()]
    for i in range(num_nodes - 1):
        new_node = Node()
        old_node = choice(nodes)
        old_node.connect_to(new_node, Edge(randint(0, max_weight)))
        nodes.append(new_node)
    
    # Create more connections
    for i in range(num_connections - (num_nodes - 1)):
        a, b = choice(nodes), choice(nodes)
        i, max_iterations = 0, 100
        while i < max_iterations and (a is b or b in a.get_neighbors() or a in b.get_neighbors()):
            a, b = choice(nodes), choice(nodes)
            i += 1
        a.connect_to(b, Edge(randint(0, max_weight)))

    # A Graph object that represents the traffic network
    network = Graph(nodes)
    
    start, end = nodes[0], choice(nodes)
    path = network.get_path(start, end)
    print(path)