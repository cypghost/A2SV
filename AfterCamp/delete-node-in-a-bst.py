# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def inordertraverse(node):
            curr = node

            while curr.right:
                curr = curr.right
                
            return curr
        
        if not root:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                return root.right
            
            elif not root.right:
                return root.left
            
            temp = inordertraverse(root.left)

            root.val = temp.val

            root.left = self.deleteNode(root.left, temp.val)

        return root

        

        