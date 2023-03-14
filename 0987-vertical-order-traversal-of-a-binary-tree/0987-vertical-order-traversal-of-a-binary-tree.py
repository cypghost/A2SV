# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        
        small, large = float("inf"), -float("inf")
        
        def helper(root, hort, vert):
            nonlocal small, large
            
            small = min(hort,  small)
            large = max(hort, large)
            
            dic[hort].append((vert, root.val))
            
            if root.left:
                helper(root.left,  hort - 1, vert + 1)
                
            if root.right:
                helper(root.right, hort + 1, vert + 1)
        
        helper(root, 0, 0)
        
        out = []
        
        for index in range(small, large + 1):
            out += [[idx for index, idx in sorted(dic[index])]]
            
        return out
        