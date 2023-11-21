class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i >= len(s) and j >= len(p): 
                return True
            
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if j + 1 < len(p) and p[j + 1] == "*":
                memo[(i, j)] = ((dp(i, j + 2)) or (match and dp(i + 1, j)))
                
                return memo[(i, j)]
        
            if match:
                memo[(i, j)] = dp(i + 1, j + 1)
                
                return memo[(i, j)]
        
            memo[(i, j)] = False
            
            return memo[(i, j)]
        
        return dp(0, 0)