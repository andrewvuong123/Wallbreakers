class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # General Idea: Use binary search to split list in half, check on upper/lower half of list based on if median is larger/smaller than target. Keep searching until target is found or not.
        
        start = 0
        end = len(nums) - 1
        while start <= end :
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                return mid
        return -1