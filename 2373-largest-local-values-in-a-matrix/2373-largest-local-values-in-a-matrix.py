class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        maxlocal = (n - 2) * (n - 2); n = 4
        
        maxvalue = 9
        
             0    1
            -----------
        0  | 9    9
        
        1  | 8    6     
        
        
        row = n - 1, col = n - 1
        
        '''
        maxlocal = []
       
        for row in range(len(grid) - 2):
            larger = []
            
            for col in range(len(grid) - 2):
                maxvalue = 0
                mat = [grid[row + index][col : col + 3] for index in range(3)]
                
                for large in mat:
                    if maxvalue < max(large):
                        maxvalue = max(large) 
                        
                larger.append(maxvalue)
                    
            maxlocal.append(larger)
                   
        return maxlocal
                        
        
            
        