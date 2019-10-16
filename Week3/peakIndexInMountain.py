class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # General Idea: Initialize a start/end variable and binary search by checking the mid of the list. If its greater than both whats before/after it then return that index, if its lower than the previous element then recheck on the lower half of the list, else recheck on the upper half.
        
        start = 0
        end = len(A) - 1
        while start < end:
            mid = (start + end) // 2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] < A[mid-1]:
                end = mid - 1
            elif A[mid] < A[mid+1]:
                start = mid + 1
        return start 
            
                