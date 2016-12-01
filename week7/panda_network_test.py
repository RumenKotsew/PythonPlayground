from unittest import TestCase, main
from panda_network import PandaNetwork
from panda_graph import Node


class PandaNetworkTest(TestCase):
	def setUp(self):
		self.panda = Node('Ivo', 'ivo@pandamail.com', 'male')
		self.network = PandaNetwork()

	def test_add_panda(self):
		self.network.add_panda(self.panda)
		self.assertEqual(self.network.pandas_dict[self.panda.get_name()],
						 (self.panda.get_email(), self.panda.get_gender()))

	def test_has_panda(self):
		self.network.add_panda(self.panda)
		panda_2 = Node('Rumen', 'rumen@rumen.com', 'male')
		self.assertTrue(self.network.has_panda(self.panda))
		self.assertFalse(self.network.has_panda(panda_2))


if __name__ == "__main__":
    main()