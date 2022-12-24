class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:] = nums2
        # nums1.sort()
        # Taking index into variables
        nums1top = m - 1
        nums2top = n - 1
        nums1last = len(nums1) - 1
        
        while nums2top != -1 and nums1top != -1:
            
            # Comparing values to sort them
            if nums1[nums1top] <= nums2[nums2top]:
                nums1[nums1last] = nums2[nums2top]
                nums1last -= 1
                nums2top -= 1

            elif nums1[nums1top] > nums2[nums2top]:
                nums1[nums1last] = nums1[nums1top]
                nums1top -= 1
                nums1last -= 1
                
        # for leftovers       
        while nums2top != -1:
            
            nums1[nums1last] = nums2[nums2top]
            nums1last -= 1
            nums2top -= 1
            
            