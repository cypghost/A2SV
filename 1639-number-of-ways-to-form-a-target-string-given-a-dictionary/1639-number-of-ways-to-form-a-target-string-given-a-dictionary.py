class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        letters = 26
        mod = 1000000007
        
        n = len(target)
        w = len(words[0])
        
        cnt = [[0] * w for _ in range(letters)]
         
        for index in range(w):
            for word in words:
                cnt[ord(word[index]) - ord('a')] [index] += 1
                
        dp = [[-1] * (w + 1) for _ in range(n + 1)]
        
        
        def f(i, j):
            
            if j == 0:
                return 1 if i == 0 else 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = f(i, j - 1)
            
            if i > 0:
                dp[i][j] += (cnt[ord(target[i - 1]) - ord('a')]) [j - 1] * f(i - 1, j - 1)
                
            
            dp[i][j] %= mod
            
            return dp[i][j]
        
        return f(n, w)
                
                
        
        