'''1652. Defuse the Bomb'''
'''class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[0]*n
        if k==0:
            return res
        elif k>0:
            win_sum=0
            for i in range(1,k+1):
                win_sum+=code[i%n]
            for j in range(n):
                res[j]=win_sum
                win_sum-=code[(j+1)%n]
                win_sum+=code[(j+k+1)%n]
            return res
        else:
            k=-k
            win_sum=0
            for i in range(1,k+1):
                win_sum+=code[(-i)%n]
            for j in range(n):
                res[j]=win_sum
                win_sum-=code[(j-k)%n]
                win_sum+=code[(j)%n]
            return res'''