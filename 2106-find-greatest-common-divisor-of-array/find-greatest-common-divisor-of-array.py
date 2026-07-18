class Solution(object):
    def findGCD(self, nums):
        nums.sort()
        x=len(nums)
        max=0
        for i in range (1,(nums[0]+1)):
            if (nums[0])  %i==0 and (nums[x-1]) %i==0:
               max=i
        return max 


        