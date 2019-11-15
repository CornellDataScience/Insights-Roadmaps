
from .graph import Edge, Node, Graph
from .network import TrafficEdge, TrafficNode, Network

class TrafficLight(TrafficNode):

    def __init__(self):
        super().__init__()

        # Traffic lights are implemented by a sequence of sets of paths that can be 'active' together.
        # Active paths allow immediate traversal (green) while inactive paths stop traversal (red).
        # The set of paths that are 'active' cycles through a sequence defined by self.path_sequence
        # The time that a set of paths is 'active' is given by the parallel list self.
        # Representation Invariant: self.path_sequence and self.time_sequence must be the same length
        self.path_sequence = [] # list of list of tuple of TrafficNode objects ... I know right
        self.time_sequence = []

    def traverse(self, t, behind: TrafficNode, ahead: TrafficNode):
        t %= sum(self.time_sequence) # t will be at least 0

        i = -1 # i is the index of the current position in the sequence
        while t >= 0:
            i = (i + 1) % len(self.path_sequence)
            t -= self.time_sequence[i]
        
        idle_time = 0
        while (behind, ahead) not in self.path_sequence[i]:
            i = (i + 1) % len(self.path_sequence)
            idle_time += self.time_sequence[i]

        return idle_time
    