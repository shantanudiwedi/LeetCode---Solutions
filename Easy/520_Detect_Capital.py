##Q520 Detect Capital

class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper() or word.islower() or word.istitle():
            return True
        return False
