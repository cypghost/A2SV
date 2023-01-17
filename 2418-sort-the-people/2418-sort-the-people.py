class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # Bubble Sort
#         for index in range(len(names)):
#             for elements in range(len(heights) - 1 - index):
#                 if heights[elements] < heights[elements + 1]:
#                     heights[elements], heights[elements + 1] = heights[elements + 1], heights[elements]
#                     names[elements], names[elements + 1] = names[elements + 1], names[elements]
        
        # Selection Sort
#         for index in range(len(heights)):
#             minindex = index
            
#             for element in range(index , len(heights)):
#                 if heights[element] > heights[minindex]:
#                     minindex = element
                    
#             heights[minindex], heights[index] = heights[index], heights[minindex]
#             names[minindex], names[index] = names[index], names[minindex]
        
    
        for index in range(1, len(names)):
            i = index
            j = index - 1
            
            while j >= 0 and heights[i] > heights[j]:
                heights[i], heights[j] = heights[j], heights[i]
                names[i], names[j] = names[j], names[i]
                i -= 1
                j -= 1
        
                # if heights[index] < heights[element]:
                #     heights[index], heights[element] = heights[element], heights[index]
                #     names[index], names[element] = names[element], names[index]
                #     break
          
                
                
                
        return names
    
    '''
    1,2,3,6,4,5
    2,1,3,6,4,5
    
    2,3,1,6,4,5
    
    '''