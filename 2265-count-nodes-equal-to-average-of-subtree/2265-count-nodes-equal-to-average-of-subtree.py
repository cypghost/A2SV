# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = []
        
        def preorderTraversal(root):
            if not root:
                return []
            
            ans = [root.val]
            ans += preorderTraversal(root.left)
            ans += preorderTraversal(root.right)

            return ans
        
        res = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            temp = preorderTraversal(curr)

            if temp and sum(temp) // len(temp) == curr.val:
                res += 1

            curr = curr.right
            
        return res