class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        
        upper_dps = [0 for _ in range(n)]
        lower_dps = [0 for _ in range(n)]
        
        count = 0
        for i in range(n):
            for j in range(i):
                if rating[j] < rating[i]:
                    count += upper_dps[j]
                    upper_dps[i] += 1
                    
                else:
                    count += lower_dps[j]
                    lower_dps[i] += 1
            
        return count          