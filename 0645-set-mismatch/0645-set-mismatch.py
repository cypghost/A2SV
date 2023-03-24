class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        left = 0
        ans = []
        
        while left < len(nums):
            cur = nums[left] - 1
            
            if cur != left and nums[cur] != nums[left]:
                nums[cur], nums[left] = nums[left], nums[cur]
                
            else:
                left += 1
            
        for index in range(len(nums)):
            if index + 1 != nums[index]:
                ans.append(nums[index])
                ans.append(index + 1)
            
        return ans
        