class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        evens = []
        odds = []
        for x in A:
            if x % 2 == 0:
                evens.append(x)
            else:
                odds.append(x)
        return evens + odds        
        