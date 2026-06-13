## Q217 Contains duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        count = { }
        for num in nums :
            count[num] = count.get(num,0)+1
            if count[num] !=1:
                return True 
        return False 
