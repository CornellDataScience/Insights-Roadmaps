
# Adds the root directiory to the sys path
# Allows importing any package defined in the root
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname( __file__ )))



from model.factory import planar_graph
from model.planar import PlanarEdge



def getPlanarGraphAsDict():
    planarGraphResult = planar_graph()
    temp = [[40.752127, -73.993497], [40.752851, -73.993037], [40.753479, -73.992542], [40.754071, -73.992088], [40.754703, -73.991640], [40.755332, -73.991189], [40.754123, -73.988374], [40.753530, -73.988830], [40.752929, -73.989262], [40.752162, -73.987534], [40.751439, -73.987723], [40.750701, -73.987846]]
    dict = {'nodes': [], 'edges': [], 'weights': []}
    for i in range(len(temp) - 1):
        dict['nodes'].append({'lat': temp[i][0], 'lng': temp[i][1]})
        dict['edges'].append({'lat': temp[i][0], 'lng': temp[i][1]})
        dict['edges'].append({'lat': temp[i+1][0], 'lng': temp[i+1][1]})
        dict['weights'].append(PlanarEdge(temp[i], temp[i+1]).get_weight())
    #MAX_TIME = 10000
    #s = Simulation(15, g.get_nodes()[:15], g.get_nodes()[-15:], g, MAX_TIME)
    #s.start()
    #dict['cars'] = s.run_webapp()
    #TODO: figure out way to get car path
    return dict
