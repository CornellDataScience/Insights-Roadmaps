import simpy
from collections import deque
# from models import Vehicle
from model.factory import random_graph
from model.graph import Graph, Edge, Node
import model.intersections



class Vehicle(object):
	"""
	Vehicle objects on the road.
	"""
	def __init__(self, env, path):
		self.env = env
		self.path = path
		self.action = env.process(self.run())

	def run(self):
		while self.path:
			if self.path[0].traverse() > 0:
			    print('Start waiting for a traffic light at %d' % self.env.now)
			    wait_duration = 5
			    yield self.env.process(self.wait(wait_duration))
			prev_node = self.path.popleft()
			if not self.path:
				print('Arrived at destination.')
				return
			edge = prev_node.get_edge(self.path[0])
			print('Start driving at %d' % self.env.now)
			drive_duration = edge.traverse(self.env.now)
			yield self.env.timeout(drive_duration)

	def wait(self, duration):
		yield self.env.timeout(duration)


g = random_graph(7, 20)


TOTAL_TIME = 200




env = simpy.Environment()
vehicle = Vehicle(env, deque(g.get_path(g.get_nodes()[0], g.get_nodes()[-1])))
env.run(until=TOTAL_TIME)