class Solution(object):
    def removeDuplicates(self, s):
        output = []
        for letters in s :
            if not output or letters!=output[-1]:
                output.append(letters)
            else :
                output.pop()
        return "".join(output)