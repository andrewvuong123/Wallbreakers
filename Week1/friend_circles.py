class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))
        
    def union(self, x, y):
        x_r = self.find(x)
        y_r = self.find(y)
        if x_r != y_r:
            self.parent[x_r] = y_r
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        row = len(M)
        col = len(M[0])
        total = set()
        if row == 0 or col == 0:
            return 0
        
        uf = UnionFind(row)
        for i in range(row):
            for j in range(col):
                if M[i][j] == 1:
                    uf.union(i, j)
        
        for i in range(row):
            total.add(uf.find(i))
            
        return len(total)
            
                