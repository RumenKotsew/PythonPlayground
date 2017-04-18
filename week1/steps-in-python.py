def sum_of_digits(number):
    result = 0
    number = abs(number)
    number = str(number)
    for i in number:
        result += int(i)
    return result


def to_digits(number):
    result = []
    while number > 0:
        result.insert(0, number % 10)
        number = number // 10

    return result


def to_number(digits):
    number = 0
    for i in range(0, len(digits)):
        if i != 0:
            number = (number * 10) + digits[i]
        else:
            number = number + digits[i]

    return number


def count_vowels(string):
    string = string.lower()
    counter = 0
    vowels = ["a", "i", "u", "o", "e", "y"]

    for char in string:
        if char in vowels:
            counter = counter + 1

    return counter


def count_consonants(string):
    string = string.lower()
    result = 0
    vowels = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

    for char in string:
        if char in vowels:
            result += 1

    return result


def prime_number(number):
    for i in range(1, number + 1):
        if (number % i) == 0 and i != number and i != 1:
            return False
    return True


def fact_digits(n):
    n = str(n)
    total_sum = 0
    for i in range(0, len(n)):
        total_sum += fact(int(n[i]))

    return total_sum


def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def fibonacci(number):
    arr = []
    for iterator in range(0, number):
        if iterator == 0 or iterator == 1:
            arr.append(1)
        else:
            arr.append(arr[iterator - 1] + arr[iterator - 2])

    return arr


def palindrome(string):
    flag = False
    string = str(string)
    for char_number in range(0, len(string)):
        if string[(len(string) - char_number) - 1] == string[char_number]:
            flag = True
        else:
            flag = False
            break

    return flag


def char_histogram(input_string):
    result_dict = {}
    for char in input_string:
        if char not in result_dict:
            result_dict[char] = 1
        else:
            result_dict[char] += 1
    return result_dict
