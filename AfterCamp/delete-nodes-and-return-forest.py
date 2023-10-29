# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node, parent, is_root):
            if not node:
                return None

            is_deleted = node.val in to_delete

            if is_root and not is_deleted:
                forest_roots.append(node)

            node.left = dfs(node.left, node, is_deleted)
            node.right = dfs(node.right, node, is_deleted)

            return None if is_deleted else node

        forest_roots = []
        dfs(root, None, True)
        return forest_roots
