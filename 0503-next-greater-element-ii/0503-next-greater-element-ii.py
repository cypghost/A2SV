class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        
        for _ in range(2):
            for index in range(len(nums)):
                while stack and stack[-1][0] < nums[index]:
                    ans[stack.pop()[1]] = nums[index]

                stack.append([nums[index], index])
        
        return ans
            
        