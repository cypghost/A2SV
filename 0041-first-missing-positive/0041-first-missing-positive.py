class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            
            if nums[0] == 1:
                return 2
            
            else:
                return 1
        
        left = 0
        
        while left < len(nums):
            cur = nums[left] - 1
            
            if cur >= 0 and cur < len(nums) and left + 1 != cur and nums[cur] != nums[left]:
                nums[left], nums[cur] = nums[cur], nums[left]
                
            else:
                left += 1
            
        for index in range(len(nums)):
            if index + 1 != nums[index]:
                return index + 1
            
        return len(nums) + 1
                