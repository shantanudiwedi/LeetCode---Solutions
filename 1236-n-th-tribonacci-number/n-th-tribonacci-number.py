class Solution(object):
    def tribonacci(self, n):
        
        if n == 0 :
            return 0
        elif n == 1:
            return 1 
        elif n == 2:
            return 1 
        a=0
        b=1
        c=1
        for _ in range(3 ,n+1):
            t = a+b+c
            a=b
            b=c
            c=t
        return t
        