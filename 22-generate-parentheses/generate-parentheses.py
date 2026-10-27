class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def backtrack(cur, open_, close):
            if len(cur) == 2 * n:
                res.append(cur)
                return
            if open_ < n:
                backtrack(cur + "(", open_ + 1, close)
            if close < open_:
                backtrack(cur + ")", open_, close + 1)

        backtrack("", 0, 0)
        return res