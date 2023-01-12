class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index = 0
        elements = 0
        
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                nums[index] = nums[index] * 2
                nums[index + 1] = 0
                index += 2
            
            else: 
                index += 1
        
        for element in range(len(nums)):
            if nums[element] != 0:
                temp = nums[element]
                nums[element] = nums[elements]
                nums[elements] = temp
                elements += 1
                
        return nums