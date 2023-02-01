# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp2 = head
        
        if head == None:
            return 
        temp = head
        
        count = 1
        
        while temp.next != None:
            temp = temp.next
            count += 1
            
        k %= count
        count = 1
        
        while count != k + 1 :
            temp = temp2.next 
            
            while temp != None:
                value = temp2.val
                
                temp2.val = temp.val
                temp.val = value
                
                temp = temp.next
                
            count += 1
        
        return head
            