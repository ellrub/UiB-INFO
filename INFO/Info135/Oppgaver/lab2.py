class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node1
node2.next = node2
node3.next = node3
