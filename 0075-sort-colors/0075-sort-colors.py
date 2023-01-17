class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        for index in range(1, len(nums)):
            left = index - 1
            right = index
            
            while left >= 0 and nums[right] < nums[left]:
                nums[left], nums[right] = nums[right], nums[left]
                left -= 1
                right -= 1
        return nums     
        
                