class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # identify the zero 
        '''
               0  1  2                    0   1   2   3
              -----------                ---------------
           0 | 1  1  1                0 | 0   1   2   0 
                         
           1 | 1  0  1                1 | 3   4   5   2
           
           2 | 1  1  1                2 | 1   3   1   5

        
            list[1][1] = 0             list[0][0] = 0 , list[0][3] = 0
                         sum,sub                     sum,sub       
            (1,0) = 1    1  , 1        (1,0) = 3     1  , -1 
            (0,1) = 1    1  ,-1        (0,1) = 1     1  , -1 
            
            (2,1) = 1    3  , 1        (2,0) = 1     2  , -2  
            (1,2) = 1    3  ,-1        (0,2) = 2     2  , -2
                                       
                                       (1,3) = 2     4  , -2
                                       (2,3) = 5     5  , -1          
            Unwanted Results
            
            (0,0) = 1    0  , 0        (1,1) = 4     2  ,  0
            (0,2) = 1    2  ,-2        (1,2) = 5     3  , -1
            (2,0) = 1    2  , 2        (2,1) = 1     3  ,  1
            (2,2) = 1    4  , 0        (2,2) = 1     4  ,  0
             
                                                             
        ''' 
        zeroindex = []
        value = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeroindex.append([row, col])
                    
        for index in range(len(zeroindex)): 
            for element in range(len(matrix[0])):
                value = zeroindex[index][0]
                matrix[value][element] = 0
            
            for element in range(len(matrix)):
                value = zeroindex[index][1]
                matrix[element][value] = 0
            
        return matrix
        