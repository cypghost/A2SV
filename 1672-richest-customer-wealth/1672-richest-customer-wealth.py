class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        
        for row in range(len(accounts)):
            add = 0
            
            for col in range(len(accounts[0])):
                add += accounts[row][col]
            
            ans = max(ans, add)
        
        return ans