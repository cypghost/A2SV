class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mini = [0] * len(nums)
        mini[0] = nums[0]
        
        if len(nums) < 3:
            return False
        
        for index in range(1, len(nums)):
             mini[index] = min(mini[index - 1], nums[index])
        
        for index in range(len(nums) - 1, -1, -1):
            if nums[index] > mini[index]:
                while stack and stack[-1] <= mini[index]:
                    stack.pop()
                
                if stack and stack[-1] < nums[index]:
                    return True
            
            stack.append(nums[index])
        
        return False
        
        