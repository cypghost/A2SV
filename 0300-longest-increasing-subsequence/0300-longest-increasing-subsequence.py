class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        for i in range(n):
            if stack:
                if nums[i] <= stack[-1]:
                    a = bisect_left(stack, nums[i])
                    stack[a] = nums[i]
                
                else:
                    stack.append(nums[i])

            else:
                stack.append(nums[i])

        return len(stack)

#         n = len(nums)
#         dp = [1] * n

#         for i in range(n):
#             count = 0

#             for j in range(i - 1, -1, -1):
#                 if nums[j] < nums[i]:
#                     count = max(count, dp[j])
            
#             dp[i] += count

#         return max(dp)
