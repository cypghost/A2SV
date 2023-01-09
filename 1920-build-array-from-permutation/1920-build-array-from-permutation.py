class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [] * len(nums)
        length = len(nums)
        
        for index in range(length):
            answer.append(nums[nums[index]])
            
        return answer