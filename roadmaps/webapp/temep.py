
# Adds the root directiory to the sys path
# Allows importing any package defined in the root
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname( __file__ )))



from model.factory import planar_graph
from model.planar import PlanarEdge



def getPlanarGraphAsDict():
    planarGraphResult = planar_graph()
    dict = {'nodes': [], 'edges': [], 'weights': []}
    for node in planarGraphResult.nodes:
        dict['nodes'].append({'lat': node.coordinates[0], 'lng': node.coordinates[1]})
        neighbors = node.get_neighbors()
        for neighbor_node in neighbors:
            dict['edges'].append({'lat': node.coordinates[0], 'lng': node.coordinates[1]})
            dict['edges'].append({'lat': neighbor_node.coordinates[0], 'lng': neighbor_node.coordinates[1]})
            dict['weights'].append(PlanarEdge(node.coordinates, neighbor_node.coordinates).get_weight())
    #MAX_TIME = 10000
    #s = Simulation(15, g.get_nodes()[:15], g.get_nodes()[-15:], g, MAX_TIME)
    #s.start()
    #dict['cars'] = s.run_webapp()
    #TODO: figure out way to get car path
    return dict
