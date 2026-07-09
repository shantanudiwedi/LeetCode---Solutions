class Solution(object):
    def majorityElement(self, nums):
        count = {}
        for n in nums: 
            count[n]=count.get(n,0)+1
        max_count =0
        for keys in count:
            if count[keys]>max_count :
                max_count = count[keys]
        for keys in count:
            if count[keys]==max_count:
                return (keys) 