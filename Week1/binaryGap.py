class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        # General Idea: Convert N to a binary number and then iterate through and append the distances to a list and take the max of the list.
        result = []
        binary = bin(N)
        consecutive = 0 # track consecutive
        dist = 0 # track length between 
        for bit in binary:
            if bit == "1":
                consecutive += 1
            if bit == "0" and consecutive == 1:
                dist += 1
            if consecutive == 2:
                dist += 1
                result.append(dist)
                consecutive = 1
                dist = 0
        if not result:
            return 0
        return max(result)