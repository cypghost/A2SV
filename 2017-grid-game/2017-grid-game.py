class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top = sum(grid[0])
        bottom = 0
        res = float("inf")
        
        for idx, val in zip(grid[0], grid[1]):
            top -= idx
            res = min(res, max(top, bottom))
            bottom += val
            
        return res