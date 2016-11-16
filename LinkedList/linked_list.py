from node import Node


class LinkedList():
    def __init__(self, head_data):
        self.head = Node(head_data)
        self.counter = 0

    def get_head(self):
        return self.head.data

    def add_element(self, data):
        self.add_at_index(self.size() - 1)

    def index(self, index):
        current_node = self.head
        counter = 0
        result = self.index_recursive(current_node, counter, index)
        print(result)

    def index_recursive(self, current_node, counter, index):
        if counter != index:
            counter += 1
            current_node = current_node.next
            self.index_recursive(current_node, counter, index)
        else:
            return current_node.data  # done

    def size(self):
        current_node = self.head
        counter = 0
        return self.size_recursive(current_node, counter)

    def size_recursive(self, current_node, counter):
        if current_node.next is not None:
            counter += 1
            current_node = current_node.next
            self.size_recursive(current_node, counter)
        else:
            return counter

    def remove(self, index):
        current_node = self.head
        target_node = Node(self.index(index))
        while current_node.next != target_node:
            current_node = current_node.next
        current_node.next = current_node.next.next
        current_node.next.previous = current_node

    def pprint(self):
        current_node = self.head
        self.print_recursive(current_node)

    def print_recursive(self, current_node):
        print(current_node.data)
        if current_node.next is not None:
            current_node = current_node.next
            self.print_recursive(current_node)

    def to_list(self):
        counter = 0
        new_list = []
        current_node = self.head
        while current_node.next is not None:
            new_list[counter] = current_node.data
            counter += 1
            current_node = current_node.next
        new_list[counter + 1] = current_node.data

        return new_list

    def add_at_index(self, index, data):
        current_node = self.head
        counter = 0
        while counter != index - 1:
            current_node = current_node.next
            counter += 1
        temp_node = current_node.next
        current_node.next = Node(data)
        current_node.next.previous = current_node
        current_node.next.next = temp_node
        current_node.next.next.previous = current_node.next

    def add_first(self, data):
        temp_node = self.head
        self.head = Node(data)
        self.head.next = temp_node

    def add_linked_list(self, new_list):
        current_node = Node(new_list.get_head())
        self.add_element(current_node.data)
        counter = 1
        while counter != new_list.size():
            current_node.next = Node(new_list.index(counter))
            counter += 1
            current_node = current_node.next
            self.add_element(current_node.data)

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
        current_node = self.head
        while current_node.next is not None:
            self.remove_identical_nodes(current_node.data)
            current_node = current_node.next

    def remove_identical_nodes(self, data):
        target_node = Node(data)
        counter = 1
        if self.head.next.data != target_node.data:
            current_node = self.head.next.next
            counter = 2
        else:
            current_node = self.head.next
        while current_node.next is not None:
            if current_node.data == target_node.data:
                current_node = current_node.next
                self.remove(counter)
            else:
                counter += 1
                current_node = current_node.next
