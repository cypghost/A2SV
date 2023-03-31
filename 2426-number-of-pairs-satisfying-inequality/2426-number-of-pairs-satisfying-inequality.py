class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        nums_diff = [nums1[i] - nums2[i] for i in range(n)]
        result = 0
        
        def merge(nums_diff):
            
            if len(nums_diff) == 1:
                return nums_diff
            
            nonlocal result
            
            mid = len(nums_diff) // 2
            
            left = merge(nums_diff[:mid])
            
            right = merge(nums_diff[mid:])
            
            for index in left:
                result += len(right) - bisect_left(right, index - diff)
            
            return sorted(left + right)
        
        merge(nums_diff)
        return result