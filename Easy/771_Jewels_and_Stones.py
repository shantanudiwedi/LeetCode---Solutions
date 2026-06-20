##Q771 Jewels and Stones

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
         count1 = {}
         count2= {}
         output = 0
         for letters in jewels :
            count1[letters]= count1.get(letters,0)+1
         for letters in stones:
            count2[letters]= count2.get(letters,0)+1
         for keys in count1 :
            if keys in count2:
                output+=count2[keys]
         return output
