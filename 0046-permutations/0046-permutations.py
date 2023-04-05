class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(bit, res):
            
            if len(res) == len(nums):
                ans.append(res.copy())
                return
     
            for index in range(len(nums)):
                if bit & (1 << index) == 0:
                    res.append(nums[index])
                    backtrack(bit | (1 << index), res)
                    res.pop()
            
            return ans
        
        return backtrack(0,[])