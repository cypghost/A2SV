class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for index in range(len(matrix[0])):
            for element in range(len(matrix)):
                if matrix[element][index] == target:
                    return True
                
            
        return False