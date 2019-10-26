
from node import Node

class Edge:
    """Represents a road in the network that a car must traverse in its entirety."""

    def __init__(self, start: Node, end: Node, distance: int, speed: int):
        self.start = start
        self.end = end
        self.distance = distance
        self.speed_limit = speed
        
        # Adds the edge to the node endpoints
        self.start.add_output_edge(self)
        self.end.add_input_edge(self)

    def get_origin(self):
        """Returns the node from which this edge originates"""
        return self.start

    def get_destination(self):
        """Returns the node at the endpoint of traversing this edge"""
        return self.end

    def get_time(self):
        """Returns the traversal time of this edge using the length and speed limit"""
        return self.distance / self.speed_limit

    def get_speed(self):
        """Returns the speed a vehicle travels on this edge"""
        return self.speed_limit

    def get_distance(self):
        """Returns the length of this edge"""
        return self.distance