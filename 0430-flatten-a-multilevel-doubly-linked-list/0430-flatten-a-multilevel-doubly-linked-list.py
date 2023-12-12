"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        
        T = self.traverse(head, [])
        new = Node(T[0])
        curr = new
        curr.child = None
    
        for i in range(1, len(T)):
            new_node = Node(T[i])
            new_node.prev = curr
            new_node.child = None
            curr.next = new_node
            curr = curr.next
        
        return new
        
    def traverse(self, head, ans):
        if head is None:
            return 
        
        ans.append(head.val)
        self.traverse(head.child, ans)
        self.traverse(head.next, ans)
        
        return ans