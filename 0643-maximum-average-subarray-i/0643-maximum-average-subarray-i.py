class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0
        add = 0
        res = -float("inf")
        
        if len(nums) < 2:
            return nums[0]
        
        while right < k - 1:
            add += nums[right]
            right += 1
            
            
        # add = sum(nums[left : right + 1])   
        
        while right < len(nums):
            add += nums[right]
            
            res = max(res, add / k)
            
            add -= nums[left] 
            left += 1
            
            right += 1
            
            # if right < len(nums):
            #     add += nums[right]
        
        return res