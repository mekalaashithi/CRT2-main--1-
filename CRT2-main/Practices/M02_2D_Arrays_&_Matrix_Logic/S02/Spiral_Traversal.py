from typing import List

def spiralOrder(matrix):
    rows,cols = len(matrix),len(matrix[0])
    
    top,bottom = 0,rows - 1
    left,right = 0,cols - 1

    ans = []

    while top <= bottom and left <= right:

        # left -> right
        for col in range(left, right + 1):
            ans.append(matrix[top][col])
        top += 1

        # top -> bottom
        for row in range(top, bottom + 1):
            ans.append(matrix[row][right])
        right -= 1

        # right -> left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                ans.append(matrix[bottom][col])
            bottom -= 1

        # bottom -> top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                ans.append(matrix[row][left])
            left += 1

    return ans
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))
#59
def generateMatrix( n: int) -> List[List[int]]:
    left=0
    right=n-1
    top=0
    bottom=n-1
    num=1
    res=[[0]*n for i in range(n)]
    while top<=bottom and left<=right:
        for col in range(left, right + 1):
            res[top][col]=num
            num+=1
        top += 1

    # top -> bottom
        for row in range(top, bottom + 1):
            res[row][right]=num
            num+=1
        right -= 1

    # right -> left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                res[bottom][col]=num
                num+=1
            bottom -= 1

    # bottom -> top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                res[row][left]=num
                num+=1
            left += 1

    return res
n=3
print(generateMatrix(n))