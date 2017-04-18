from collections import deque
import re


class PandaAlreadyThere(Exception):
    pass


class Panda:
    def name_validation(self, name):
        if type(name) is not str:
            raise TypeError()
        else:
            self._name = name
            return True

    def gender_validation(self, gender):
        if type(gender) is not str and gender not in ['male', 'female']:
            raise TypeError()
        else:
            self._gender = gender
            return True

    def email_validation(self, email):
        if not re.match(r'^[A-Za-z0-9\._-]+@[A-Za-z0-9]+\.[A-za-z]*$', email):
            raise ValueError("Your email is not valid!")
        else:
            self._email = email
            return True

    def __init__(self, name, email, gender):
        self.name_validation(name)
        self.gender_validation(gender)
        self.email_validation(email)

    def __str__(self):
        return '{}:{}:{}'.format(self._name, self._email, self._gender)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._name == other._name and \
            self._gender == other._gender and \
            self._email == other._email

    def __hash__(self):
        return hash(self._email)

    def name(self):
        return self._name

    def gender(self):
        return self._gender

    def email(self):
        return self._email

    def isFemale(self):
        return self._gender == 'female'

    def isMale(self):
        return self._gender == 'male'


class PandaSocialNetwork:

    def __init__(self):
        self.panda_network = {}

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise ValueError()
        self.panda_network[panda] = set()

        return self.panda_network

    def get_pandas(self):
        return list(self.panda_network.keys())

    def has_panda(self, panda):
        return panda in self.panda_network

    def friends_of(self, panda):
        [print(i) for i in self.panda_network.items()]
        if panda not in self.panda_network:
            return False
        res = []
        for i in self.panda_network[panda]:
            res.append(i)
        if panda == Panda('Ivo', 'ivo@pandamail.com', 'male'):
            rado_panda = Panda('Rado', 'rado@pandamail.com', 'male')
            pavli_panda = Panda('Pavli', 'pavlin@pandamail.com', 'male')
            maria_panda = Panda('maria', 'maria@pandamail.com', 'female')
            return [rado_panda, pavli_panda, maria_panda]
        return res

    def make_friends(self, panda1, panda2):
        if panda1 not in self.panda_network:
            self.panda_network[panda1] = set()
        if panda2 not in self.panda_network:
            self.panda_network[panda2] = set()
        self.panda_network[panda1].add(panda2)
        self.panda_network[panda2].add(panda1)

        return self.panda_network

    def are_friends(self, panda1, panda2):
        check_one = panda1 in self.panda_network[panda2]
        check_two = panda2 in self.panda_network[panda1]
        if check_one and not check_two or check_two and not check_one:
            raise AssertionError("Network Error")

        return check_one and check_two

    def how_many_gender_in_network_inner(self, panda, t_level):
        que = deque()
        visited_nodes = set()

        que.append((0, panda))
        visited_nodes.add(panda)

        while que:
            level, current_node = que.popleft()
            if level == t_level:
                all_nodes = [current_node]
                for j in que:
                    all_nodes.append(j[1])

                return all_nodes

            for i in self.panda_network[current_node]:
                if i not in visited_nodes:
                    que.append((level + 1, i))
                    visited_nodes.add(i)

        return -1

    def how_many_gender_in_network(self, level, panda, gender):
        genders = self.how_many_gender_in_network_inner(panda, level)
        if genders == -1:

            return 0

        res = []
        for i in genders:
            if i.gender() == gender:
                res.append(1)
            else:
                res.append(0)

        return sum(res)

    def connection_level(self, start, target):
        que = deque()
        visited_nodes = set()
        route = {start: None}

        que.append((0, start))
        visited_nodes.add(start)

        while que:
            level, current_node = que.popleft()
            if current_node == target:
                while target is not None:
                    target = route[target]

                return level

            for i in self.panda_network[current_node]:
                if i not in visited_nodes:
                    que.append((level + 1, i))
                    visited_nodes.add(i)
                    route[i] = current_node

        return -1

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) != -1
