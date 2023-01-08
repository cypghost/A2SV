class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = [0] * len(grid)
        cols = [0] * len(grid[0])
    
        for gridrow in range(len(grid)):
            for gridcol in range(len(grid[0])):
                
                # value will be -1 if the element is 0 otherwise 1
                value = 2 * grid[gridrow][gridcol] - 1 
                
                # operation of onesrow and zerosrow will be made
                rows[gridrow] += value
                cols[gridcol] += value
        
        # return the difference with in the specified row and column 
        return [[rows[gridrow] + cols[gridcol] for gridcol in range(len(grid[0]))] for gridrow in range(len(grid))]
