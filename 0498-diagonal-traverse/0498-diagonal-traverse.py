class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        Rows = len(mat) 
        Columns = len(mat[0])
        
        diagonal = defaultdict(list)
        
        for row in range(Rows):
            for col in range(Columns):
                diagonal[row + col].append(mat[row][col])
                
        answer = []
        
        key = 0
        
        while key in diagonal:
            if key % 2:
                answer.extend(diagonal[key])
            else: 
                answer.extend(diagonal[key][::-1])
            
            key+=1
        
        return answer