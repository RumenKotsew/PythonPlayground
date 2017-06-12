class Permutations(object):

    def histogram(self, item):
        res = {}
        for i in item:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        return res

    def is_permutation(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        dict1 = self.histogram(str1)
        dict2 = self.histogram(str2)
        return dict1 == dict2
