##Q389 — Find the Difference

class Solution(object):
    def findTheDifference(self, s, t):
        dict1= { }
        dict2= { }
        for letters in s:
            dict1[letters]= dict1.get(letters,0)+1
        for letters in t:
            dict2[letters]= dict2.get(letters,0)+1

        for keys in dict2:
            if dict2[keys] != dict1.get(keys,0):
                return keys
