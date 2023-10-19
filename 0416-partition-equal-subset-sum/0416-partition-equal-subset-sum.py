class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        
        if total % 2:
            return False

        # target = total // 2
        # dp = [False] * (target + 1)
        # dp[0] = True

        # for num in nums:
        #     for j in range(target, num - 1, -1):
        #         dp[j] |= dp[j - num]

        # return dp[target]

        dp = {0}

        for num in nums:
            cur = set()

            for i in dp:
                cur.add(i + num)
                cur.add(i)
            
            dp = cur
        
        return total // 2 in dp        