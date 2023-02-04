# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None: 
            return 
        
        temp = head
        count = 0
        
        while temp:
            count += 1
            temp = temp.next
        
        if n < 1  or n > count:
            return -1
    
        temp = head
        
        if n == count:
            head = head.next
    
        else:
            for _ in range(1, count - n):
                temp = temp.next
            
            temp.next = temp.next.next
        
        return head
#         if head == None:
#             return
        
#         temp = head
#         count = 1
    
#         while temp:
#             count += 1
                
#         if n > count or n < 0: 
#             return
        
#         temp = head
        
#         if n == count:
#             head = head.next
            
#         else:
#             for _ in range(1, count - n):
#                 temp = temp.next
        
#             temp.next = temp.next.next
        
#         count -= 1
        
#         return head