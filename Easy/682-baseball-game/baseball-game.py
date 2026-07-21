class Solution(object):
    def calPoints(self, operations):
        result = []
        for val in operations:
            if val.lstrip('-').isdigit():
                result.append(int(val))
            elif val == 'C':
                result.pop()
            elif val == 'D':
                result.append(result[-1]*2)      
            elif val == '+':
                result.append(result[-1]+result[-2])  
        total = sum(result)
        return total