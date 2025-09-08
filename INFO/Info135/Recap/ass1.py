# Oppgave 1
# a) log2(102400) = 16.6 = 17 steps
# b) log2(480000) = 18.9 = 19 steps

# Oppgave 2
class LinkedList:
    
    def __init__(self):
        self.head = None

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node("brunch")
node2 = Node("bocce")
node3 = Node("drink tea")

todo_list = LinkedList()
todo_list.head = node1
node1.next = node2
node2.next = node3

todo_list.print_list()

# Oppgave 3
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

def reverse_list(list):
    stack = Stack()
    new_list = []
    for item in list:
        stack.push(item)
    while not stack.is_empty():
        new_list.append(stack.pop())

    print(new_list)

my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)