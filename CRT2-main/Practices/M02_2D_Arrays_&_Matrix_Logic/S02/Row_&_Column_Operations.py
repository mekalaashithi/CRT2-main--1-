from typing import List
def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    for row in image:
        row.reverse()
        for i in range(len(row)):
            row[i]=1 if row[i]==0 else 0
    return image
image=[[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))