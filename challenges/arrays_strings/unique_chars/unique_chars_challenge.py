class UniqueChars(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        if string == '':
            return True
        res = set(string)
        return sorted(list(res)) == sorted(string)
