class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # General Idea: Sort the given intervals and then have a var curr for the interval we are checking against. Increment curr to next interval in list if there is no overlap, else set the end of the current interval to the end of the next and pop the next interval out of the list.
        intervals.sort()
        curr = 0
        for i in range(len(intervals)-1): 
            # If current interval is within prev interval, update end and pop current interval off 
            if intervals[curr][1] >= intervals[curr+1][0]:
                if intervals[curr][1] > intervals[curr+1][1]:
                    intervals.pop(curr+1)
                else:
                    intervals[curr][1] = intervals[curr+1][1]
                    intervals.pop(curr+1)
            else: # update current interval to next interval
                curr += 1
        return intervals
   