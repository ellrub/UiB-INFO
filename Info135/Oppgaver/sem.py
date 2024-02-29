class BinaryTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def printndoes(self):
        print(self.data)
        if self.left:
            self

node1 = BinaryTree(1)

node1.left = BinaryTree(2)
node1.right = BinaryTree(3)

node1.left.left = BinaryTree(4)
node1.right.left = BinaryTree(5)

node1.right.left = BinaryTree(6)
node1.right.right = BinaryTree(7)