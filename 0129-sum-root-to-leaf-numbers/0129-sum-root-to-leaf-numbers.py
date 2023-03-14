# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.helper(root, 0)
        return self.res
    
    def helper(self, root, path):
        if not root:
            return root
        
        if not root.left and not root.right:
            path = path * 10 + root.val
            self.res += path
            
        self.helper(root.left, path * 10 + root.val)
        self.helper(root.right, path * 10 + root.val)