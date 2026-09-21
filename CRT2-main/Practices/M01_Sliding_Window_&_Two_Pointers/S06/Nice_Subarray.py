'''class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k):
            if k < 0:
                return 0

            left = 0
            total = 0
            ans = 0

            for right in range(len(nums)):
                total += nums[right]

                while total > k:
                    total -= nums[left]
                    left += 1

                ans += right - left + 1

            return ans

        return atMost(goal) - atMost(goal - 1)'''


'''class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def sub_arr(target):
            left,count,odd=0,0,0
            for right in range(len(nums)):
                if nums[right]%2==1:
                    odd+=1
                while odd>target:
                    if nums[left]%2==1:
                        odd-=1
                    left+=1
                count+=(right-left+1)
            return count
        return sub_arr(k)-sub_arr(k-1)'''