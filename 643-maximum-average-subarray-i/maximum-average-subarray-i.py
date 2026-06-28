class Solution(object):
    def findMaxAverage(self, nums, k):
        sum_window = sum(nums[0:k])
        max_window = sum_window
        for i in range (k,len(nums)):
            sum_window+=nums[i]-nums[i-k]
            max_window = max(max_window , sum_window)
        return max_window/float(k)