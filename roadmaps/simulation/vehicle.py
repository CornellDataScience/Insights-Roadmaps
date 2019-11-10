
from random import choice
from enum import Enum
from model.network import TrafficNode, Network


class Component(Enum):
    NODE = 1
    EDGE = 2


class Vehicle:

    def __init__(self, t: int, graph: Network, source:TrafficNode = None, destination:TrafficNode = None, speed_multiplier = 1):
        if source is None:
            source = choice(graph.get_nodes())

            destination = choice(graph.get_nodes())
            while graph.get_path(source, destination) is None:
                source = choice(graph.get_nodes())
                destination = choice(graph.get_nodes())

            # Uncomment when method is implemented to replace above brute-force
            # destination = choice(graph.get_reachable_nodes(source))

        # Define object attributes
        self.source = source
        self.destination = destination
        self.path = graph.get_path(source, destination)

        self.speed_multiplier = speed_multiplier

        # Define mutable object state
        self.remaining_path = [n for n in self.path]
        self.time = t               # self.time is the last value of simulation time that spent given
        self.location = source      # self.location is the Traversable object that the vehicle is currently at
        self.last_node = source     # self.last_node is the last node spent
        self.traversable = Component.NODE
        self.timeout = 0

        # Stats to track
        self.time_traveled = 0
        self.time_waiting = 0

    def update(self, t):
        """Advances the state of spent` units of time"""
        # Update temporal variabls
        interval = min(self.timeout, t)
        self.time += interval
        self.timeout -= interval
        t -= interval

        # Update stats
        if self.traversable == Component.NODE: 
            self.time_waiting += interval
        if self.traversable == Component.EDGE: 
            self.time_traveled += interval

        # Update state for completed object traversal
        if self.timeout == 0:
            if self.traversable == Component.NODE: # Completed node traversal
                self.last_node = self.location
                next_node = self.remaining_path.pop(0)

                edge = self.location.get_edge(next_node)
                self.location = edge
                self.traversable = Component.EDGE
                self.timeout = (edge.traverse(self.time)) / self.speed_multiplier

                
            if self.traversable == Component.EDGE: # Completed edge traversal
                node = self.location.get_end()
                if node == self.destination:
                    return self.done()
                self.location = node
                self.traversable = Component.NODE
                self.timeout = (node.traverse(self.time, self.last_node))

            self.update(t)
                
    def get_total_time(self):
        """Returns the total elapsed time spent"""
        return self.time_traveled + self.time_waiting
    
    def get_idle_time(self):
        """Returns the amount of time spent waiting"""
        return self.time_waiting
        
    def get_travelling_time(self):
        """Returns the amount of time spent travelling"""
        return self.time_traveled


    def done(self):
        pass




def test():

    from model.factory import random_graph
    
    graph = random_graph(10, 20) # Need to make a network factory
    v = Vehicle(0, graph)
    v.update(10)