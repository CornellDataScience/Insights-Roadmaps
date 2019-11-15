
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
    dict = {'nodes': [], 'edges': [], 'weights': [], 'cars': []}
    for node in planarGraphResult.nodes:
        dict['nodes'].append({'lat': node.coordinates[0], 'lng': node.coordinates[1]})
        neighbors = node.get_neighbors()
        for neighbor_node in neighbors:
            dict['edges'].append({'lat': node.coordinates[0], 'lng': node.coordinates[1]})
            dict['edges'].append({'lat': neighbor_node.coordinates[0], 'lng': neighbor_node.coordinates[1]})
            dict['weights'].append(node.get_cost(neighbor_node))
    g = random_graph(30, 300)
    MAX_TIME = 10000
    s = Simulation(15, g.get_nodes()[:15], g.get_nodes()[-15:], g, MAX_TIME)
    s.start()
    dict['cars'] = s.run_webapp()
    #TODO: figure out way to get car path
    return dict

#ogging.basicConfig(level=logging.DEBUG)
def run_app():
    return render_template("index.html", cars=getPlanarGraphAsDict())

if __name__ == '__main__':
    app.run()
