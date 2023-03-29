class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        v = sorted(satisfaction,reverse=True)
        sums = 0
        ans = 0
        
        for i in v:
            if sums + i > 0:
                ans += sums + i
                sums += i
                
        return ans