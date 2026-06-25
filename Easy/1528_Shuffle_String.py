class Solution(object):
    def restoreString(self, s, indices):
        ans = [""] * len(s)

        for i in range(len(s)):
            ans[indices[i]] = s[i]

        return "".join(ans)
