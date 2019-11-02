
class Edge:

    def __init__(self, weight: int):
        self.weight = weight

    def get_weight(self) -> float:
        return self.weight


# Simple example subclasses of Edge

class RoadUsage(Edge):

    def __init__(self, capacity, amount=0):
        self.capacity = capacity
        self.amount = amount

    # Measuring traffic
    def get_weight(self):
        self.amount /  self.capacity

    def update_amount(self, amt):
        if amt > 0: 
            self.amount = amt