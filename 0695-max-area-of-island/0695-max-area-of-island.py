class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        
        def dfs(row, col):
            if not ((row >= 0 and row < len(grid)) and (col >= 0 and col < len(grid[0])) and (row, col) not in visited and grid[row][col]):
                return 0
            
            visited.add((row, col))
            
            return (1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1))
        
        return max(dfs(row, col) for row in range(len(grid)) for col in range(len(grid[0])))