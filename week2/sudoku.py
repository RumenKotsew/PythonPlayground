def _inner(sudoku):
    res = []
    for i in range(len(sudoku[0])):
        res.append([0] * len(sudoku))
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            res[j][i] = sudoku[i][j]
    return res


def _check_matrix(row, col, sudoku):
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    index1 = 0
    index2 = 0
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            matrix[index1][index2] = sudoku[i][j]
            index2 += 1
        index1 += 1
        index2 = 0
    res = sorted([v for arr in matrix for v in arr])
    return res == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sudoku_solved(sudoku):
    numbers_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for item in sudoku:
        if sorted(item) != numbers_arr:
            return False
    for item in _inner(sudoku):
        if sorted(item) != numbers_arr:
            return False
    for row in range(6, 3):
        for col in range(6, 3):
            if _check_matrix(row, col, sudoku) is False:
                return False
    return True
