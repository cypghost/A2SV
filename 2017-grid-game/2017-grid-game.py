class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top, bottom, res = sum(grid[0]), 0, math.inf
        for g0, g1 in zip(grid[0], grid[1]):
            top -= g0
            res = min(res, max(top, bottom))
            bottom += g1
        return res