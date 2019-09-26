class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # General Idea: Sort and then use xor to compare the number
        result = 0
        for i in nums:
            result ^= i
        return result
                
            