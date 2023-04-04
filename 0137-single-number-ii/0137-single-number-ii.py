class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Dictionary
        
#         nums_dict = defaultdict(int)
        
#         for num in nums:
#             nums_dict[num] += 1
        
#         for key in nums_dict:
#             if nums_dict[key] == 1:
#                 return key
        
        # Set
        
        return (3 * sum(set(nums)) - sum(nums)) // 2