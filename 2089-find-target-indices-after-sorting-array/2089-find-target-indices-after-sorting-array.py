class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        answer = []
        
        for index in range(len(nums)):
            left = index - 1
            right = index
            
            while left >= 0 and nums[left] > nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left -= 1
                right -= 1
            
        for index in range(len(nums)):
            if nums[index] == target:
                answer.append(index)
                
        return answer