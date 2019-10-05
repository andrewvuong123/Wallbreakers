class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # General Idea: Happy number will either loop endlessy or get to one. Can calculate the value from n and add it to a set and keep recalculating to check if there is a cycle.
        
        seen = set()
        value = 0
        while n > 1:
            value = 0
            numbers = list(str(n)) 
            for num in numbers:
                value = int(num)**2 + value
            if value in seen:
                return False
            seen.add(value)
            n = value
        if n == 1: 
            return True