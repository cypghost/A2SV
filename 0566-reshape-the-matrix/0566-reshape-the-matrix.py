class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        temp = []
        reshaped = []
        
        for row in mat:
            for num in row:
                temp.append(num)
                
        if r * c != len(temp): 
            return mat
        
        else:
            for row_index in range(r):
                reshaped.append(temp[row_index * c : row_index * c + c])
        
            return reshaped
        