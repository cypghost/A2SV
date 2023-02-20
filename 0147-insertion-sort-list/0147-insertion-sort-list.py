# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1. if the value is less than the head value then add it to the first list 
        2. else move the head ptr to next and compare
        
        4, 2, 1, 3
        
   1.   4 > 2                             2.    2 > 1                               
        2, 4, 1, 3                              1, 2, 4, 3
        
   3.   1 > 3 False                       4.    2 > 3 False                    5.    4 > 3
        1, 2, 4, 3                              1, 2, 4, 3                           1, 2, 3, 4
           ^                                          ^
           |                                          |
          temp                                       temp
          
        ''' 
        res = ListNode()
        res.next = head
        res_tail = head
        
        curr = head.next
        
        while curr:
            if curr.val >= res_tail.val:
                res_tail = curr
                curr = curr.next
                
            else:
                res_tail.next = curr.next
                
                pos = res
                
                while pos.next.val < curr.val:
                    pos = pos.next
                
                curr.next = pos.next
                pos.next = curr
                
                curr = res_tail.next
        
        return res.next