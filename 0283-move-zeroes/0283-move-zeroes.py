from collections import deque

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        element = 0
        
        for index in range(len(nums)):
             if nums[index] != 0:
                temp = nums[index]
                nums[index] = nums[element]
                nums[element] = temp
                
                # nums[index], nums[element] = nums[element], nums[index]
                element += 1
                
        return nums
        
        
        
        
        
        
        
