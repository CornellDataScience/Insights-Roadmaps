
from random import choice, randint

from network.planar import PlanarNode, PlanarGraph

if __name__ == '__main__':
    #
    # Generate a random directed planar graph
    #

    # Hyperparameters
    num_nodes = 20
    num_connections = 50
    max_weight = 100

    # Planar hyperparameters
    min_x, max_x = 0, 100
    min_y, max_y = 0, 100

    # Build connected nodes
    nodes = [PlanarNode((randint(min_x, max_x), randint(min_y, max_y)))]
    for i in range(num_nodes - 1):
        new_node = PlanarNode((randint(min_x, max_x), randint(min_y, max_y)))
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
    planar_network = PlanarGraph(nodes)