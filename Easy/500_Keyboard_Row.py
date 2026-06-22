##Q500 — Keyboard Row

class Solution(object):
    def findWords(self, words):
        ans=[]
        row1=set("qwertyuiop")
        row2=set("asdfghjkl")
        row3=set("zxcvbnm")
        for word in words:
           letter=set(word.lower())
           if letter<=row1 or letter<=row2 or letter<=row3:
               ans.append(word)
        return ans
