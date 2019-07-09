class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Idea: Sort the points list into ascending order and check to see if the start or end of each point is within the overlap. If it is update the overlap accordingly.
        
        if not points:
            return 0
        points.sort()
        arrows = 1 # start with one arrow
        start = points[0][0]
        end = points[0][1]
        for i in range(1, len(points)):  
            # if the current points is already within the overlap then update start and end 
            if points[i][1] <= end: 
                start = points[i][0]
                end = points[i][1]
            # if the start of the next points is within the overlap update start and keep the end.
            elif points[i][0] <= end: 
                start = points[i][0]
            # if its not within overlap at all then create new overlap interval and add an arrow
            else:
                start = points[i][0]
                end = points[i][1]
                arrows += 1
        return arrows
