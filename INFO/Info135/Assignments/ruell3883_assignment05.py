# Assignment 5
#------- Question 1 -------#
# All of the trees are Full Binary Trees

#--------------------------#

#------- Question 2 -------#
# Matrix number 2 correctly displays the adjacency matrix of the graph.

#--------------------------#

#------- Question 3 -------#
def binary_tree(r):
    return [r, [], []]

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def insert_left_child(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right_child(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, t, []])
    else:
        root.insert(2, [new_branch, [], []])
    return root

def make_tree():
    my_tree = binary_tree('1')
    insert_left_child(my_tree, '2')
    insert_right_child(my_tree, '3')

    insert_left_child(get_left_child(my_tree), '4')

    insert_left_child(get_right_child(my_tree), '5')
    insert_right_child(get_right_child(my_tree), '6')

    print(my_tree)

make_tree() # Output ['1', ['2', ['4', [], []], []], ['3', ['5', [], []], ['6', [], []]]]

#--------------------------#

#------- Question 4 -------#
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

    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(vertex + ': ' + str(edges))

    def dfs(self, start):
        visited = []
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                for x in self.graph.get(vertex, []):
                    if x not in visited:
                        stack.append(x)
        return visited

graph = Graph()

vertices = ['a', 'b', 'c', 'd', 'e']

for vertex in vertices:
    graph.add_vertex(vertex)

edges = [('a', 'c'), ('a', 'd'), ('b', 'a'), ('c', 'b'), ('d', 'e'), ('e', 'a')]

for from_vertex, to_vertex in edges:
    graph.add_edge(from_vertex, to_vertex)

print('\n---------- Graph structure ----------')
graph.print_graph()

print('\n---------- DFS ----------')
dfs_order = graph.dfs('b')
print('DFS visit order starting from "b":', dfs_order)

#------- Output a) --------#
# ---------- Graph structure ----------
# a: ['c', 'd']
# b: ['a']
# c: ['b']
# d: ['e']
# e: ['a']

#------- Output b) --------#
# ---------- DFS ----------
# DFS visit order starting from "b": ['b', 'a', 'd', 'e', 'c']

#--------------------------#

#------- Question 5 -------#
class BinarySearchTree:
    def __init__(self, value = None):
        self.value = value
        if self.value is not None:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        else:
            self.left_child = None
            self.right_child = None

    def is_empty(self):
        return self.value is None
    
    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        elif value < self.value:
            self.left_child.insert(value)
        elif value > self.value:
            self.right_child.insert(value)

    def in_order(self):
        if self.is_empty():
            return []
        else:
            return (self.left_child.in_order() + [self.value] + self.right_child.in_order())

    def compute_sum(self):
        sum = 0
        numbers = self.in_order()
        for num in numbers:
            sum += num
        return sum

    def compute_count(self):
        count = len(self.in_order())
        return count

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)
my_tree.insert(10)
my_tree.insert(12)

print('Sum:', my_tree.compute_sum())
print('Number of nodes:', my_tree.compute_count())

# Output
# Sum: 42
# Number of nodes: 6

#--------------------------#