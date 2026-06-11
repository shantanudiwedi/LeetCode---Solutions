# LeetCode 167 - Two Sum II (Input Array Is Sorted)
class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1

        while i < j:
            total = numbers[i] + numbers[j]

            if total == target:
                return [i + 1, j + 1]
            elif total < target:
                i += 1
            else:
                j -= 1
