class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
       # General Idea: Intersection <=> Appears in both arrays. Can append nums1 to a set and compare with nums2 to see if numbers in nums2 are in the set.
        
        intersection = set()
        result = set()
        for i in nums1:
            intersection.add(i)
        for i in nums2:
            if i in intersection:
                result.add(i)
        return result    