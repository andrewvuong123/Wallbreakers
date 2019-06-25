class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        for i in range(length):
            if i+1 > length-1:
                return nums[i]
            if nums[i] == nums[i+1] or nums[i] == nums[i-1]:
                continue;
            else:
                return nums[i]