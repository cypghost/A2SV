class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        ans = 0
        
        for index in range(n, len(piles), 2):
            ans += piles[index]
        
        return ans
            