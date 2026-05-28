# Use this to find groups of sets together that are touching
# It basically builds a tree and maps each value. 
# If the value's parent has a larger size, then that smaller tree is mapped into larger (memory efficient). 
# Leetcode https://leetcode.com/problems/max-area-of-island/editorial/

# visit set is not needed since if pp0 == pp1, it would have been visited already and it's O(1) runttime anyway. 

class Dsu:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.size = [1] * (n+1)
    
    def find(self, p):
        if self.parents[p] != p:
            self.parents[p] = self.find(self.parents[p])
        return self.parents[p]
    
    def union(self, p0, p1):
        pp0 = self.find(p0)
        pp1 = self.find(p1)
        if pp0 == pp1:
            return
        else:
            if self.size[pp0] >= self.size[pp1]:
                self.size[pp0] += self.size[pp1]
                self.parents[pp1] = pp0
            else:
                self.size[pp1] += self.size[pp0]
                self.parents[pp0] = pp1

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        duf = Dsu(len(grid)*len(grid[0]))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def index(i, j):
            return len(grid[0])*i+j
        island_found = False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island_found = True
                    for ox, oy in directions:
                        nx = i + ox
                        ny = j + oy
                        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                            continue
                        if grid[nx][ny] == 1:
                            duf.union(index(i, j), index(nx, ny))
        if island_found:
            return max(duf.size)
        return 0
