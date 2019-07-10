class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Idea: Keep pointers to the start/end indices of list as the upper/lower bounds. Initialize a mid var to get the index at the mid. If the target is found at the mid index then return that mid index. Else if the value at the mid index is lower than the target then set the lower bound to the mid index plus one and vice versa if it is higher than the target. Repeat till it is either found or if not return -1. 
        lower, higher = 0, len(nums)-1 
        while lower <= higher:
            mid = (lower + higher) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lower = mid + 1 
            else:
                higher = mid - 1
        return -1