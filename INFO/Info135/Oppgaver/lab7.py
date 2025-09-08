# Exercise 1

# 1) True, the graph is directed
# 2) False, (2,1) is not part of the edge set
# 3) True, 0 -> 1 -> 2 -> 0 is one cycle

# Exercise 2 and 3
class Graph:
    def __init__(self):
        self.graph = {} 

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.graph:
            self.graph[from_vertex] = []
        self.graph[from_vertex].append(to_vertex)
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)

    # def get_vertices(self):
    #     return list(self.graph.keys())

    # def get_adjacency(self, vertex):
    #     return self.graph.get(vertex, [])

    # def get_vertex(self, vertex_key):
    #     return self.graph.get(vertex_key, None)

    # def __contains__(self, vertex):
    #     return vertex in self.graph

    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(vertex + ": " + str(edges))

    def nodes_out_degree(self, n):
        nodes = []
        for vertex, edges in self.graph.items():
            if len(edges) == n:
                nodes.append(vertex)
        return nodes
    
    def remove_edge(self, node1, node2):
        if node2 in self.graph.get(node1, []):
            self.graph[node1].remove(node2)

graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'A')
graph.add_edge('C', 'A')
graph.add_edge('B', 'C')
graph.add_edge('F', 'B')

print(graph.nodes_out_degree(2))

graph.remove_edge('A', 'B')

graph.print_graph()


