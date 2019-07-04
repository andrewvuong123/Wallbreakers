class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # Idea: Add each candy into a set. Get the max amount of candy the sister can get by calculating half the length of the candies list. Use the length of the set and the number of candies the sister can get to calculate the max kinds of candy.
        
        if not candies:
            return 0
        unique = set(candies)
        amount = len(candies)/2    
        unique_len = len(unique)
        if unique_len < amount:
            return unique_len
        else:
            return amount
            
            