class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 0
        
        while left < len(nums):
            cur = nums[left] - 1
            
            if cur != left and nums[cur] != nums[left]:
                nums[cur], nums[left] = nums[left], nums[cur]
                
            elif cur != left and nums[cur] == nums[left]:
                return nums[left]
            
            else:
                left += 1
        
        
        