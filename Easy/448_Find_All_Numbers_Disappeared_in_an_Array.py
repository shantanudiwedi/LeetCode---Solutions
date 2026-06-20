##Q448 Find All Numbers Disappeared in an Array

class Solution(object):
    def findDisappearedNumbers(self, nums):
        num = set(nums)
        list=[]
        for i in range (1 ,(len(nums)+1)):
            if i not  in num :
                list.append(i)
        return list
