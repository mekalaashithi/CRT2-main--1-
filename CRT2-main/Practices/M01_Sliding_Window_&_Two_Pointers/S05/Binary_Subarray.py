'''leetcode - 1493'''
from typing import List

def longestSubarray( nums: List[int]) -> int:
    left,zero,res = 0,0,0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero += 1

        while zero > 1:
            if nums[left]==0:
                zero -= 1
                left += 1
        res = max(res,right-left+1 )    
    return res - 1 
nums = [0,1,1,1,0,1,1,0,1]
print( longestSubarray(nums)) 


'''1004'''
def longestOnes(self, nums: List[int], k: int) -> int:
    left,zero,res = 0,0,0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero += 1

        while zero > k:
            if nums[left]==0:
                zero -= 1
            left += 1
        res = max(res,right-left+1 )    
    return res  

nums=[1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestSubarray(nums))

'''930'''