class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, digit in enumerate(nums):
            for j in range(len(nums)):
                if digit + nums[j] == target:
                    if i != j:
                        return [i, j]
                

class Solution_2(object):
    def twoSum_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for i, digit in enumerate(nums):
            tar_num = target - digit 
            if tar_num in dictionary:
                return [dictionary[tar_num], i]
            dictionary[digit] = i