# 200. Number of Islands
# Time: O(MxN), Space: O(MxN)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        w, h = len(grid[0]), len(grid)
        self.check = [[0 for x in range(w)] for y in range(h)]
        self.grid = grid
        count = 0
        
        for x in range(w):
            for y in range(h):
                if self.grid[y][x] == "1" and self.check[y][x] == False:
                    self.check_island(x, y, w, h)
                    count += 1
                
        return count
        
    def check_island(self, x: int, y: int, w: int, h: int):
        if (x < 0) or (x >= w):
            return
        if (y < 0) or (y >= h):
            return
        if self.check[y][x] == True:
            return

        self.check[y][x] = True
        if self.grid[y][x] == "1":
            self.check_island(  x, y-1, w, h)
            self.check_island(x-1,   y, w, h)
            self.check_island(x+1,   y, w, h)
            self.check_island(  x, y+1, w, h)
        else:
            return