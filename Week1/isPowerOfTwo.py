class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # General Idea: A number is a power of two if dividing by two gets you to one eventually. While n is greater than 1 keep dividing by two and if it doesn't equal one return false else it is a power.
        n = float(n)
        while n >= 1:
            if n == 1:
                return True
            n = n / 2
        return False