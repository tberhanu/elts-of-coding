class Vertex:
    def __init__(self, id, color="white", adjacents={}, edges={}):
        self.id = id
        self.color = color
        self.adjacents = adjacents
        self.edges = edges

    def add_edge(self, vertex, weight=0):
        self.adjacents[vertex] = weight
        self.edges[vertex] = (self, vertex, weight)

    def get_id(self):
        return self.id

    def set_color(self, color):
        self.color = color



class Graph:
    def __init__(self):
        self.num_of_vertices = 0
        self.lookup_vertex = {}

    def add_vertex(self, id):
        vertex = Vertex(id)
        self.lookup_vertex[id] = vertex
        self.num_of_vertices += 1

    def set_color(self, id, color):
        self.lookup_vertex[id] = color

    def get_vertex(self, id):
        if id in self.lookup_vertex:
            return self.lookup_vertex[id]
        else:
            return None

    def add_edge(self, id1, id2, weight=9):
        if id1 not in self.lookup_vertex:
            self.lookup_vertex[id1] = Vertex(id1)
            self.num_of_vertices += 1
        if id2 not in self.lookup_vertex:
            self.lookup_vertex[id2] = Vertex(id2, "Gray")
            self.num_of_vertices += 1

        vertex1 = self.lookup_vertex[id1]
        vertex2 = self.lookup_vertex[id2]
        vertex1.add_edge(vertex2, weight)

    def get_all_vertices(self):
        return self.lookup_vertex.values()

    def get_all_vertices_id(self):
        return self.lookup_vertex.keys()

    def get_adjacent_ids(self, id):
        if id not in self.lookup_vertex:
            return None
        vertex = self.lookup_vertex[id]
        return vertex.adjacents.keys()

    def get_adjacent_vertices(self, id):
        if id not in self.lookup_vertex:
            return None
        vertex = self.lookup_vertex[id]
        return vertex.adjacents.values()

    def get_all_edges(self):
        """
        Note: To apply Kruskal Algorithm, we need to get all the EDGES and need to SORT them.
        """
        all_edges = []
        vertices = self.get_all_vertices()
        for vertex in vertices:
            id = vertex.get_id()
            adj_vertices = self.get_adjacent_vertices(id)
            for adj_vertex in adj_vertices:
                edge = vertex.edges[adj_vertex]
                all_edges.append(edge)
        return all_edges



