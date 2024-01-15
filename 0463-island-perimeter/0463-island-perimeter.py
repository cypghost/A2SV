class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid[0]), len(grid)
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def inbound(row, col):
            return (0 <= row < m and 0 <= col < n)
        
        def dfs(row, col):
            if not inbound(row, col) or grid[row][col] == 0:
                return 1
                
            if grid[row][col] == -1:
                return 0
            
            grid[row][col] = -1
            ans = 0
            
            for r, c in dirs:
                new_r, new_c = r + row, c + col
                ans += dfs(new_r, new_c)
            
            return ans
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    return dfs(row, col)