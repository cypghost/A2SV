class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for index in range(len(nums)):
            value, curr = index, nums[index]
            
            while value > 0 and not str(nums[value - 1]) + str(curr) > str(curr) + str(nums[value - 1]):
                nums[value] = nums[value - 1] 
                value -= 1
                
            nums[value] = curr
            
        return str(int("".join(map(str, nums))))