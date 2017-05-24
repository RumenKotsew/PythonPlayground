class CompressString(object):

    def compress_old(self, string):
        if string is None:
            return None
        res = [[string.count(i), i] for i in string]
        for i in res:
            if i[0] == 2:
                i[0] = i[1]

        tes = []
        for i in res:
            if i not in tes:
                tes.append(i)
            res.remove(i)
        result = ''.join(str(j) for i in tes for j in i)
        result = result.replace('1', '')
        return result

    def compress(self, string):
        if string is None:
            return None
        if not string:
            return ''

        count = 0
        previous = string[0]
        res = ''

        for i in string:
            if i == previous:
                count += 1
            else:
                res += self._combine(previous, count)
                previous = i
                count = 1

        res += self._combine(previous, count)
        res = res.replace('1', '')
        return res if len(res) < len(string) else string

    def _combine(self, previous, count):
        return previous + str(count)
