 class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Idea: Base case if n reaches 0 just return one. Store two temp variables for negative and positive n that calls the function again but with half of n. If n is an even number then you can just return the product of the temp variable twice. Else if n is an odd number you can do the same thing with multiplying two halves of n and then multiplying by one more x. 
        if n == 0:
            return 1
        if n < 0:
            neg = self.myPow(x, -n/2) # calculate the positive value of n
        elif n > 0:
            temp = self.myPow(x, n/2)
            
        if n % 2 == 0:
            if n < 0:
                return 1/(neg*neg) # to inverse just return 1 divided by the positive calculation
            return temp * temp
        else:
            if n < 0:
                return 1/(x*neg*neg)
            return x * temp * temp