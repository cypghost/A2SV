class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # With in place 
        
        matrix.reverse()
        for row in range(len(matrix)):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        # Without in place
        
#         answer = []
        
#         for row in range(len(matrix)):
#             shifted = []
#             for col in range(len(matrix[0])):
#                 shifted.append(matrix[col][row])
#             answer.append(shifted[::-1])
            
#         for row in range(len(matrix)):
#             for col in range(len(matrix[0])):
#                 matrix[row][col] = answer[row][col]

             
            