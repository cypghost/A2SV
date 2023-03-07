# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode], ans= []) -> List[int]:    
#         if not root:
#             return []
        
#         ans = self.inorderTraversal(root.left)
#         ans.append(root.val)
#         ans += self.inorderTraversal(root.right)
        
#         return ans
    
        ans = []
        
        def traverse(root):
            
            if root:
                traverse(root.left)
                ans.append(root.val)
                traverse(root.right)
        
        traverse(root)
        
        return ans
