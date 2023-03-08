# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def heights(root):
            return 0 if not root else max(heights(root.left), heights(root.right)) + 1
        
        leftlen = heights(root.left)
        rightlen = heights(root.right)

        if abs(leftlen - rightlen) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True  
        
        else:
            return False
        
        