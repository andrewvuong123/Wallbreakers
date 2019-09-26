class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
       # General Idea: Nested loop through row and col. Each outer iteration resets transpose list and inner loop creates new transposed inner list. Append the transposed list to result after each inner loop is done.
    
        result = []
        for i in range(0, len(A[0])):
            transpose = []
            for j in range(0, len(A)):
                transpose.append(A[j][i])
            result.append(transpose)
        return result
                