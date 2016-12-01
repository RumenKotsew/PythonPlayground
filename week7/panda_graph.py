class Node():
    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def is_male(self):
        if self.gender == 'male':
            return True
        else:
            return False

    def is_female(self):
        if self.gender == 'female':
            return True
        else:
            return False

    def __str__(self):
        return str(self.name) + ', ' + str(self.email)\
                   + ', ' + str(self.gender)

    def __eq__(self, other_panda):
        return self.__hash__() == other_panda.__hash__()

    def __hash__(self):
        return hash(self.name + self.email + self.gender)
