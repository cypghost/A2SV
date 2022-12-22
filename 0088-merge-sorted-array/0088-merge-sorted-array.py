class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = 0
        for i in range(m,m+n):
            nums1.remove(0)
            nums1.append(nums2[temp])
            temp+=1
            print(nums1[i])
        nums1.sort()
        