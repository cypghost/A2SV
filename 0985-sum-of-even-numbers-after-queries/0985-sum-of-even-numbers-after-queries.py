class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answer = []
        evensum = 0
        
        for index in range(len(nums)):
            if nums[index] % 2 == 0:
                evensum += nums[index]
        
        for queryrow in range(len(queries)):
            index = queries[queryrow][1]
            value = queries[queryrow][0]
            
            numsele = nums[index]
            
            nums[index] += value
            
            if nums[index] % 2 == 0 and numsele % 2 != 0:
                evensum += nums[index]
                
            elif nums[index] % 2 == 0 and numsele % 2 == 0:
                evensum += value
                
            elif nums[index] % 2 != 0 and numsele % 2 == 0:
                evensum -= numsele
            
            answer.append(evensum)
            
        return answer
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         for queryrow in range(len(queries)):
            
#             index = queries[queryrow][1]
#             value = queries[queryrow][0]
#             evensum = 0
            
#             # to add value to the nums[index] value
#             nums[index] += value
            
#             # To find even numbers and sum them up
#             for index in range(len(nums)):
#                  if nums[index] % 2 == 0:
#                     evensum += nums[index]
                
#             answer.append(evensum) 
            
#         return answer
                
            
            