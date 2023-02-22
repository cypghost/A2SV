class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        add = sum(nums)
        leftsum = 0

        for left in range(len(nums)):
            diff = add - nums[left]
            
            if diff == leftsum * 2:
                return left
            
            leftsum += nums[left]
            left += 1
       
        return -1
        