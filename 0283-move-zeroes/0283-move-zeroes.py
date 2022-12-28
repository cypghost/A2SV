from collections import deque

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while True:
            if 0 in nums:
                i += 1
                nums.remove(0)
                continue
            break
        for j in range(i):
            nums.append(0)
            