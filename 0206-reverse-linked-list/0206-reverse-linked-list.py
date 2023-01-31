# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp2 = head 
        
        if head == None:
            return 
            
        while temp2.next != None:
            temp = temp2.next
            
            while temp != None:
                value = temp2.val

                temp2.val = temp.val
                temp.val = value

                temp = temp.next
                
            temp2 = temp2.next
            
        return head

            