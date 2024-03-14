# Assignment 4
#------- Question 1 -------#
# Answer is d) {(v0,v1), (v1,v2), (v2,v3)(v3,v4), (v4,v0), (v0,v5), (v5,v4), (v3,v5), (v5,v2) 

#------- Question 2 -------#
print('#------- Question 2 -------#')

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, from_vertex, to_vertex, cost):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.graph[from_vertex][to_vertex] = cost
    
    def get_vertices(self):
        return list(self.graph.keys())
    
    def get_vertex(self, vertex_key):
        return self.graph.get(vertex_key, {})
    
    def __contains__(self, vertex):
        return vertex in self.graph
    
    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(str(vertex) + ': ' + str(edges))

    def prepare_djikstra(self, start):
        dist = {vertex: float('inf') for vertex in self.graph}
        prev = {vertex: None for vertex in self.graph}
        dist[start] = 0
        return dist, prev
    
    def build_path(self, prev, start, end):
        path = []
        vertex = end
        while vertex != start:
            if prev[vertex] is None:
                return None
            path.insert(0, vertex)
            vertex = prev[vertex]
        path.insert(0, start)
        return path
    
    def dijkstra(self, start, end):
        dist, prev = self.prepare_djikstra(start)
        visited = set()
        current_vertex = start
        while current_vertex and current_vertex != end:
            visited.add(current_vertex)
            neighbors = self.graph.get(current_vertex, {})
            for neighbor, cost in neighbors.items():
                if neighbor not in visited:
                    new_cost = dist[current_vertex] + cost
                    if new_cost < dist[neighbor]:
                        dist[neighbor] = new_cost
                        prev[neighbor] = current_vertex
            next_vertex = None
            lowest = float('inf')
            for vertex in dist:
                if vertex not in visited and dist[vertex] < lowest:
                    lowest = dist[vertex]
                    next_vertex = vertex
            current_vertex = next_vertex
        return self.build_path(prev, start, end), dist[end]
    
graph = Graph()

graph.add_edge('A', 'B', 7)
graph.add_edge('A', 'C', 13)
graph.add_edge('B', 'C', 15)
graph.add_edge('B', 'D', 9)
graph.add_edge('C', 'D', 1)
graph.add_edge('C', 'E', 11)
graph.add_edge('D', 'E', 5)

print('\n---------- Graph structure ----------')
graph.print_graph()

vertex_key = 'A'
print('\n---------- Vertices and Edges for A ----------')
print('Edges for A:', graph.get_vertex(vertex_key))
print('Vertex ' + vertex_key + 'in graph: ', end='')
print(vertex_key in graph)

path, cost = graph.dijkstra('A', 'E')
print('\n---------- Shortest path from A to E ----------')
print('Shortest path:', path)
print('Cost: ', cost)

# Answer is 1) Shortest path: A -> B -> C -> D - Distance 19
print()
print('#--------------------------#')

#------- Question 3 -------#
print('#------- Question 3 -------#')
print()

COLUMNS = 'abcde'
NUM_QUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3
all_solutions = []

def solve(partial_sol):
    exam = examine(partial_sol)

    if exam == ACCEPT:
        all_solutions.append(partial_sol)

    elif exam != ABANDON:
        for p in extend(partial_sol):
            solve(p)
    return all_solutions

def extend(partial_sol):
    results = []
    row = len(partial_sol) + 1

    for column in COLUMNS:
        new_solution = list(partial_sol)
        new_solution.append(column + str(row))
        results.append(new_solution)

    return results

def examine(partial_sol):
    for i in range(len(partial_sol)):
        for j in range(i + 1, len(partial_sol)):

            if attacks(partial_sol[i], partial_sol[j]):
                return ABANDON
            
    if len(partial_sol) == NUM_QUEENS:
        return ACCEPT
    else:
        return CONTINUE

def attacks(p1, p2):
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])

    column2 = COLUMNS.index(p2[0]) + 1
    row2 = int(p2[1])

    return (row1 == row2 or column1 == column2 or abs(row1-row2) == abs(column1-column2))

def is_solution(candidate_solution):
    for char, num in candidate_solution:
        print(char, num)

candidate_solution1 = ['d3', 'c1', 'e5', 'b4', 'a2']
candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']

result1 = is_solution(candidate_solution1)
result2 = is_solution(candidate_solution2)

print('Candidate Solution 1:', result1)
print('Candidate Solution 2:', result2)

print()
print('#--------------------------#')

#------- Question 4 -------#
print('#------- Question 4 -------#')
print()

class Graph2:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.graph:
            self.graph[from_vertex] = []
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)
        self.graph[from_vertex].append(to_vertex)

    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(vertex + ': ' + str(edges))

    def remove_vertex(self, vertex):
        self.graph.pop(vertex)

graph2 = Graph2()
graph2.add_edge('a', 'b')
graph2.add_edge('a', 'c')
graph2.add_edge('b', 'c')
graph2.add_edge('b', 'd')
graph2.add_edge('c', 'd')
graph2.add_edge('d', 'e')

print('Before removal of vertex:')
graph2.print_graph()

graph2.remove_vertex('a')
print('After removal of vertex:')
graph2.print_graph()


