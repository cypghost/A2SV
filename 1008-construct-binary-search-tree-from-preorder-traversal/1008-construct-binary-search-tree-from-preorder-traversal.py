# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        return self.helper(preorder,inorder)

    def helper(self,preorder,inorder):
        if inorder:
            root = TreeNode(preorder.pop(0)) 
            idx = inorder.index(root.val)
            
            root.left = self.helper(preorder, inorder[:idx])
            root.right = self.helper(preorder, inorder[idx + 1:])
            
            return root