class Solution(object):
    def reverseWords(self, s):
        return " ".join(words[::-1] for words in s.split())