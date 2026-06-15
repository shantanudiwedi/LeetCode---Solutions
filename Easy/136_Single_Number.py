##136 Single Number

class Solution(object):
    def singleNumber(self, nums):
        count = {}
        for n in nums:
            count[n]= count.get(n,0)+1
        for keys in count :
            if count[keys]==1 :
                return keys  
        
