# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        if not head.next:
            return head.next
          
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
            
        while slow and slow != head:
            slow = slow.next
            head = head.next
            
        if slow != head:
            return None
        
        return head
        
        
        