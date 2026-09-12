class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        a = nums[0]
        b = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            c = max(b, a + nums[i])
            a = b
            b = c
        return b
        