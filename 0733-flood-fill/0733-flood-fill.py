class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
            
        def dfs(row, col, cur):
            if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]):
                return 
        
            if cur != image[row][col]:
                return 
        
            image[row][col] = color
            
            dfs(row - 1, col, cur)
            dfs(row + 1, col, cur)
            dfs(row, col - 1, cur)
            dfs(row, col + 1, cur)
                    
        dfs(sr, sc, image[sr][sc])
        return image
                
                
                
            
            
            
            
            