##Q645 — Set Mismatch

class Solution(object):
    def findErrorNums(self, nums):
        count = {}
        list=[]
        for num in nums :
            count[num]= count.get(num,0)+1
        for keys in count :
            if count[keys]==2:
                list.append(keys)
        for num in range (1,len(nums)+1):
            if num not in count:
                list.append(num)
        return list
        
