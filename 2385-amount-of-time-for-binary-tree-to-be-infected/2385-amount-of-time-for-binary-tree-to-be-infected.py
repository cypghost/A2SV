# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(set)
        queue = deque([start])
        visited = set([start])
        result = 0
        
        def tree(root, parent):
            if not root:
                return 
            
            if parent != 0:
                graph[root.val].add(parent)
                
            if root.right:
                graph[root.val].add(root.right.val)
            
            if root.left:
                graph[root.val].add(root.left.val)
            
            tree(root.right, root.val)
            tree(root.left, root.val)
        
        tree(root, 0)
        
        while queue:
            a = len(queue)
            
            while a > 0:
                cur = queue.popleft()
                
                for i in graph[cur]:
                    if i not in visited:
                        visited.add(i)
                        queue.append(i)
                        
                a -= 1
                
            result += 1
        
        return result - 1