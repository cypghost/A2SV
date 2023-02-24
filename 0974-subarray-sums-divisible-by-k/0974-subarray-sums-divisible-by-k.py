class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        num_dict = defaultdict(int)
        num_dict[0] = 1
        
        ans = 0
        add = 0
        
        for num in nums:
            add += num
            rem = add % k
            
            ans +=  num_dict[rem]
            num_dict[rem] += 1
        
        return ans
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         pre_sum = []
#         add = 0
#         count = 0
        
#         left = 0
        
#         for index in range(len(nums)):
#             add = 0
            
#             for left in range(index, len(nums)):
#                 add += nums[left]
                
#                 if add % k == 0:
#                     count += 1
                    
#         return count
                    