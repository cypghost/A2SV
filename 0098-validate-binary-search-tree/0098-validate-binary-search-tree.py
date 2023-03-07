# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        # Solution 1
    
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         
        
#         ans = []

#         def inorderTraversal(root):
#             if not root:
#                 return root
            
#             inorderTraversal(root.left)
#             ans.append(root.val)
#             inorderTraversal(root.right)

#         inorderTraversal(root)

#         if ans == sorted(ans) and len(set(ans)) == len(ans):
#             return True

#         return False


        # Solution 2

class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val=float('-inf'), max_val=float('inf')) -> bool:
        if not root:
            return True

        if root.val <= min_val or root.val >= max_val:
            return False

        left_valid = self.isValidBST(root.left, min_val, root.val)
        right_valid = self.isValidBST(root.right, root.val, max_val)

        return left_valid and right_valid



        

        
        



