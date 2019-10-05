class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # General Idea: Map the jewels to a set and then iterate through each stone in S, if its in the jewel set then increment a counter.
        
        jewels = set()
        count = 0
        for jewel in J:
            jewels.add(jewel)
        for stone in S:
            if stone in jewels:
                count += 1
        return count        
        