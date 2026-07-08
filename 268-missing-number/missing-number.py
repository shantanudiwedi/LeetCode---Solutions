class Solution(object):
    def missingNumber(self, nums):
        i = 0 
        nums= sorted(nums)
        for i in range (len(nums)):
            if i != nums[i]:
               return i
           
        return len(nums)