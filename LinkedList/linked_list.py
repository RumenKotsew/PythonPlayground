from node import Node


class LinkedList():
    def __init__(self, head_data):
        self.head = Node(head_data)
        self.head.next = Node(None)
        self.head.previous = Node(None)

    def get_head(self):
        return self.head.data

    def add_element(self, data):
        if self.head.next.data is None:
            self.head.next.data = data
        else:
            current_node = self.head
            return self.add_element_recursive(current_node, data)

    def add_element_recursive(self, current_node, data):
        if current_node.next is None:
            current_node.next = Node(data)
        else:
            current_node = current_node.next
            return self.add_element_recursive(current_node, data)

    def index(self, index):
        current_node = self.head
        counter = 0
        result = self.index_recursive(current_node, counter, index)
        return result

    def index_recursive(self, current_node, counter, index):
        if counter != index:
            counter += 1
            current_node = current_node.next
            return self.index_recursive(current_node, counter, index)
        else:
            return current_node.data

    def size(self):
        current_node = self.head
        counter = 1
        return self.size_recursive(current_node, counter)

    def size_recursive(self, current_node, counter):
        if self.head.next is not None and self.head.next.data is None:
            return counter
        if current_node.next is None:
            return counter
        else:
            counter += 1
            current_node = current_node.next
            return self.size_recursive(current_node, counter)

    def remove(self, index):
        current_node = self.head
        counter = 0
        while counter != index:
            counter += 1
            current_node = current_node.next
        target_node = current_node
        current_node = self.head
        while current_node.next is not None:
            if current_node.next != target_node:
                current_node = current_node.next
            else:
                current_node.next = current_node.next.next

    def pprint(self):
        current_node = self.head
        self.print_recursive(current_node)

    def print_recursive(self, current_node):
        print(current_node.data)
        if current_node.next is not None:
            current_node = current_node.next
            return self.print_recursive(current_node)

    def to_list(self):
        new_list = []
        current_node = self.head
        while current_node.next is not None:
            new_list.append(current_node.data)
            current_node = current_node.next
        else:
            new_list.append(current_node.data)
            return new_list

    def add_at_index(self, index, data):
        current_node = self.head
        counter = 0
        while counter != index - 1:
            current_node = current_node.next
            counter += 1
        temp_node = current_node.next
        current_node.next = Node(data)
        current_node.next.next = temp_node

    def add_first(self, data):
        temp_node = self.head
        self.head = Node(data)
        self.head.next = temp_node

    # def add_linked_list(self, new_list):
    #     self.add_element(new_list.get_head())
    #     return self.add_linked_list_inner(new_list)

    # def add_linked_list_inner(self, new_list):
    #     if new_list.head.next.data is not None:
    #         index = 1
    #         while index != new_list.size():
    #             self.add_element(new_list.index(index))
    #             index += 1

    def add_list(self, new_list):
        for i in range(0, len(new_list)):
            self.add_element(new_list[i])

    def ll_from_to(self, start_index, end_index):
        current_node = self.head
        counter = 0
        while counter != start_index:
            current_node = current_node.next
            counter += 1
        new_list = LinkedList(current_node.data)
        counter += 1
        while counter != end_index:
            current_node = current_node.next
            counter += 1
            new_list.add_element(current_node.data)

        return new_list

    def pop(self):
        self.remove(self.size() - 1)

    def reduce_to_unique(self):
        if self.head.next is not None and self.head.next.data is not None:
            target_node = self.head
            current_node = self.head
            while target_node.next is not None:
                self.reduce_to_unique_recursive(target_node, current_node)
                target_node = target_node.next

    def reduce_to_unique_recursive(self, target_node, current_node):
        if current_node.next is not None:
            if current_node.next.data == target_node.data and \
                    current_node.next != target_node:
                current_node.next = current_node.next.next
            if current_node.next is not None:
                return self.reduce_to_unique_recursive(target_node,
                                                       current_node.next)
