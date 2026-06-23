##Q575 Distribute Candies

class Solution(object):
    def distributeCandies(self, candyType):
        candy = set(candyType)
        target = (len(candyType))//2 
        if len(candy)<= target:
            return (len(candy))
        else:
            return (target) 
