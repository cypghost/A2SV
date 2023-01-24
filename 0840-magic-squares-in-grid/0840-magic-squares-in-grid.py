class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        num = 0
        col = len(grid[0])
        row =  len(grid)
        
        if row < 3 or col < 3:
            return 0
        
        for index in range(row - 2):
            
            for val in range(col - 2):
                
                squares = []
                
                squares.append(grid[index][val : val+3])
                squares.append(grid[index + 1][val : val + 3])
                squares.append(grid[index + 2][val : val + 3])
                
                Col1 = squares[0][0] + squares[1][0] + squares[2][0]
                Col2 = squares[0][1] + squares[1][1] + squares[2][1]
                Col3 = squares[0][2] + squares[1][2] + squares[2][2]
                
                Diag1 = squares[0][0] + squares[1][1] + squares[2][2]
                Diag2 = squares[0][2] + squares[1][1] + squares[2][0]
                
                if set(squares[0] + squares[1] + squares[2]) == set(range(1,10)):
                    
                    if sum(squares[0]) == sum(squares[1]) == sum(squares[2]):
                        
                        if Col1 == Col2 == Col3:
                            
                            if Diag1 == Diag2:
                                    
                                num+= 1
 
        return num