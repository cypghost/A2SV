class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        land = []
        
        def dfs(row,col):
            grid[row][col] = 2
            land.append((row, col, 0))

            moves = ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1))

            for r, c in moves:
                if 0 <= r < n and 0 <= c < n and grid[r][c] == 1:
                    dfs(r, c)
        
        flag = True
        
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    dfs(row, col)
                    flag = False
                    break

            if not flag:
                break
                
        queue = land
        while queue:
            row, col, dist = queue.pop(0)
            
            if grid[row][col] == 1:
                return dist

            moves = ((row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1))
            for r, c in moves:
                if 0 <= r < n and 0 <= c < n and grid[r][c] != 2:
                    if grid[r][c] == 1:
                        return dist

                    grid[r][c] = 2
                    queue.append((r, c, dist + 1))
        
        return -1