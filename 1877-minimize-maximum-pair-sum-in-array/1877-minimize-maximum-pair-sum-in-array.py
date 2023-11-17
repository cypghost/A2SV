class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        ans = 0
        left = 0
        right = n - 1
        
        while left < right:
            ans =  max(ans, nums[left] + nums[right])
            left += 1
            right -= 1
        
        return ans