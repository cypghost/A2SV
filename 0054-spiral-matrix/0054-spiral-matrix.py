class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        mat = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        
        value = 0
        
        while True:
            if left > right:
                break
            
            for index in range(left, right + 1):
                mat.append(matrix[top][index])
                
            top += 1
            
            if top > bottom:
                break
            
            for index in range(top, bottom + 1):
                mat.append(matrix[index][right])
                
            right -= 1
            
            if left > right:
                break
            
            for index in range(right, left - 1, -1):
                mat.append(matrix[bottom][index])
                
            bottom -= 1
        
            if top > bottom:
                break
            
            for index in range(bottom, top - 1, -1):
                mat.append(matrix[index][left])
            
            left += 1
            
        return mat
        # for row in range(len(matrix)):
        #     for col in range(len(matrix[0])):
        #         print(mat[i][j],end= " ");
        #     print();
            
            
                