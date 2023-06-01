class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        
        for index in range(2, n + 1):
            dp[index] = min(dp[index - 1] + cost[index - 1], dp[index - 2] + cost[index - 2])

        return dp[n]