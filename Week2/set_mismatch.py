from collections import Counter

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Idea: Create a counter from the nums list to get count of each number. Loop through the length of nums and check to find the number that has a count of 0 or 2 and append it to a result list. Then return the result
       
        c = Counter(nums)
        result = [0] * 2
        for nums in range(1, len(nums)+1):
            if c[nums] == 2:
                result[0] = nums
            if c[nums] == 0:
                result[1] = nums
        return result
         