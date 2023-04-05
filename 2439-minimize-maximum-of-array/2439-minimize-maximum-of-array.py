class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        answer = 0
        prefix_sum = 0
        
        for index in range(len(nums)):
            prefix_sum += nums[index]
            answer = max(answer, math.ceil(prefix_sum / (index + 1)))

        return answer