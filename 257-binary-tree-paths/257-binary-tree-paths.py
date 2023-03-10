# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def Traversal(root, path):
            if not root:
                return root
    
            if not root.right and not root.left:
                ans.append(''.join(path) + str(root.val))
                return root
            
            path.append(str(root.val) + '->')

            Traversal(root.left, path)
            Traversal(root.right, path)
            
            path.pop()

        Traversal(root, [])

        return ans
    