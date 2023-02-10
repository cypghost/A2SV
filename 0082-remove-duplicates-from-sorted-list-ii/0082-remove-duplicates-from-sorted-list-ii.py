# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(-1)
        node.next = head

        cur = head
        prv = node
        
        while cur:
            
            while cur.next and cur.val == cur.next.val:
                
                cur = cur.next
            
            if prv.next == cur:
                
                prv = prv.next
                cur = cur.next
            
            else:
                prv.next = cur.next
                cur = prv.next
        
        return node.next