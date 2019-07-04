class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Idea: Create a set using nums1 array. Then loop through the second num array and if the number appears in the set append that to another set result and return the result set.
        
        common = set(nums1)
        result = set()
    
        for num in nums2:
            if num in common:
                result.add(num)
                
        return result