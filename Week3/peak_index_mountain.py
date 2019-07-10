class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Idea: Use binary search, find middle index and check if the  
        start = 0
        end = len(A) - 1
        while start < end:
            mid = (start + end) // 2
            if A[mid] > A[mid + 1] and A[mid] > A[mid -1]:
                return mid
            elif A[mid] < A[mid + 1]:
                start = mid + 1
            else: 
                end = mid - 1
        return start # If it exits that means start and end are on the same index
                
            