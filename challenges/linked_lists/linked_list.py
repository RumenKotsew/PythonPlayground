class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()


class LinkedList(object):

    def __init__(self, head=None):
        if isinstance(head, Node):
            self.head = head
        elif head is not None:
            self.head.data = head
        else:
            self.head = None

    def __len__(self):
        if self.head is None:
            return 0
        counter = 0
        current_node = self.head
        while current_node.next is not None:
            counter += 1
            current_node = current_node.next
        counter += 1
        return counter

    def insert_to_front(self, data):
        if data is None:
            return False
        if self.head is None:
            self.head = Node(data)
            return True
        current_node = Node(self.head.data)
        if self.head.next is not None:
            current_node.next = self.head.next
        self.head.data = data
        self.head.next = current_node

    def append(self, data):
        if data is None:
            return False
        elif self.head is None:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(data)

    def find(self, data):
        if data is None:
            return None
        if self.head is None:
            return None
        current_node = self.head
        while current_node.next is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def delete(self, data):
        if data is None or self.head is None:
            return None
        if self.head.data == data:
            self.head = self.head.next
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
            current_node = current_node.next

    def print_list(self):
        if self.head is None:
            print(None)
        current_node = self.head
        while current_node.next is not None:
            print(current_node)
            current_node = current_node.next

    def get_all_data(self):
        res = []
        if self.head is None:
            return res
        if self.head.next is None:
            res.append(self.head.data)
            return res
        current_node = self.head
        while current_node.next is not None:
            res.append(current_node.data)
            current_node = current_node.next
        res.append(current_node.data)
        return res
