class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
    
        if total < abs(target) or (total + target) & 1:
            return 0

        def dp(target):
            curr = [1] + [0] * total

            for num in nums:
                for j in range(total, num - 1, -1):
                    curr[j] += curr[j - num]

            return curr[target]
    
        return dp((total + target) // 2)