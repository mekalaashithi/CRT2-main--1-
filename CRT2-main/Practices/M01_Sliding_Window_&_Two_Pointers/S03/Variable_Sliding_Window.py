'''from typing import List
def minSubArrayLen(self, target: int, nums: list[int]) -> int:
    left = 0
    curr_sum = 0
    min_len = float('inf')
    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len
target=7
nums=[2,3,1,2,4,3]
print(minSubArrayLen(target,nums))'''

from typing import List
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    left = 0
    c = 0
    p = 1
    for right in range(len(nums)):
        p *= nums[right]
        while p >= k:
            p //= nums[left]
            left += 1
        c += (right - left + 1)
    return c

nums = [10, 5, 2, 6]
k = 100
print(numSubarrayProductLessThanK(nums, k))


class Solution:
    def totalFruit(self, fruits):
        left = 0
        fruit_count = {}
        max_fruits = 0
        for right in range(len(fruits)):
            fruit = fruits[right]
            fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
            while len(fruit_count) > 2:
                left_fruit = fruits[left]
                fruit_count[left_fruit] -= 1
                if fruit_count[left_fruit] == 0:
                    del fruit_count[left_fruit]
                left += 1
            max_fruits = max(max_fruits, right - left + 1)
        return max_fruits