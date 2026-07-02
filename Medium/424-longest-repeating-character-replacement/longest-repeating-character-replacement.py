class Solution(object):
    def characterReplacement(self, s, k):
        store={}
        max_len=0
        left=0
        for right in range(len(s)):
            store[s[right]] = store.get(s[right], 0) + 1
    
            while (right - left + 1) - max(store.values()) > k:
                store[s[left]] -= 1
                if store[s[left]] == 0:
                    del store[s[left]]
                left += 1
    
            max_len = max(max_len, right - left + 1)
        
        return max_len


        