class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = defaultdict(int)
        
        for num in nums:
            nums_dict[num] += 1
        
        for key in nums_dict:
            if nums_dict[key] == 1:
                return key