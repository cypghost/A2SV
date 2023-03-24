class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        left = 0
        ans = []
        
        while left < len(nums):
            cur = nums[left] - 1
            
            if cur != left and nums[cur] != nums[left]:
                nums[left], nums[cur] = nums[cur], nums[left]
            
            else:
                left += 1
            
        
        for index in range(len(nums)):
            if nums[index] != index + 1:
                ans.append(index + 1)
            
        return ans