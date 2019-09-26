class UnionFind(object):
    def __init__(self, N):
        self.parent = list(range(N))
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])
    
    def union(self, i, j):
        i_r = self.find(i)
        j_r = self.find(j)
        self.parent[j_r] = i_r

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid) 
        col = len(grid[0]) 
        island = set()
        uf = UnionFind(row*col)
        for x in range(row):
            for y in range(col):
                # all the h/v positions
                for (dx, dy) in [
                    [-1, 0], [0, 1], [1, 0], [0, -1]
                ]:
                    newx, newy = x + dx, y + dy
                    if newx >=0 and newy >= 0 and newx <= row-1 and newy <= col-1 and grid[newx][newy] == "1" and grid[x][y] == "1":
                        uf.union(x*col+y, newx*col+newy)
                                          
        for x in range(row):
            for y in range(col):
                if grid[x][y] == "1":
                    island.add(uf.find(x*col+y))
        return len(island)
    
    