class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        maxcontainer = 0
        
        while left <= right:
            if height[left] <= height[right]:
                prod = height[left] * (right - left)
                left += 1
                
            elif height[left] > height[right]:
                prod = height[right] * (right - left)
                right -= 1
                
            maxcontainer = max(prod, maxcontainer)
            
        return maxcontainer
            