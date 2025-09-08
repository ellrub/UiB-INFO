# Assignment 1
import math

print(math.ceil(math.log(102400, 2))) # 17 steps
print(math.ceil(math.log(480000, 2))) # 19 steps

# Assignment 2
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

node1 = Node("Letters")
node2 = Node("A")
node3 = Node("B")

node_list = LinkedList()
node_list.head = node1
node1.next = node2
node2.next = node3
node_list.print_list()

# Assignment 3
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

def reverse_list(my_list):
    stack = Stack()
    new_list = []
    for item in my_list:
        stack.push(item)
    while not stack.is_empty():
        new_list.append(stack.pop())

    print(new_list)
    
my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)

