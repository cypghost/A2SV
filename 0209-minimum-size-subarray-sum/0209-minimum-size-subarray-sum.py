class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        minimum = float("inf")
        add = nums[0]
        
        while right < len(nums) and left <= right:
            
            if add >= target:
                minimum = min(minimum, right - left + 1)
                add -= nums[left]
                left += 1 
                
            elif add < target:
                right += 1
                if right < len(nums):
                    add += nums[right]
                    
        if minimum != float("inf"):
            return minimum
        
        return 0
        
        
            
                