
import random
from node import Node
from edge import Edge

nodes = [Node() for i in range(10)]
edges = [Edge(random.choice(nodes), random.choice(nodes), random.randint(1, 100), random.randint(1, 100)) for i in range(30)]

print(nodes)
print(edges)