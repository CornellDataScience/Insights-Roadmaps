
 # Adds the root directiory to the sys path
 # Allows importing any package defined in the root
import os, sys
sys.path.insert(0, os.path.dirname( __file__ ))

# import webapp
# from simulation.vehicle import test
from model.factory import random_graph
# from model.graph import Graph, Edge, Node
# import model.intersections
from simpy_sim.controller import Simulation




if __name__ == '__main__':
    g = random_graph(20, 100)
    MAX_TIME = 10000

    s = Simulation(5, g.get_nodes()[:5], g.get_nodes()[-5:], g, MAX_TIME)
    s.start()
    