class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans , subarray = 0, 0
        
        for num in nums:
            if num == 0:
                subarray += 1
            
            else:
                subarray = 0
            
            ans += subarray
        
        return ans