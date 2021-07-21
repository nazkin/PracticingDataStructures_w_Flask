class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_array_list(self):
        arr_list = []
        if self.head is None:
            return arr_list
        node = self.head
        while node:
            arr_list.append(node.data)
            node = node.next_node
        return arr_list


    def print_list(self):
        list_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            list_string += f" {str(node.data)} ->"
            if node.next_node is None:
                list_string += " None"
            node = node.next_node
        print(list_string)

    def insert_beginning(self, data):
        if self.head is None:
            new_node = Node(data, None)
            self.head = new_node
            self.last_node = self.head

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if int(node.data["id"]) is int(user_id):
               return node.data
            node = node.next_node
        return None
