from collections import deque

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        deq = deque()
        
        for i in range(len(nums)):
                if nums[i] % 2 == 0:
                    deq.appendleft(nums[i])
                else:
                    deq.append(nums[i])
                
        return deq