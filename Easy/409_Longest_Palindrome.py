##Q409 — Longest Palindrome

class Solution(object):
    def longestPalindrome(self, s):
        total= 0
        count = { }
        for letters in s :
            count[letters]= count.get(letters,0)+1
        has_odd = False 
        for keys in count :
            if count[keys]%2==0 :
                total +=count[keys]
            else :
                total +=(count[keys]-1)
                has_odd = True 
        if has_odd:
            total+=1
        return total 
