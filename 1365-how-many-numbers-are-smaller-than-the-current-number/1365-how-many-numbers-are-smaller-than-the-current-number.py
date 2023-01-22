class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        indexes = {}
        result = []
        
        for index in range(len(temp)):
            if temp[index] not in indexes:
                indexes[temp[index]] = index
        
        for index in range(len(nums)):
            result.append(indexes[nums[index]])
               
        return result
    
    # TIME LIMIT EXCEEDED
#         answer = []
        
#         for index in range(len(nums)):
#             left = index
#             right = 0
#             count = 0
            
#             while right <= len(nums) - 1:
#                 if nums[left] > nums[right]:
#                     count += 1
#                     right += 1
                    
#             answer.append(count) 
            
        return answer