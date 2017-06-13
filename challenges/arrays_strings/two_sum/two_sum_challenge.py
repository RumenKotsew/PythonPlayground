class Solution(object):

    def two_sum(self, item, n):
        if item is None:
            raise TypeError
        if not item:
            raise ValueError
        for i in range(len(item)):
            for j in range(1, len(item)):
                if item[i] + item[j] == n:
                    return [i, j]
