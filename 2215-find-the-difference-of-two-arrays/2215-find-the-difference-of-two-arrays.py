class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        res = []
        
        for num in nums1:
            if num not in nums2:
                res.append(num)
        
        ans.append(set(res))
        
        res = []
        
        for num in nums2:
            if num not in nums1:
                res.append(num)
              
        ans.append(set(res))
        
        return ans
        
        
        
        
        