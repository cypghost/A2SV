class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1
        
        while right <= len(nums) - 1:
            if nums[left] != 0:
                left += 1
                
            elif nums[right] != 0 and nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
       
            right += 1
            
        return nums  
    
    
#         element = 0
        
#         for index in range(len(nums)):
#              if nums[index] != 0:
#                 temp = nums[index]
#                 nums[index] = nums[element]
#                 nums[element] = temp
#                 element += 1
                
#                 # nums[index], nums[element] = nums[element], nums[index]
                
                
        
        
        
        
        
        
        
        
