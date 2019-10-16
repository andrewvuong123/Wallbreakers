class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # General Idea: Sort the list intervals and set pointers to the start/end range. Once you hit a point that is not within the range then increment how many arrows are needed.
        if not points: 
            return 0
        points.sort()
        arrows = 1
        start = points[0][0]
        end = points[0][1]
        for i in range(len(points)):
            # If points are within the interval update start and end to current points
            if points[i][0] >= start and points[i][1] <= end:
                start = points[i][0]
                end = points[i][1]
            # If start is within overlap, update start to new starting point
            elif points[i][0] <= end:
                start = points[i][0]
            # If not within overlap, update new start and end points and increment arrow count
            else:
                start = points[i][0]
                end = points[i][1]
                arrows += 1
        return arrows
        