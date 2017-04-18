from functools import reduce


ALIVE = 1
DEAD = 0


def strawberries(rows, columns, days, dead_strawberries):
    if rows < 1 or rows > 1000:
        raise ValueError()
    if columns < 1:
        raise ValueError()
    if rows > columns:
        raise ValueError()
    matrix = [[ALIVE for i in range(columns)] for j in range(rows)]

    for strawberry in dead_strawberries:
        matrix[strawberry[0]][strawberry[1]] = DEAD

    for day in range(days):
        for item in dead_strawberries:
            if check_neighbours((item[0] - 1, item[1]), (rows, columns)):
                matrix[item[0] - 1][item[1]] = DEAD
            if check_neighbours((item[0], item[1] - 1), (rows, columns)):
                matrix[item[0]][item[1] - 1] = DEAD
            if check_neighbours((item[0], item[1] + 1), (rows, columns)):
                matrix[item[0]][item[1] + 1] = DEAD
            if check_neighbours((item[0] + 1, item[1]), (rows, columns)):
                matrix[item[0] + 1][item[1]] = DEAD
        dead_strawberries = [(row, col) for row in range(rows)
                             for col in range(columns)
                             if matrix[row][col] == DEAD]

    return sum(reduce(lambda x, y: x + y, matrix))


def check_neighbours(index, length):
    return bool(index[0] >= 0 and index[0] < length[0] and
                index[1] >= 0 and index[1] < length[1])


def has_dead_neighbours(index, length, matrix):
    return bool(index[0] >= 0 and index[0] < length[0] and
                index[1] >= 0 and index[1] < length[1]) and \
        bool(index[0] >= 0 and index[0] < length[0] and
             index[1] >= 0 and index[1] < length[1]) and \
        bool(index[0] >= 0 and index[0] < length[0] and
             index[1] >= 0 and index[1] < length[1]) and \
        bool(index[0] >= 0 and index[0] < length[0] and
             index[1] >= 0 and index[1] < length[1])
