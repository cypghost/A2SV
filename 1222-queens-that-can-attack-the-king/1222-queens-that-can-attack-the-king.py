class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        
        queens = set(tuple(queen) for queen in queens)
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        answer = []
        
        for dir_x, dir_y in dirs:
            xKing, yKing = king
            
            while 0 <= xKing < 8 and 0 <= yKing < 8:
                xKing += dir_x
                yKing += dir_y
                
                if (xKing, yKing) in queens:
                    answer.append([xKing, yKing])
                    break
                    
        return answer

#         diag = []
#         vert = []
#         hori = []
        
#         for index in range(len(queens)):
#             if queens[index][0] == queens[index][1]:
#                 diag.append(queens[index])
            
#             elif queens[index][0] > queens[index][1]:
#                 vert.append(queens[index])
                
#             else:
#                 hori.append(queens[index])
                
#         diag.sort()
#         hori.sort()
#         vert.sort()
        
#         return [diag[0], vert[0], hori[0]]
        
            
            
        