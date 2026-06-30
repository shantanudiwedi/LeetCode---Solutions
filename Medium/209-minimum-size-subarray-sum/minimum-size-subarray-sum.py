class Solution(object):
    def minSubArrayLen(self, target, nums):
        total=0
        left = 0
        mini = float('inf')
        for right in range (len(nums)):
            total += nums[right]
            while total >=target:
                mini = min(mini, right - left+1)
                total -= nums[left]
                left+=1
        return mini if mini!=float('inf') else 0