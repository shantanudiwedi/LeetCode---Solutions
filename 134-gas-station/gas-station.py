class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total = 0
        curr = 0
        start = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]

            if curr < 0:
                start = i + 1
                curr = 0

        if total < 0:
            return -1

        return start
        