class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        add = 0
        
        for num in nums:
            add += num
            res.append(add)
        
        return res