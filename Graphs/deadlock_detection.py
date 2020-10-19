from Graphs import Vertex, Graph
def is_deadlock(graph):
    """
    Question: Write a program that takes as input a directed graph and checks if the graph contains a cycle.

    Strategy:
        1. Need to check each of the vertices if any of them has a cycle.
        2. Any visited fresh node is in PENDING mode until it's adjacent nodes finish.
        3. But if one of it's adjacent nodes point to that PENDING mode vertex, then CYCLE created.

    Time: O(|V| + |E|) like DFS
    Space: O(|V|) which is the maximum Recursion Stack Depth

    Variant: What if the graph is UNDIRECTED GRAPH?
        Strategy: DFS and claim for CYCLE if getting already visited vertex.
    """
    def has_cycle(vertex):
        if vertex.status == Vertex.pending:
            return True
        vertex.status = Vertex.pending
        for adj_vertex in vertex.edges:
            if adj_vertex.status != Vertex.done and has_cycle(adj_vertex): # dfs
                return True
        vertex.status = Vertex.done
        return False

    return any(has_cycle(vertex) for vertex in graph.vertices if vertex.status == Vertex.fresh)

if __name__ == "__main__":
    c, b, a, d, f, e = Vertex(3), Vertex(2), Vertex(1), Vertex(4), Vertex(6), Vertex(5)
    a.add_edge(b)
    a.add_edge(c)
    b.add_edge(c)
    d.add_edge(a)
    d.add_edge(e)
    e.add_edge(f)
    f.add_edge(d)
    vertices = [a, b, c, d, e, f]
    graph = Graph(vertices)
    print(is_deadlock(graph))






