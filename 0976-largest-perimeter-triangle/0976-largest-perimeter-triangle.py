class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse = True)
        sum = 0
        
        for index in range(len(nums) - 2):
            
            if nums[index] < nums[index + 1] + nums[index + 2]:
                sum += nums[index] + nums[index + 1] + nums[index + 2]
                return sum
            
        return 0
            