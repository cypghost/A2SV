class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        pair = [(scores[i], ages[i]) for i in range(n)]
        pair.sort()

        dp = [pair[i][0] for i in range(n)]

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if pair[j][1] <= pair[i][1]:
                    dp[i] = max(dp[i], pair[i][0] + dp[j])
        
        return max(dp)