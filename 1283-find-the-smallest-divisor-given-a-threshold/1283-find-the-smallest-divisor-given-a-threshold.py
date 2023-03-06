class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(nums, mid):
            add = 0
            
            for index in range(len(nums)):
                add += ceil(nums[index] / mid)
            
            return add
        
        left = 1 
        right = max(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if check(nums, mid) > threshold:
                left = mid + 1
            
            else:
                right = mid
        
        return left
                
            
            