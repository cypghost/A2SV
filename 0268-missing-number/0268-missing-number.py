class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Cyclic Sorting
        
        left = 0
        
        while left < len(nums):
            cur = nums[left] - 1
            
            if cur != left and nums[left] != 0:
                nums[left], nums[cur] = nums[cur], nums[left]
            
            else:
                left += 1
            
        for index in range(len(nums)):
            if index + 1 != nums[index]:
                return index + 1
        
        return 0
        
        # Normal Sorting
        
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
