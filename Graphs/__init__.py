"""
DAG - directed graph with NO CYCLE.
CONNECTED - if EVERY pair of vertices in the graph is CONNECTED.
CONNECTED COMPONENT - self explanatory ...
WEAKLY CONNECTED - Connected definition without taking consideration of the DIRECTION
STRONGLY CONNECTED - Connected definition considering the DIRECTION
CONNECTED - without considering the DIRECTION
GRAPH IMPLEMENTATION - Adjacency Lists or Adjacency Matrix
TREE - Undirected Connected Graph with NO CYCLES
    ROOTED TREE -
    ORDERED TREE -
    BINARY TREE -

BFS and DFS: Time: O(|V| + |E|)
             Space: O(|V|)

BFS: Can be used to compute distances from the start index.
DFS: Can be used to check for the presence of cycles.
"""

class Vertex:
    fresh, pending, done = range(3)
    def __init__(self, id, edges=[]):
        self.id = id
        self.edges = edges
        self.status = Vertex.fresh

    def add_edge(self, vertex):
        self.edges.append(vertex)

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
