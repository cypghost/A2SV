class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        '''
             0  1  2  3                   0  1  
                          
        0  | 1  2  3  4              0 |  1  2
                             
        1  | 5  1  2  3              1 |  2  2
        
        2  | 9  5  1  2
        
        (0,0), (1,1), (2,2) = 1      
        (0,1), (1,2), (2,3) = 2
        (0,2), (1,3) = 3 
        (1,0), (2,1) = 5
        
        
        (0,0), (1,0), (2,0) = 1
        (1,-1), (3,-1), (5,-1) = 2
        (2,-2), (4,-2) = 3
        (1,1), (3,1) = 5
        
        
        
        '''
        from collections import defaultdict
        
        diagonals = []
        
        right = defaultdict(set)
        
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                right[row - col].add(matrix[row][col])
                   
                if len(right[row - col]) != 1:
                    return False
                        
        return True
                    
        