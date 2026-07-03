class Solution(object):
    def maxVowels(self, s, k):
        vowels = set("aeiou")
        count = sum(1 for c in s[:k] if c in vowels)
        max_len = count
        left = 0
        
        for right in range(k, len(s)):
            if s[right] in vowels:
                count += 1
            if s[left] in vowels:
                count -= 1
            left += 1
            max_len = max(max_len, count)
        
        return max_len