# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head 
        
        if head == None:
            return head
        
        even = head.next
        temp = head.next
        
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next 
            
            even.next = even.next.next 
            even = even.next 
            
        odd.next = temp 
        
        return head 
            
            
            