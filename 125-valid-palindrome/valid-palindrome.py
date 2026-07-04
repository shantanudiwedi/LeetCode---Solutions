class Solution(object):
    def isPalindrome(self, s):
        s=list(s)
        s2 = []
        for char in s : 
            if char.isalnum():
                s2.append(char)
            else :
                continue 
        i = 0 
        j = len(s2)-1
        while i<j:
            s2[i],s2[j]=s2[j],s2[i]
            i +=1
            j-=1
        s2 ="".join(s2).lower()
        i = 0
        j= len(s2)-1
        while i <j :
            if s2[i] != s2[j]:
                return False 
            else :
                i+=1
                j-=1
        return True 

        
