class Solution(object):

    def fizz_buzz(self, num):
        if num is None:
            raise TypeError
        if num is 0:
            raise ValueError
        res = ['1', '2']

        for i in range(3, num + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            if i % 3 != 0 and i % 5 != 0:
                res.append(str(i))
        return res
