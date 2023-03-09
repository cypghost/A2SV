# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Solution 1
        
        # ans = []
        # out = []

        # def maxDepth(root):
        #     if not root:
        #         return 0

        #     return max(maxDepth(root.left), maxDepth(root.right)) + 1
        
        # def findnodes(root, n):
        #     if not root:
        #         return root
            
        #     if n == 0:
        #         res.append(root.val)
        #         return

        #     findnodes(root.left, n - 1)
        #     findnodes(root.right, n - 1)

        # Depth = maxDepth(root)

        # for index in range(Depth):
        #     res = []
        #     findnodes(root, index) 
        #     ans.append(res)

        # for index in range(len(ans)):
        #     out.append(ans[index][-1])
        
        # del ans

        # return out


        # Solution 2

        res = []

        def findnodes(root, level):
            if not root:
                return root
            
            if len(res) == level:
                res.append(root.val)
            
            findnodes(root.right, level + 1)
            findnodes(root.left, level + 1)
        
        findnodes(root, 0)

        return res
