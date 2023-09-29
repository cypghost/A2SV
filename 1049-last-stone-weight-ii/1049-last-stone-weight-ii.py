class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        memo = {}

        def dp(pos, res):
            if pos == n:
                return res if res >= 0 else float('inf')

            cur = (pos, res)

            if cur in memo:
                return memo[cur]

            memo[cur] = min(
                float('inf'),
                dp(pos + 1, res - stones[pos]), 
                dp(pos + 1, res + stones[pos]) 
            )

            return memo[cur]

        return dp(0, 0) 
        