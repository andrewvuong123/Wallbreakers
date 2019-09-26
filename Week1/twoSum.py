class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # General Idea: Append each num - target to a set and then check to see if the original nums are in the set and append the index to the resulting list if it is.
        subtract = set()
        result = []
        for i in nums:
            subtract.add(target-i)
        for i, digit in enumerate(nums):
            if digit in subtract:
                result.append(i)
        if len(result) % 2 == 1: # If there is a num used twice
            for i in result:
                if nums[i] * 2 == target:
                    result.remove(i)
                    break
        return result
            