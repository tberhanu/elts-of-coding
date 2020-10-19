from collections import deque
class Graph:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def print_graphs(self):
        print(self.name)
        for vertex in self.edges:
            vertex.print_graphs()

def clone_graph(G):
    """
    Consider a vertex type for a directed graph in which there are two fields: an integer label(or string name) and
    a list of references to other vertices.
    Design an algorithm that takes a references to a vertex U, and creates a copy of the graph on the vertices reachable
    from U. Return the copy of U.

    Time: O(|V| + |E|)
    Space: O(|V| + |E|)
    """
    if not G:
        return None
    queue = deque([G])
    cloned_graph = {G: Graph(G.name)}
    while queue:
        node = queue.pop() # node = queue.popleft()
        for adj in node.edges:
            if adj not in cloned_graph:
                cloned_graph[adj] = Graph(adj.name)
                queue.appendleft(adj) # queue.append(adj)
            cloned_graph[node].edges.append(cloned_graph[adj])

    return cloned_graph[G]

if __name__ == "__main__":
    graph = Graph("A")
    B, C, D = Graph("B"), Graph("C"), Graph("D")
    graph.edges = [B, C, D]
    B.edges = [Graph("BB"), Graph("BBB")]
    C.edges = [Graph("CC"), Graph("CCC")]
    print("____ original graph ____")
    graph.print_graphs()
    print("________ cloned graph ______")
    cloned = clone_graph(graph)
    cloned.print_graphs()


