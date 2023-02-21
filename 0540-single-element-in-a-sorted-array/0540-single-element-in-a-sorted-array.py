class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:    
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        
#         if nums[0] != nums[1]:
#             return nums[0]
 
        if nums[right] != nums[right - 1]:
            return nums[right]
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
                
            elif (nums[mid] == nums[mid + 1] and mid % 2 == 0) or (nums[mid] == nums[mid - 1] and mid % 2 != 0):
                left = mid + 1
                
            else:
                right = mid - 1
                
        return nums[left]
