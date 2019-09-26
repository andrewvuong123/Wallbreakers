class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # General Idea: Use the reverse function to flip each inner list and then flip the 1s and 0s using an if statement.
        
        for i, list in enumerate(A):
            A[i].reverse();
            for j, num in enumerate(A[i]):
                if num == 1:
                    A[i][j] = 0;
                else:
                    A[i][j] = 1;            
        return A