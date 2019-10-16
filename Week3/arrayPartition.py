class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # General Idea: Sort nums and then iterate through and add the min of each pair to a total sum count.
        
        result = 0
        nums.sort()
        for digit in range(0, len(nums), 2):
            min_pair = min(nums[digit], nums[digit] + 1)
            result = result + min_pair
        return result