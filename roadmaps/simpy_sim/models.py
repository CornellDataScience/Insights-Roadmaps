class Vehicle_deprecated(object):
	"""
	Vehicle objects on the road.
	"""
	def __init__(self, env):
		self.env = env
		self.action = env.process(self.run())

	def run(self):
		while True:
			print('Start waiting for a traffic light at %d' % self.env.now)
			wait_duration = 5
			yield self.env.process(self.wait(wait_duration))
			print('Start driving at %d' % self.env.now)
			drive_duration = 7
			yield self.env.timeout(drive_duration)

	def wait(self, duration):
		yield self.env.timeout(duration)


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
			if self.path[0].traverse(self.env.now) > 0:
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
