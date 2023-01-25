class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        window = nums[len(nums) - k:] + nums[:len(nums) - k]   
        right = 0
        
        for index in window:
            nums[right] = index
            right += 1