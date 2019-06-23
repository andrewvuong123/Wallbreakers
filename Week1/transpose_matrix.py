class Solution(object):
    def transpose(self, A): #12 ms faster at runtime
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        transpose = []
        for x in range(len(A[0])): #number of columns
            transpose.append([])
            for y in range(len(A)): #number of rows
                transpose[x].append(A[y][x])
        return transpose


class Solution_2(object):
    def transpose_2(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        transpose = []
        for i in range(len(A[0])):
            transpose.append([row[i] for row in A])
        return transpose