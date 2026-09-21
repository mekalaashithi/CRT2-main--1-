from typing import List

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    res = [[rStart, cStart]]

    # directions: east, south, west, north
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    direction = 0
    step = 1

    r = rStart
    c = cStart

    while len(res) < rows * cols:

        # east/south or west/north
        for _ in range(2):

            dr, dc = directions[direction]

            for _ in range(step):
                r += dr
                c += dc

                # add only if inside the grid
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])

            direction = (direction + 1) % 4

        # increase spiral size
        step += 1

    return res


if __name__ == '__main__':
    rows, cols, rStart, cStart = map(int, input().split())
    print(spiralMatrixIII(rows, cols, rStart, cStart))