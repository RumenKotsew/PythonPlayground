from unittest import TestCase, main
from node import Node
from linked_list import LinkedList


class TestLinkedList(TestCase):
    def setUp(self):
        self.test_list = LinkedList('head_data')

    def test_set_up(self):
        self.assertIsNone(self.test_list.head.next.data)
        self.assertEqual(self.test_list.head.data, 'head_data')
        self.test_list.head.next = Node(25)
        current_node = self.test_list.head
        self.assertEqual(current_node.next.data, 25)

    def test_get_head(self):
        self.assertEqual(self.test_list.get_head(), self.test_list.head.data)

    def test_add_element(self):
        self.test_list.add_element('node2data')
        self.assertEqual(self.test_list.head.next.data, 'node2data')

    def test_add_at_index(self):
        self.test_list.head.next.data = 'node2data'
        self.test_list.add_at_index(2, 'node3data')
        self.assertEqual(self.test_list.head.next.next.data, 'node3data')

    def test_size(self):
        self.test_list.head.next.data = 'node2data'
        self.test_list.head.next.next = Node('node3data')
        self.assertEqual(self.test_list.size(), 3)

    def test_index(self):
        self.test_list.head.next.data = 'node2data'
        self.assertEqual(self.test_list.index(1), 'node2data')

    def test_remove(self):
        self.test_list.head.next.data = 'node2data'
        self.test_list.head.next.next = Node('node3data')
        self.assertEqual(self.test_list.size(), 3)
        self.test_list.remove(1)
        self.assertEqual(self.test_list.size(), 2)
        self.assertEqual(self.test_list.head.next.data, 'node3data')

    def test_to_list(self):
        self.test_list.head.next.data = 'node2data'
        self.assertEqual(self.test_list.to_list(), ['head_data', 'node2data'])

    def test_add_first(self):
        self.test_list.add_first('add_first_data')
        self.assertEqual(self.test_list.head.next.data, 'head_data')

    def test_add_list(self):
        self.test_list.add_list([1, 2, 3, 4])
        self.assertEqual(self.test_list.size(), 5)

    def test_pop(self):
        self.test_list.head.next.data = 'node2data'
        self.test_list.pop()
        self.assertEqual(self.test_list.size(), 1)

    def test_reduce_to_unique(self):
        self.test_list.head.next.data = 'node2data'
        self.test_list.add_element('node3data')
        self.test_list.add_element('node2data')
        self.test_list.reduce_to_unique()
        self.assertIsNone(self.test_list.head.next.next.next)


if __name__ == "__main__":
    main()
