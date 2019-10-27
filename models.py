import numpy as np

class RoadMap:
    def __init__(self,
                 init_state,
                 bounds = [-10, 10, -10, 10],
                 #bounds = [-2, 2, -2, 2],
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

        self.state[crossed_x1, 0] = self.bounds[0] + self.size
        self.state[crossed_x2, 0] = self.bounds[1] - self.size

        self.state[crossed_y1, 1] = self.bounds[2] + self.size
        self.state[crossed_y2, 1] = self.bounds[3] - self.size

        self.state[crossed_x1 | crossed_x2, 2] *= -1
        self.state[crossed_y1 | crossed_y2, 3] *= -1

class Roads:
    def __init__(self, start_x, start_y, stop_x, stop_y, speed_limit):
        self.start_x = start_x
        self.start_y = start_y
        self.stop_x = stop_x
        self.stop_y = stop_y
        self.speed_limit = speed_limit

class Lights:
    def __init(x, y, red_duration, green_duration):
        self.x = x
        self.y = y
        self.red_duration = red_duration
        self.green_duration = green_duration

        #change color of traffic lights
        red_duration = 5
        green_duration = 10

        counter = 0
        self.time_elapsed += dt
        counter +=dt
        if counter <=green_duration:
            color = 'green'
        if counter >green_duration:
            color = 'red'
