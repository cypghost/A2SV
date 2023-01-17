class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        greatest = -1
        temp = 0
        
        for index in range(len(arr) - 1, -1, -1):
            temp = arr[index]
            arr[index] = greatest
            greatest = max(greatest, temp)
            
        return arr
    
    # TIME LIMIT EXCEED
#         left = 0
#         right = left + 1
        
#         answer = []
    
#         if len(arr) < 2:
#             arr[0] = -1
        
#         while left < len(arr) - 1 and right < len(arr):
#             maxvalue = 0
            
#             if maxvalue < arr[right]:
#                 maxvalue = arr[right]
#                 right += 1
            
            
#             for element in range(left + 1, len(arr)):
#                 if maxvalue < arr[element]:
#                     maxvalue = arr[element]
            
#             answer.append(maxvalue)
#             left += 1
            
#         answer.append(-1)
        
        
