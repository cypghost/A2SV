class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i):
            if i == 0:
                return nums[i]

            if i == 1:
                return max(nums[0],nums[1])

            if i not in memo:
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])

            return memo[i]

        memo = {}
        
        return dp(len(nums) - 1)