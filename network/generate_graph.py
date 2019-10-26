
import random
from node import Node
from edge import Edge
from graph import Graph

# 
# 0 -> 1 -> 2
#      |
#      V
#      3

nodes = [Node(), Node(), Node(), Node()]

edge0 = Edge(nodes[0], nodes[1], distance=10, speed=5)
edge1 = Edge(nodes[1], nodes[2], distance=20, speed=10)
edge2 = Edge(nodes[1], nodes[3], distance=30, speed=15)

edges = [edge0, edge1, edge2]
graph = Graph(nodes, edges)