class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # General Idea: Can put the unique amount of candies into a set and see if there are enough for sister to get a different piece equally. Else can just return how many unique candies there are.
        if not candies:
            return 0
        unique = set(candies)
        amount = len(candies) / 2
        if len(unique) < amount:
            return len(unique)
        else:
            return amount