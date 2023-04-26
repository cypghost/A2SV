# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg = [float(root.val)]
        queue = deque([root])
    
        while queue:
            total = 0
            
            for index in range(len(queue)):
                popped = queue.popleft()
                
                if popped.left:
                    queue.append(popped.left)
                    total += popped.left.val
                
                if popped.right:
                    queue.append(popped.right)
                    total += popped.right.val
                
            if queue:
                avg.append(total / len(queue))

        return avg



                

            
        
            
        