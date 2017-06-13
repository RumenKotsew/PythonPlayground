class Solution(object):

    def find_diff(self, s1, s2):
        s1 = sorted(s1)
        s2 = sorted(s2)
        [s2.remove(i) for i in s1]
        return s2[0]
