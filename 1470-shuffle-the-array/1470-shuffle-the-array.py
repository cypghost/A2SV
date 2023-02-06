class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = 0 
        
        ans = []
        while left + n < len(nums):
            ans.append(nums[left])
            ans.append(nums[left + n])
            
            left += 1
        
        return ans