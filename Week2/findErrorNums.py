from collections import Counter

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # General Idea: Initialize a counter with data from nums, iterate through len of nums and find the count with 2 and 0 and return the result.
        result = [0, 0] 
        c = Counter(nums)
        for digit in range(len(nums)+1):
            if c[digit] == 2:
                result[0] = digit
            if c[digit] == 0:
                result[1] = digit
        return result