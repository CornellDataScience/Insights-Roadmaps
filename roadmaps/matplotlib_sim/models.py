import numpy as np

class RoadMap:
    def __init__(self,
                 init_state,
                 bounds = [-10, 10, -10, 10],
                 # bounds = [-2, 2, -2, 2],
                 size = 0.04):
        self.init_state = np.asarray(init_state, dtype=float)
        self.size = size
        self.state = self.init_state.copy()
        self.time_elapsed = 0
        self.bounds = bounds

    def step(self, dt):
        self.time_elapsed += dt
        self.state[:, :2] += dt * self.state[:, 2:]

        crossed_x1 = (self.state[:, 0] < self.bounds[0] + self.size)
        crossed_x2 = (self.state[:, 0] > self.bounds[1] - self.size)
        crossed_y1 = (self.state[:, 1] < self.bounds[2] + self.size)
        crossed_y2 = (self.state[:, 1] > self.bounds[3] - self.size)

        negative_x = (self.state[:, 0] < 0)
        positive_x = (self.state[:, 0] > 0)
        going_vertical = (abs(self.state[:, 3]) == 1)
        at_even = (self.state[:, 1] % 2 < 0.1)
        self.state[negative_x & going_vertical & at_even, 2] = 1
        self.state[positive_x & going_vertical & at_even, 2] = -1
        self.state[going_vertical & at_even, 3] = 0

        self.state[crossed_x1, 0] = self.bounds[0] + self.size
        self.state[crossed_x1, 2] = 0
        self.state[crossed_x1, 3] = -1
        self.state[crossed_x2, 0] = self.bounds[1] - self.size
        self.state[crossed_x2, 2] = 0
        self.state[crossed_x2, 3] = -1

        self.state[crossed_y1, 1] = self.bounds[2] + self.size
        self.state[crossed_y2, 1] = self.bounds[3] - self.size

        self.state[crossed_x1 | crossed_x2, 2] *= -1
        self.state[crossed_y1 | crossed_y2, 3] *= -1

        
