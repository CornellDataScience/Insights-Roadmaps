class Vehicle(object):
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
