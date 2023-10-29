# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return node and not node.left and not node.right
        
        def tree(root):
            if not root:
                return 0

            left_sum = 0
            if isLeaf(root.left):
                left_sum = root.left.val

            return left_sum + tree(root.left) + tree(root.right)

        return tree(root)