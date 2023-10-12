# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
    
        def dfs(node):
            nonlocal moves
            
            if not node:
                return 0

            # Recursively calculate the balance of coins in left and right subtrees
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)

            # Calculate the excess coins at this node
            excess_coins = node.val + left_balance + right_balance - 1

            # Calculate the moves needed to balance this node
            moves += abs(excess_coins)

            return excess_coins

        dfs(root)
        return moves

        