# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root, pnt, gpnt):
            if not root:
                return 0
            
            val = 0
            
            if gpnt % 2 == 0:
                val = root.val
            
            val += dfs(root.left, root.val, pnt)
            val += dfs(root.right, root.val, pnt)
            
            return val
        
        return dfs(root, 1, 1)
            
            