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
        return self.iterate_list_for(list_len=True)

    def validate_user_input(self, data):
        if data is None:
            raise TypeError('Input type cannot be None')
        else:
            return True

    def insert_to_front(self, data):
        if self.validate_user_input(data):
            if self.head is None:
                self.head = Node(data)
            else:
                current_node = Node(self.head.data)
                if self.head.next is not None:
                    current_node.next = self.head.next
                self.head.data = data
                self.head.next = current_node

    def append(self, data):
        if self.validate_user_input(data):
            if self.head is None:
                self.head = Node(data)
            else:
                current_node = self.head
                while current_node.next is not None:
                    current_node = current_node.next
                current_node.next = Node(data)

    def find(self, data):
        if data is None or self.head is None:
            return None
        return self.iterate_list_for(find=True, data=data)

    def delete(self, data):
        if data is None or self.head is None:
            return None
        if self.head.data == data:
            self.head = self.head.next
        self.iterate_list_for(delete=True, data=data)

    def print_list(self):
        if self.head is None:
            print('List is empty')
        self.iterate_list_for(print_list=True)

    def get_all_data(self):
        if self.head is None:
            return []
        if self.head.next is None:
            return [self.head.data]
        return self.iterate_list_for(get_all_data=True)

    def iterate_list_for(self, list_len=False, find=False, delete=False,
                         print_list=False, get_all_data=False, data=None):
        current_node = self.head
        res = []
        counter = 0
        while current_node.next is not None:
            if list_len:
                counter += 1
            if find:
                if current_node.data == data:
                    return current_node
            if delete:
                if current_node.next.data == data:
                    current_node.next = current_node.next.next
                    break
            if print_list:
                print(current_node)
            if get_all_data:
                res.append(current_node.data)
            current_node = current_node.next

        if find:
            return None
        if list_len:
            counter += 1
            return counter
        if get_all_data:
            res.append(current_node.data)
            return res
