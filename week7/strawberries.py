from copy import deepcopy


def strawberries(rows, columns, days, dead_strawberries):
    matrix = []
    count = 0
    for i in range(0 ,rows):
        matrix.append(deepcopy([0 for j in range(0 ,columns)]))
    for coords in dead_strawberries:
        matrix[coords[0]][coords[1]] = 'r'
    while count != days:
        count += 1
        matrix = rot_new_matrix(matrix)
    return matrix

def rot_berries(i, j, matrix):
    result = matrix
    if i != 0:
        result[i - 1][j] = 'r'
    if i != len(matrix) - 1:
        result[i + 1][j] = 'r'
    if j != 0:
        result[i][j - 1] = 'r'
    if j != len(matrix[0]) - 1:
        result[i][j + 1] = 'r'
    return result

def rot_new_matrix(matrix):
    count = 0
    result = matrix
    for i in range(0 , len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 'r':
                result = rot_berries(i, j, matrix)
    return result

def main():
    result = strawberries(10, 10, 1, [[5, 5], [7, 7]])
    for i in result:
        print(i)


main()