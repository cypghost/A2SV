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

        return True if abs(heights(root.left) - heights(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) else False
        
        