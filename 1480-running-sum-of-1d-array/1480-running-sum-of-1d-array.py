class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        add = 0

        right = 0
        
        while right < len(nums):
            add += nums[right]
            res.append(add)
            right += 1
        
        # for num in nums:
        #     add += num
        #     res.append(add)
        
        return res