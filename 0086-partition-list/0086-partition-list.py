# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head1 = None
        self.head2 = None
        
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:        
        temp = head
        
        less = None
        greater = None
        
        if head == None or head.next == None:
            return head
        
        while temp != None:
            if temp.val < x:
                if less == None: 
                    self.head1 = ListNode(temp.val)
                    less = self.head1
                    
                else:
                    less.next = ListNode(temp.val)
                    less = less.next
                
            else:
                if greater == None: 
                    self.head2 = ListNode(temp.val)
                    greater = self.head2
                    
                else:
                    greater.next = ListNode(temp.val)
                    greater = greater.next
        
            temp = temp.next
        
        if less != None:
            less.next = self.head2
            
        else:
            return self.head2
        
        return self.head1
            
            
        
        
        
        
                    
                    
                    
                
                
            