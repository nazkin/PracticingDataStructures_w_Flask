class Node:
    def __init__(self, data=None):
        self.data=data
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_recursively(self, data, node):
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_recursively(data, node.left)
        elif data["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_recursively(data, node.right)
        else:
            return

    def insert_value(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_recursively(data, self.root)

    def search_node_recursively(self, node_id, node):
        if node_id == node.data["id"]:
            return node.data

        if node_id < node.data["id"] and node.left is not None:
           if node_id == node.left.data["id"]:
               return node.left.data
           else:
               return self.search_node_recursively(node_id, node.left)

        if node_id > node.data["id"] and node.right is not None:
            if node_id == node.right.data["id"]:
                return node.right.data
            else:
                return self.search_node_recursively(node_id, node.right.data)

        return False

    def search_node(self, id):
        node_id = int(id)
        if self.root is None:
            return False
        else:
           return self.search_node_recursively(node_id, self.root)