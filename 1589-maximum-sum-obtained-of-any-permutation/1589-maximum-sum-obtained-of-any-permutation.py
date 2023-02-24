class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre_sum = [0]*(len(nums) + 1)
        add = 0
        
        for request in requests:
            pre_sum[request[0]] += 1
            pre_sum[request[1] + 1] -= 1
            
        for index in range(1, len(pre_sum)):
            pre_sum[index] += pre_sum[index-1]
            
        pre_sum = sorted(pre_sum, reverse=True)
        nums = sorted(nums, reverse=True)
        
        for index in range(len(nums)):
            add += pre_sum[index] * nums[index]
            
        return add % (10**9 + 7)