# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        diction = defaultdict(int)
        
        def inorderTraverse(root):
            if not root:
                return root
            
            inorderTraverse(root.left)
            diction[root.val] += 1
            inorderTraverse(root.right)

        inorderTraverse(root)

        maxcount = 0
        element = []

        for index in diction:
            if diction[index] > maxcount:
                element = [index]
                maxcount = diction[index]

            elif diction[index] == maxcount:
                element.append(index)

        return element