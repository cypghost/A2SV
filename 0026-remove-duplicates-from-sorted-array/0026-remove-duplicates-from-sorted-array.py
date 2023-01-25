class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        
        while right < len(nums):
            if nums[left] == nums[right]:
                nums.remove(nums[left])
            
            else:
                left += 1
                right += 1
                
        return len(nums)