class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start = 0, curr = []):
            if len(curr) == idx:  
                res.append(curr[:])
                return

            for index in range(start, len(nums)):
                curr.append(nums[index])
                backtrack(index + 1, curr)
                curr.pop()
        
        res = []
        
        for idx in range(len(nums) + 1):
            backtrack()

        return res
