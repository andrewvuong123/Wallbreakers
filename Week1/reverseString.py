class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Keep pointers to each end of the string and swap using temp variable until reaching the middle
        for i in range(0, len(s)//2):
            start = s[i]
            end = s[-i-1]
            s[i] = end
            s[-i-1] = start