
class Edge:
    """Represents a road in the network that a car must traverse in its entirety."""

    def __init__(self, start, stop, distance, speed):
        self.start = start
        self.stop = stop
        self.distance = distance
        self.speed_limit = speed
