class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        for index in range(len(names)):
            for elements in range(len(heights) - 1 - index):
                if heights[elements] < heights[elements + 1]:
                    heights[elements], heights[elements + 1] = heights[elements + 1], heights[elements]
                    names[elements], names[elements + 1] = names[elements + 1], names[elements]
        
        
#         for index in range(len(heights)):
#             minindex = index
            
#             for element in range(index , len(heights)):
#                 if heights[element] > heights[minindex]:
#                     minindex = element
                    
#             heights[minindex], heights[index] = heights[index], heights[minindex]
#             names[minindex], names[index] = names[index], names[minindex]
                    
        return names