# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp2 = head
        
        count = 0
        
        while temp2:
            temp2 = temp2.next
            count += 1
        
        length = count // 2
        
        for itr in range(length):
            head = head.next
                
        return head
            
            
                
                    
                
                
                
                