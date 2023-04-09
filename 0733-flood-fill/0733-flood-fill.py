class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cur_color = image[sr][sc]
        
        if cur_color == color:
            return image
            
        def dfs(row, col):
            if image[row][col] == cur_color:
                
                image[row][col] = color
                
                if col > 0:
                    dfs(row, col - 1)
                
                if col + 1 < len(image[0]):
                    dfs(row, col + 1)
                    
                if row > 0:
                    dfs(row - 1, col)
                
                if row + 1 < len(image):
                    dfs(row + 1, col)
                    
        
        dfs(sr, sc)
        return image
                
                
                
            
            
            
            
            