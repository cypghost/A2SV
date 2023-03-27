# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        presum = {0: 1}
        
        def helper(root, targetSum, currsum):
            if not root:
                return

            currsum += root.val
            self.count += presum.get(currsum - targetSum, 0)
            
            presum[currsum] = presum.get(currsum, 0) + 1

            helper(root.left, targetSum, currsum)
            helper(root.right, targetSum, currsum)

            presum[currsum] -= 1

        
        helper(root, targetSum, 0)
        
        return self.count
        
    