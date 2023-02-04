# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp2 = head
        
        if head == None:
            return 
        
        temp = head.next
        
        while temp2:
            temp = temp2.next
            
            while temp:
                
                if temp2.val == temp.val:
                    temp2.next = temp.next
    
                temp = temp.next
           
            temp2 = temp2.next
            
            
        return head
            