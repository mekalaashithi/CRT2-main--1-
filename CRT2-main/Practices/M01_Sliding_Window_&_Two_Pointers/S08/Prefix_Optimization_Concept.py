'''from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i + 1):
                curr_sum += nums[j]
            res[i] = curr_sum

        return res
'''
'''
#optimal solution:
nums=[1,2,3,4]
for i in range(1,len(nums)):
    nums[i]-nums[j-1]+nums[i]
print(res)'''

'''class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        alt=[0]*(n+1)
        for i in range(1,n+1):
            alt[i]=alt[i-1]+gain[i-1]
        return max(alt)'''
'''
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        left_sum=0
        for i in range(len(nums)):
            right_sum=total-nums[i]-left_sum
            if left_sum==right_sum:
                return i
            left_sum+=nums[i]
        return -1 '''