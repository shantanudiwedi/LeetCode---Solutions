class Solution(object):
    def firstUniqChar(self, s):
        count = { }
        for letters in s :
            count[letters]= count.get(letters,0)+1
        for i in range (len(s)):
            if count[s[i]]==1:
                return i
        
        return (-1)        