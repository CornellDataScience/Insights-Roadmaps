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
	def __init__(self, env, path, id):
		self.id = id
		self.env = env
		self.path = path
		self.action = env.process(self.run())

	def run(self):
		print('Car #%d began its trip!' % self.id)
		while self.path:
			wait_time = self.path[0].traverse(self.env.now)
			if wait_time > 0:
			    print('Car #%d started waiting for a traffic light at time %d.' % (self.id, self.env.now))
			    yield self.env.process(self.wait(wait_time))
			prev_node = self.path.popleft()
			print('Car #%d passed an intersection.' % self.id)
			if not self.path:
				print('Car #%d arrived at its destination.' % self.id)
				return
			edge = prev_node.get_edge(self.path[0])
			print('Car #%d continued driving at %d' % (self.id, self.env.now))
			drive_duration = edge.traverse(self.env.now)
			yield self.env.timeout(drive_duration)

	def wait(self, duration):
		yield self.env.timeout(duration)
