class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid2[row][col] == 0:
                return True

            if grid1[row][col] == 0:
                return False

            grid2[row][col] = 0
            res = True

            for r, c in dirs:
                res &= dfs(row + r, col + c)

            return res
        
        m, n = len(grid1), len(grid1[0])
        count = 0

        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 1 and dfs(row, col):
                    count += 1

        return count




        

                    