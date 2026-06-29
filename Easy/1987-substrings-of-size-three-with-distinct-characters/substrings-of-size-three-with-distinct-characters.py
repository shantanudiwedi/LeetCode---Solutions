class Solution(object):
    def countGoodSubstrings(self, s):
        total = 0
        for i in range (0,len(s)):
            window=s[i : (i+3)] 
            if len(set(window))==3:
                total+=1
        return total
        
        