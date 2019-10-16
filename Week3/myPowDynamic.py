class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # General Idea: Recurse on half of n with positive/negative values if n is greater or less than 0. If n is an even number then you can just return the product of the positive/negative values, else you can get the product multiplied by one more.
        
        if n == 0:
            return 1
        if n < 0:
            negative = self.myPow(x, -n/2) # can convert it to positive and then take inverse later
        elif n > 0:
            positive = self.myPow(x, n/2)
            
        if n % 2 == 0:
            if n < 0:
                return 1/(negative * negative)
            return positive * positive
        else:
            if n < 0:
                return 1/(negative * negative * x)
            return positive * positive * x
            