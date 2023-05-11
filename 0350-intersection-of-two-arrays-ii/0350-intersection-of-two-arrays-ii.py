class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        
        nums3 = nums1.copy()
        
        for index in range(len(nums3)):
            if nums3[index] in nums2:
                ans.append(nums3[index])
                
                nums2.remove(nums3[index])
                nums1.remove(nums3[index])
                
    
        return ans
            
                    
        