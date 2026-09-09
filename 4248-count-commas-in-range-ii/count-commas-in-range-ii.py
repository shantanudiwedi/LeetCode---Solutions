class Solution(object):
    def countCommas(self, n):
        total = 0
        range_start = 1000       # numbers below this have 0 commas
        comma_count = 1
        while range_start <= n:
            range_end = min(n, range_start * 1000 - 1)
            total += (range_end - range_start + 1) * comma_count
            range_start *= 1000
            comma_count += 1
        return total
        