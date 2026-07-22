class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}
        stack = []
        for nums in nums2:
            while stack and stack[-1]<nums:
                popped = stack.pop()
                next_greater[popped]=nums 
            stack.append(nums)
        return [next_greater.get(n,-1)for n in nums1]