class Node:
    def __init__(self, data=None):
        self.data=data
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_recursively(self, value, node):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_recursively(value, node.left)
        elif value > node.data:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recursively(value, node.right)
        else:
            return

    def insert_value(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursively(value, self.root)