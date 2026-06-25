class Solution:
    def twoSum(self, nums, target):
        seen = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[nums[i]] = i
        
        
        