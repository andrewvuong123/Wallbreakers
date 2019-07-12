class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Idea: Sort all the intervals and check the end of the first interval with the start of the next interval. If they overlap merge by replacing the end of the first interval with the end of the next one and then pop the next interval off the list of lists. If they do not overlap move to the next interval and check again. Break when reach the end length of intervals.
        intervals.sort() # sort to make sure all intervals in increasing order
        curr = 0 # pointer to current interval we are checking
        for i in range(len(intervals) - 1):
            if intervals[curr][1] >= intervals[curr+1][0]: 
                if intervals[curr][1] > intervals[curr+1][1]:
                    intervals.pop(curr+1)
                else:
                    intervals[curr][1] = intervals[curr+1][1]
                    intervals.pop(curr+1)
            else:
                curr += 1
        return intervals
            