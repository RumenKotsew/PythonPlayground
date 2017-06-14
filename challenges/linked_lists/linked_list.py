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
        if head is not None:
            self.head = Node(head)
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
        pass
        # TODO: Implement me

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
        pass
        # TODO: Implement me

    def delete(self, data):
        pass
        # TODO: Implement me

    def print_list(self):
        pass
        # TODO: Implement me

    def get_all_data(self):
        res = []
        if self.head.next is None:
            res.append(self.head.data)
            return res
        current_node = self.head
        while current_node.next is not None:
            res.append(current_node.data)
            current_node = current_node.next
        res.append(current_node.data)
        return res
