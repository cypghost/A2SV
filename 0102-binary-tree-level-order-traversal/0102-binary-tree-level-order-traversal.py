# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def maxDepth(root):
            if not root:
                return 0

            return max(maxDepth(root.left), maxDepth(root.right)) + 1
        
        def findnodes(root, n):
            if not root:
                return root
            
            if n == 0:
                res.append(root.val)
                return

            findnodes(root.left, n - 1)
            findnodes(root.right, n - 1)

        Depth = maxDepth(root)

        for index in range(Depth):
            res = []
            findnodes(root, index) 
            ans.append(res)
        
        return ans