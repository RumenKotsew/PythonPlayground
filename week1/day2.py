def count_substrings(haystack, needle):
    if haystack is None:
        raise Exception('Illegal Arguments!')
    else:
        return __count_substrings_recursive(0, haystack, needle)


def __count_substrings_recursive(res, haystack, needle):
    if needle not in haystack:
        return res
    else:
        mirror_stack = haystack.replace(needle, str(hash(needle)), 1)
        res += 1
        return __count_substrings_recursive(res, mirror_stack, needle)


def sum_matrix(matrix):
    total_sum = 0
    for i in matrix:
        total_sum = total_sum + sum(i)
    return total_sum


def nan_expand(times):
    if times > 0:
        string = "NaN"
        newstr = string
        while times > 0:
            times = times - 1
            newstr = newstr[:0] + "Not a " + newstr[0:]
        return newstr
    else:
        return ""


def prime_factorization(n):
    arr = []
    res = []
    count = 0
    m = n
    for i in range(2, n):
        if n == 0:
            break
        while n % i == 0:
            arr.append([i, 1])
            n = n // i
    for j in range(2, m):
        if [j, 1] in arr:
            while [j, 1] in arr:
                for k in range(0, len(arr)):
                    if k < len(arr) and arr[k][0] == j:
                        arr.pop(k)
                        count += 1
            res.append((j, count))
            count = 0
    return res


def group(arr):
    final_arr = []
    counter = 0

    for i in range(0, len(arr)):
        if i != (len(arr) - 1):
            if arr[i] != arr[i + 1]:
                final_arr.append(arr[counter:(i + 1)])
                counter = i + 1
        else:
            final_arr.append(arr[counter:len(arr)])
    return final_arr


def max_consecutive(arr):
    counter = 0
    result = 0

    for i in range(0, len(arr)):
        if i != (len(arr) - 1):
            if arr[i] != arr[i + 1]:
                if result < (i - counter):
                    result = (i - counter)
                counter = i
        else:
            if result < (len(arr) - counter - 1):
                result = (len(arr) - counter - 1)
    return result


def word_counter(word, grid):
    result = 0
    directions_arr = ['upperleft', 'up', 'upperright', 'left', 'right',
                      'lowerleft', 'down', 'lowerright']
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            if grid[x][y] == word[0]:
                print("hit i")
                for direction in directions_arr:
                    result += recursive(word, grid, x, y, direction, 0)
    return result


def recursive(word, grid, x, y, direction, counter):
    if validate_coordinates(grid, x, y, direction):
        new_coords = create_new_coords(direction, x, y)
        new_x = new_coords[0]
        new_y = new_coords[1]
        if grid[new_x][new_y] == word[len(word) - 1] and \
                counter == word[len(word) - 1]:
            return 1
        if grid[new_x][new_y] == word[counter]:
            return recursive(word, grid, new_x, new_y,
                             direction, counter + 1)
    return 0


def create_new_coords(direction, x, y):
    if direction == 'upperleft':
        new_x = x - 1
        new_y = y - 1
    if direction == 'up':
        new_x = x - 1
        new_y = y
    if direction == 'upperright':
        new_x = x - 1
        new_y = y + 1
    if direction == 'left':
        new_x = x
        new_y = y - 1
    if direction == 'right':
        new_x = x
        new_y = y + 1
    if direction == 'lowerleft':
        new_x = x + 1
        new_y = y - 1
    if direction == 'down':
        new_x = x + 1
        new_y = y
    if direction == 'lowerright':
        new_x = x + 1
        new_y = y + 1
    return (new_x, new_y)


def validate_coordinates(grid, x, y, direction):
    if direction == 'upperleft':
        if x > 0 and y > 0:
            return True
        else:
            return False
    if direction == 'upperright':
        if x > 0 and y < len(grid[0]) - 1:
            return True
        else:
            return False
    if direction == 'lowerleft':
        if x < len(grid) - 1 and y > 0:
            return True
        else:
            return False
    if direction == 'lowerright':
        if x < len(grid) - 1 and y < len(grid[0]) - 1:
            return True
        else:
            return False
    if direction == 'up':
        if x > 0:
            return True
        else:
            return False
    if direction == 'left':
        if y > 0:
            return True
        else:
            return False
    if direction == 'down':
        if x < len(grid) - 1:
            return True
        else:
            return False
    if direction == 'right':
        if y < len(grid[0]) - 1:
            return True
        else:
            return False
    return False


print(prime_factorization(356))
