# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        queue = deque([root])
        
        while queue:
            cur = queue.popleft()
            
            if cur.left:
                queue.append(cur.left)

                graph[cur.val].append(cur.left.val)
                graph[cur.left.val].append(cur.val)

            if cur.right:
                queue.append(cur.right)

                graph[cur.val].append(cur.right.val)
                graph[cur.right.val].append(cur.val)
        
        queue = deque([target.val])
        seen = set([target.val])
        
        while k and queue:
            k -= 1

            for _ in range(len(queue)):
                cur = queue.popleft()
                
                for neighbour in graph[cur]:
                    if neighbour not in seen:
                        queue.append(neighbour)
                        seen.add(neighbour)

        return list(queue)