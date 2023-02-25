class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums_dict = defaultdict(int)
        count = 0
        ans = 0
        
        nums_dict[0] = 1
        
        for num in nums:
            if num % 2 != 0:
                count += 1
                
            ans += nums_dict[count - k]
            nums_dict[count] += 1
        
        return ans