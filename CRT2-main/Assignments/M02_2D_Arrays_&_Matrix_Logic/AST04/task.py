def diagonalSort(mat):

    rows = len(mat)
    cols = len(mat[0])

    # Start from every column of the first row
    for col in range(cols):

        values = []
        i = 0
        j = col

        # Collect diagonal elements
        while i < rows and j < cols:
            values.append(mat[i][j])
            i += 1
            j += 1

        # Sort the diagonal
        values.sort()

        # Put sorted values back
        i = 0
        j = col

        while i < rows and j < cols:
            mat[i][j] = values[i]
            i += 1
            j += 1

    # Start from every row of the first column
    for row in range(1, rows):

        values = []
        i = row
        j = 0

        # Collect diagonal elements
        while i < rows and j < cols:
            values.append(mat[i][j])
            i += 1
            j += 1

        # Sort the diagonal
        values.sort()

        # Put sorted values back
        i = row
        j = 0

        while i < rows and j < cols:
            mat[i][j] = values[i - row]
            i += 1
            j += 1

    return mat


if __name__ == '__main__':
    m, n = map(int, input().split())

    mat = []

    for i in range(m):
        mat.append(list(map(int, input().split())))

    print(diagonalSort(mat))