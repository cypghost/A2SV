# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp2 = head
        count = 1
        
        while count != left:
            temp2 = temp2.next
            count += 1 
      
        while count != right + 1:
            temp = temp2.next
            count2 = count + 1
            
            while count2 != right + 1:
                value = temp2.val
                
                temp2.val = temp.val
                temp.val = value
                
                temp = temp.next
                count2 += 1
            
            temp2 = temp2.next
            count += 1
            
        return head