
import simpy
from collections import deque
from .models import Vehicle


class Simulation(object):
	"""
	simulation of arbitrary number of cars moving on an arbitrary graph to arbitrary places.
	"""
	def __init__(self, num_cars, sources, destinations, graph, max_time):
		self.max_time = max_time
		self.env = simpy.Environment()
		self.graph = graph
		self.cars = [Vehicle(self.env, deque(graph.get_path(sources[i], destinations[i]))) for i in range(num_cars)]


	def start(self):
		self.env.run(until=self.max_time)




