class NodeData:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def create_custom_hash(self, key):
        hash_value = 0;
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * ord(i) % self.size)
        return hash_value

    def add_key_value_pair(self, key, value):
       hashed_key = self.create_custom_hash(key)
       if self.hash_table[hashed_key] is None:
           self.hash_table[hashed_key] = Node(NodeData(key, value), None)
       else:
           current_node = self.hash_table[hashed_key]
           while current_node.next_node:
               current_node = current_node.next_node

           current_node.next_node = Node(NodeData(key, value), None)

    def retrieve_value(self, key):
        hashed_key = self.create_custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            if node.next_node is None:
                return node.data.value
            else:
                while node.next_node:
                    if key == node.data.key:
                        return node.data.value
                    node = node.next_node
                if key == node.data.key:
                    return node.data.value
        return None