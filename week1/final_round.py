def is_number_balanced(m):
    left_side = 0
    right_side = 0
    n = str(m)
    left_side_arr = []
    right_side_arr = []
    left_sum = 0
    right_sum = 0
    if len(n) % 2 == 0:
        for left_side_iterator in range(0, len(n) // 2):
            left_side_arr.append(n[left_side_iterator])
        for right_side_iterator in range(len(n) // 2, len(n)):
            right_side_arr.append(n[right_side_iterator])
        for iterator in range(0, len(left_side_arr)):
            left_sum = left_sum + int(left_side_arr[iterator])
            right_sum = right_sum + int(right_side_arr[iterator])
        if right_sum == left_sum:
            return True
        else:
            return False
    if len(n) % 2 != 0:
        for i in range(0, len(n)):
            if i == len(n) // 2:
                for j in range(0, i + 1):
                    left_side = left_side + int(n[j])
            if i == len(n) - 1:
                for k in range(len(n) // 2, len(n)):
                    right_side = right_side + int(n[k])
        if right_side == left_side:
            return True
        else:
            return False


def increasing_or_decreasing(seq):
    prev = seq[0]
    flag_up = True
    flag_down = True
    for i in seq[1:]:
        if i > prev:
            prev = i
            flag_down = False
        elif i < prev:
            prev = i
            flag_up = False
        else:
            flag_down = flag_up = False

    if flag_down:
        return "Down!"
    elif flag_up:
        return "Up!"
    else:
        return False


def get_largest_palindrome(n):
    for i in range(n - 1, -1, -1):
        if str(i) == str(i)[::-1]:
            return i


def sum_of_numbers(st):
    res = 0
    counter = 0
    try:
        int(st)
        return int(st)
    except ValueError:
        pass
    for index in range(len(st)):
        try:
            int(st[index])
            counter += 1
            if counter == 1:
                res = int(st[index])
            cache = int(st[index])
            for consecutive in range(index + 1, len(st)):
                if int(st[consecutive]):
                    cache = cache * 10
                    cache += int(st[consecutive])
                    res += cache
                else:
                    break
        except ValueError:
            continue
    return res


def birthday_ranges(birthdays, ranges):
    result = []
    count = - 1
    for brange in ranges:
        count += 1
        result.append(0)
        for i in birthdays:
            if i in range(brange[0], brange[1] + 1):
                result[count] += 1
    return result


birthdays = [1, 2, 3, 4, 5]
ranges = [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]


def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


def numbers_to_message(pressed_sequence):
    next_capital = False
    res = []
    symbol = []
    lastitem = pressed_sequence[0]
    pressed_sequence.append('end')
    for item in pressed_sequence:
        if item == '-1' or item != lastitem or item == 'end':
            letter = _parse_symbol(symbol)
            symbol = []
            if letter == 'capital':
                next_capital = True
                letter = None
            if letter:
                if next_capital is True:
                    letter = letter.upper()
                    next_capital = False
                res.append(letter)

        lastitem = item
        symbol.append(item)

    return ''.join(res)


def _parse_symbol(symbol):
    alphabet = [[None],
                ['a', 'b', 'c', 'over1'],
                ['d', 'e', 'f', 'over2'],
                ['g', 'h', 'i', 'over3'],
                ['j', 'k', 'l', 'over4'],
                ['m', 'n', 'o', 'over5'],
                ['p', 'q', 'r', 's', 'over6'],
                ['t', 'u', 'v', 'over7'],
                ['w', 'x', 'y', 'z', 'over8'],
                [' ', ' ', ' ', ' ', 'over9']]
    length = (len(symbol) - 1) % 3
    if symbol[0] == 7:
        length -= 1
    if symbol[0] == 1:
        return 'capital'
    if symbol == [-1]:
        return ""
    letter_number = symbol[0] - 1
    if symbol[0] == 0:
        return alphabet[9][length]
    return alphabet[letter_number][length]


def message_to_numbers(message):
    res = []
    previous = None

    alphabet = {0: ' ',
                2: ['a', 'b', 'c'],
                3: ['d', 'e', 'f'],
                4: ['g', 'h', 'i'],
                5: ['j', 'k', 'l'],
                6: ['m', 'n', 'o'],
                7: ['p', 'q', 'r', 's'],
                8: ['t', 'u', 'v'],
                9: ['w', 'x', 'y', 'z']}

    for letter in list(message):
        if letter == " ":
            res.append(0)
        else:
            if letter.isupper() is True:
                res.append(1)
                letter = letter.lower()
            for item in alphabet.items():
                if letter in item[1]:
                    if previous == item[0]:
                        res.append(-1)
                    for i in range(item[1].index(letter) + 1):
                        res.append(item[0])
                    previous = item[0]
    return res
