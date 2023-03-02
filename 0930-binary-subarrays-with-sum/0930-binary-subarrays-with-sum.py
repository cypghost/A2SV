class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        left = 0
        count = 0
        res = 0
        add = 0
        
        for index, val in enumerate(nums):
            add += val
            
            if val == 1:
                count = 0
                
            while left <= index and add >= goal:
                if add == goal:
                    count += 1
                    
                add -= nums[left]
                left += 1
                
            res += count
            
        return res