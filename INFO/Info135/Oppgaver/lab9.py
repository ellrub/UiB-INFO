# Oppgave 1
# a) Pre-order - H, A, D, E, C, B, G, F

# b) In-order - D, A, E, H, C, G, B, F

# c) Post-order - D, E, A, G, F, B, C, A

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
        
    def print_tree(self):
        if not self.is_empty():
            print(self.in_order())

    def post_order(self):
        if self.is_empty():
            return[]
        else:
            return (self.left_child.post_order() + self.right_child.post_order() + [self.value])

    def pre_order(self):
        if self.is_empty():
            return []
        else:
            return ([self.value] + self.left_child.pre_order() + self.right_child.pre_order())
        
my_tree = BinarySearchTree()
my_tree.insert(3)
my_tree.insert(1)
my_tree.insert(4)
my_tree.insert(2)
my_tree.insert(5)

print("Pre-order traversal:", my_tree.pre_order())
print("In-order traversal:", my_tree.in_order())
print("Post-order traversal:", my_tree.post_order())
print(f'Lowest value in tree: {min(my_tree.in_order())}\nHighest value in tree {max(my_tree.in_order())}')


# Oppagve 2

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def search(self, value):
        if self.value == value:
            return True
        if self.left_child and self.left_child.search(value):
            return True
        if self.right_child and self.right_child.search(value):
            return True
        return False
    
    def print_tree(self, level = 0):
        print(' ' * level * 2 + str(self.value))
        if self.left_child is not None:
            self.left_child.print_tree(level + 1)
        if self.right_child is not None:
            self.right_child.print_tree(level + 1)

tree = BinaryTree('H')
tree.insert_left('A')
tree.insert_right('C')

node_chap1 = tree.left_child
node_chap1.insert_left('D')
node_chap1.insert_right('E')

node_chap2 = tree.right_child
node_chap2.insert_right('B')

node_sec1_2 = node_chap2.right_child
node_sec1_2.insert_left('G')
node_sec1_2.insert_right('F')

tree.print_tree()

print('D exists?', tree.search('D'))
print('T exists?', tree.search('T'))

# Oppgave 3
# Se siste linje på koden i oppagve 1

# Oppgave 4