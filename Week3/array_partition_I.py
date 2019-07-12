class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Idea: Sort the input array and then iterate through the list. At even indices add the min of the value at that index and the next to a sum variable. If its at an odd index continue.
        nums.sort()
        result = 0
        if len(nums) == 0:
            return 0
        for i, number in enumerate(nums):
            if i % 2 == 0:
                result += min(number, nums[i+1])
           
        return result
             