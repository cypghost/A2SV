class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = []

        for i in range(n + 1):
            if i <= 1:
                dp.append(i)
            
            elif i % 2 == 0:
                dp.append(dp[i // 2])
            
            else:
                dp.append(dp[i // 2] + dp[i // 2 + 1])
            
        return max(dp)
        
