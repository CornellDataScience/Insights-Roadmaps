
from random import choice, randint, uniform

from network.planar import PlanarNode, PlanarGraph

#if __name__ == '__main__':
def getPlanarGraph():
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

def getPlanarGraphAsDict():
    planarGraphResult = getPlanarGraph()
    dict = {'car1': []}
    for node in planarGraphResult.nodes:
        dict['car1'].append({'lat': node.coordinates[0], 'lng': node.coordinates[1]})
    return dict
