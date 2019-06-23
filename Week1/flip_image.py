class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for list in range(len(A)):
            A[list].reverse()
        for i, inner in enumerate(A):
            for j, val in enumerate(inner):
                if val == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A


class Solution_2(object):
    def flipAndInvertImage_2(self, A): #20 ms faster at runtime
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for list in range(len(A)):
            A[list].reverse()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A