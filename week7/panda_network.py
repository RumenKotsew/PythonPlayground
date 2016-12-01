from panda_graph import Node


class PandaNetwork():
    def __init__(self):
        self.pandas_dict = {}

    def add_panda(self, panda):
        if isinstance(panda, Node):
            if panda not in self.pandas_dict:
                self.pandas_dict[panda.get_name()] = (panda.get_email(),
                                                      panda.get_gender())
            else:
                print('PandaAlreadyThere')

    def has_panda(self, panda):
        if isinstance(panda, Node):
            return panda.get_name() in self.pandas_dict
        else:
            print('InvalidInput')

    def make_friends(panda1, panda2):
        pass

    def are_friends(panda1, panda2):
        pass

    def friends_of(panda):
        pass

    def connection_level(panda1, panda2):
        pass

    def are_connected(panda1, panda2):
        pass

    def how_many_gender_in_network(level, panda, gender):
        pass
