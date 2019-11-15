
import simpy
from collections import deque, defaultdict
from .models import Vehicle


class Simulation(object):
	"""
	simulation of arbitrary number of cars moving on an arbitrary graph to arbitrary places.
	"""
	def __init__(self, num_cars, sources, destinations, graph, max_time):
		self.max_time = max_time
		self.env = simpy.Environment()
		self.graph = graph
		self.cars = [Vehicle(self.env, deque(graph.get_path(sources[i], destinations[i])), i) for i in range(num_cars)]
		self.count = 0
		self.total_q_length = 0
		self.queues = defaultdict(list)

	def monitor(self):
		while True:
			self.count += 1
			self.total_q_length += sum(map(len, self.queues.values()))
			yield self.env.timeout(1.0)


	def start(self):
		self.env.process(self.monitor())
		self.env.run(until=self.max_time)
		print('===== Process Statistics =====')
		print('Average length of queues at intersections is %d' % (self.total_q_length / self.count))


	





