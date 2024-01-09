class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        ans = set()
        
        for num in nums1:
            l = 0
            r = len(nums2) - 1
            
            while l <= r:
                mid = (l + r) // 2
                
                if nums2[mid] == num:
                    if nums2[mid] not in ans:
                        ans.add(nums2[mid])
                    
                    break
                        
                elif nums2[mid] > num:
                    r = mid - 1
                
                elif nums2[mid] < num:
                    l = mid + 1
                    
        return ans
            
                