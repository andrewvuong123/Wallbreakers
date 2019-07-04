class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Idea: calculate numbers and add to a set, if the number is in the set then it has looped and is unhappy, else it does not loop and ends in a one. 
        seen = set()
        value = 0
        while n > 1:
            value = 0 # reset value number after each iteration
            numbers = list(str(n)) # list of digits
            for num in numbers:
                value = int(num)**2 + value
            if value in seen:
                return False
            seen.add(value)
            n = value
        if n == 1: # if n is 0 then return false else it should return true
            return True