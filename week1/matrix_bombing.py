from copy import deepcopy


def sum_matrix(m):
    return sum(i for row in m for i in row)


def validate_neighbours(index, n, m):
    if index[0] < 0 or index[0] >= n or index[1] < 0 or index[1] >= m:
        return False
    else:
        return True


def bomb_neighbours(node, m):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if validate_neighbours((node[0] + i,
                                    node[1] + j),
                                   len(m), len(m[0])) \
                    and (node[0] + i, node[1] + j) != node:
                target = m[node[0] + i][node[1] + j] - m[node[0]][node[1]]
                m[node[0] + i][node[1] + j] = max(0, target)

    return sum_matrix(m)


def matrix_bombing_plan(m):
    res = {}

    for row in range(len(m)):
        for col in range(len(m[row])):
            res[(row, col)] = bomb_neighbours((row, col), deepcopy(m))

    return res
