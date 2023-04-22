class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        
        for index in range(n - 2, -1, -1):
            prev = 0
            
            for idx in range(index + 1, n):
                temp = dp[idx]
                
                if s[index] == s[idx]:
                    dp[idx] = prev
                    
                else:
                    dp[idx] = min(dp[idx], dp[idx - 1]) + 1
                    
                prev = temp
                
        return dp[n - 1]
        
        