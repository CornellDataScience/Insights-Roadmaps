
 # Adds the root directiory to the sys path
 # Allows importing any package defined in the root
import os, sys
sys.path.insert(0, os.path.dirname( __file__ ))

from model.factory import random_graph
from simpy_sim.controller import Simulation


if __name__ == '__main__':
    g = random_graph(30, 300)
    MAX_TIME = 10000

    s = Simulation(15, g.get_nodes()[:15], g.get_nodes()[-15:], g, MAX_TIME)
    s.start()
    