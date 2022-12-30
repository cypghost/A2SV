class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        list = []
        index = 0
        
        while index < len(nums) + 1:
            list.append(index)
            index += 1
        
        for num in range(len(nums)):
            
            if nums[num] != list[num]:
                return list[num]
            
            elif nums[num] == list[num]:
                continue
            
        return list[len(list) - 1]