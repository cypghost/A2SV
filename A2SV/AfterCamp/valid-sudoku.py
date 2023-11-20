class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
          0  1  2   3  4  5   6  7  8
        --------- --------- ---------
     0  | 5  3  * | *  7  * | *  *  * |     
                   
     1  | 6  *  * | 1  9  5 | *  *  * |
        
     2  | *  9  8 | *  *  * | *  6  * |
        --------- --------- ---------
     3  | 8  *  * | *  6  * | *  *  3 |
         
     4  | 4  *  * | 8  *  3 | *  *  1 |
        
     5  | 7  *  * | *  2  * | *  *  6 |
        --------- --------- ---------
     6  | *  6  * | *  *  * | 2  8  * |
       
     7  | *  *  * | 4  1  9 | *  *  5 |
       
     8  | *  *  * | *  8  * | *  7  9 |
        --------- --------- ---------
        
        
         [[".", ".", ".",  ".", "5", ".",  ".", "1", "."],
         
          [".", "4", ".",  "3", ".", ".",  ".", ".", "."],
          
          [".", ".", ".",  ".", ".", "3",  ".", ".", "1"],
          
          
          ["8", ".", ".",  ".", ".", ".",  ".", "2", "."],
          
          [".", ".", "2",  ".", "7", ".",  ".", ".", "."],
          
          [".", "1", "5",  ".", ".", ".",  ".", ".", "."],
          
          
          [".", ".", ".",  ".", ".", "2",  ".", ".", "."],
          
          [".", "2", ".",  "9", ".", ".",  ".", ".", "."],
          
          [".", ".", "4",  ".", ".", ".",  ".", ".", "."]]
       
       '''
        rowwise = defaultdict(set)
        colwise = defaultdict(set)
        matwise = defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                
                value = board[row][col]
                
                if value == '.':
                    continue
                
                if value in rowwise[row]:
                    return False
                
                rowwise[row].add(value)
                                
                if value in colwise[col]:
                    return False
                
                colwise[col].add(value)
                                                                                       
                index = row // 3*3 + col // 3 
                
                if value in matwise[index]:                     
                    return False                          
                
                matwise[index].add(value)                       
                                                          
        return True
    
#         # Check if row has any repeated numbers
#         for row in range(len(board)):
#             rowwise = defaultdict(int)
            
#             for col in range(len(board[0])):
#                 rowwise[board[row][col]] += 1
                
#                 if board[row][col] != "." and board[row][col] in rowwise:
#                     if rowwise[board[row][col]] > 1:
#                         return False
        
#         # Check if column has any repeated numbers
#         for col in range(len(board[0])):
#             colwise = defaultdict(int)
            
#             for row in range(len(board)):
#                 colwise[board[row][col]] += 1
                
#                 if board[row][col] != "." and board[row][col] in colwise:
#                     if colwise[board[row][col]] > 1:
#                         return False
                    
#         # Check if 3 * 3 has any repeated numbers and check if one mat array contains only "."
#         value = 0
        
#         for row in range(value + 3, len(board), 3):
#             matwise = defaultdict(int)
            
#             for col in range(value, row):
#                 matwise[board[row][col]] += 1             
                    
#             for rows in range(value, row):
#                 for cols in range(value, row):
#                     if board[value: value + 3][value: value + 3] != ".":
#                         if matwise[board[rows][cols]] > 1:
#                             return False  
                      
#             value += 3           
        
#         return True
       
            
                