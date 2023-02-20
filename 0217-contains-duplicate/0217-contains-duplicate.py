class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2 = set(nums)
        
        nums2_len = len(nums2)
        nums_len = len(nums)
        
        if nums2_len != nums_len:
            return True
        
        return False
        
        