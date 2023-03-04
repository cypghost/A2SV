class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        minpos = maxpos = left = -1
        
        
        for index, val in enumerate(nums):
            
            if val < minK or val > maxK:
                left = index
                
            if val == minK:
                minpos = index
                
            if val == maxK:
                maxpos = index
                
            ans += max(0, min(minpos, maxpos) - left)
            
        return ans