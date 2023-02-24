class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in range(len(nums))]
        prod = 1
        
        for index in range(1, len(nums)):
            prod = prod * nums[index - 1]
            ans[index] = ans[index] * prod

        prod = 1
        
        for index in range(len(nums) - 2, -1, -1):
            prod = prod * nums[index + 1]
            ans[index] = ans[index] * prod

        return ans