def diagonalDifference(arr):

    n = len(arr)

    left_sum = 0
    right_sum = 0

    for i in range(n):
        left_sum += arr[i][i]
        right_sum += arr[i][n - 1 - i]

    return abs(left_sum - right_sum)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)