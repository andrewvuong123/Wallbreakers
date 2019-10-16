class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # General Idea: Recursively multiply x on itself, base case is when n is 1, if n is negative recursively multiply 1/x on itself.
        
        if n < 1:
            if n == -1:
                return 1/x
            else:
                return 1/x * self.myPow(x, n+1)
        else:
            if n == 1:
                return x
            else:
                return x * self.myPow(x, n-1)