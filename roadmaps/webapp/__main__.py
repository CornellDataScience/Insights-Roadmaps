 
# Adds the root directiory to the sys path
# Allows importing any package defined in the root
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname( __file__ )))

from flask import Flask, render_template

from model.factory import planar_graph

app = Flask(__name__)

@app.route('/')

def getPlanarGraphAsDict():
    planarGraphResult = planar_graph()
    dict = {'car1': [], 'car1edges': [], 'car1weights': []}
    for node in planarGraphResult.nodes:
        dict['car1'].append({'lat': node.coordinates[0], 'lng': node.coordinates[1]})
        neighbors = node.get_neighbors()
        for neighbor_node in neighbors:
            dict['car1edges'].append({'lat': node.coordinates[0], 'lng': node.coordinates[1]})
            dict['car1edges'].append({'lat': neighbor_node.coordinates[0], 'lng': neighbor_node.coordinates[1]})
            dict['car1weights'].append(node.get_cost(neighbor_node))
        '''for j in range(len)
        if (i == len(planarGraphResult.nodes) - 1):
            dict['car1weights'].append(planarGraphResult.nodes[i].get_cost(planarGraphResult.nodes[0]))
        else:
            dict['car1weights'].append(planarGraphResult.nodes[i].get_cost(planarGraphResult.nodes[i+1]))'''
    return dict

#ogging.basicConfig(level=logging.DEBUG)
def run_app():
    #new_dict={'car1': [{'lat': 42.436483, 'lng': -76.507386}, {'lat': 42.438501, 'lng': -76.464116}, {'lat': 42.447367, 'lng': -76.470143}]}
    temp_planar_graph = getPlanarGraphAsDict()
    return render_template("index.html", cars=temp_planar_graph)

if __name__ == '__main__':
    app.run()
