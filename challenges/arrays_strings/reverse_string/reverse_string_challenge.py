class ReverseString(object):

    def reverse(self, chars):
        if chars is None:
            return chars
        if len(chars) == 1:
            return chars
        res = []
        [res.insert(0, i) for i in chars]
        return res
