class Solution(object):
    def romanToInt(self, s):
        output = 0
        roman = { "I" : 1,
        "V" : 5, 
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500, 
        "M" : 1000}
    
        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                output -= roman[s[i]]
            else:
                output += roman[s[i]]

        return output

        