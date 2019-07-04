class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for stone in S:
            for jewel in J:
                if stone == jewel:
                    count += 1
        return count
                    
class Solution_2(object):
    def numJewelsInStones_2(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = {}
        for i in J:
            jewels[i] = 0
        for stone in S:
            if stone in jewels:
                jewels[stone] += 1
        return sum(jewels.values())