from .graph import Edge, Node, Graph

import math
import sys

class PlanarEdge(Edge):

    def __init__(self, start_coordinates: tuple, end_coordinates: tuple):
        self.start = start_coordinates
        self.end = end_coordinates
        self.weight = math.sqrt((self.end[0] - self.start[0])**2 + (self.end[1] - self.start[1])**2)

    def get_weight(self):

        return weight
        # return sum([((x1 - x2) ** 2) for x1, x2 in zip(list(self.start), list(self.end))])

    def get_start(self) -> tuple:
        return self.start

    def get_end(self) -> tuple:
        return self.end


class PlanarNode(Node):

    def __init__(self, coordinates: tuple):
        super().__init__()
        self.coordinates = coordinates

    def get_coordinates(self):
        return self.coordinates

    def connect_to(self, node):
        edge = PlanarEdge(self.get_coordinates(), node.get_coordinates())
        super().connect_to(node, edge)


class PlanarGraph(Graph):

    def connect(self, start: PlanarNode, end: PlanarNode):
        return start.connect_to(end)
