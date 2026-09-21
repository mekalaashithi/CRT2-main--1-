from typing import List

def setZeroes(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not matrix[0]:
        return matrix

    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix


if __name__ == "__main__":
    matrix = []
    while True:
        line = input()
        if not line.strip():
            break
        matrix.append(list(map(int, line.split())))

    print(setZeroes(matrix))