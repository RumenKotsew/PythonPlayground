from unittest import TestCase, main
from panda_graph import Node


class NodeTest(TestCase):
    def setUp(self):
        self.name = 'Ivo'
        self.email = 'ivo@pandamail.com'
        self.gender = 'male'
        self.panda = Node(self.name, self.email, self.gender)

    def test_get_name(self):
        self.assertEqual(self.panda.get_name(), 'Ivo')

    def test_get_email(self):
        self.assertEqual(self.panda.get_email(), 'ivo@pandamail.com')

    def test_get_gender(self):
        self.assertEqual(self.panda.get_gender(), 'male')

    def test_is_male(self):
        self.assertTrue(self.panda.is_male())

    def test_is_female(self):
        self.assertFalse(self.panda.is_female())

    def test_str(self):
        self.assertEqual(self.panda.__str__(), 'Ivo, ivo@pandamail.com, male')

    def test_eq(self):
        new_panda = Node('Ivo', 'ivo@pandamail.com', 'male')
        new_panda_2 = Node('Rado', 'radorado@rado.com', 'male')
        new_panda_3 = Node('Rado', 'radorado@rado.com', 'male')
        self.assertEqual(new_panda_2, new_panda_3)
        self.assertTrue(self.panda.__eq__(new_panda))
        self.assertFalse(self.panda.__eq__(new_panda_2))

    def test_hash(self):
        new_panda = Node('Ivo', 'ivo@pandamail.com', 'male')
        new_panda_2 = Node('Rado', 'radorado@rado.com', 'male')
        self.assertEqual(self.panda.__hash__(), new_panda.__hash__())
        self.assertNotEqual(self.panda.__hash__(), new_panda_2.__hash__())


if __name__ == "__main__":
    main()
