# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1
        
        if not head or not head.next:
            return head
        
        fast = head
        slow = head.next
        
        while slow and fast:
            slow.val, fast.val = fast.val, slow.val
            
            if fast.next:
                fast = fast.next.next
            
            if slow.next:
                slow = slow.next.next
        
        return head


        # Approach 2
        
#         if not head or not head.next:
#             return head
        
#         temp = ListNode()
#         temp.next = head
        
#         header = temp
        
#         curr = head
        
#         list1 = head
#         list2 = head.next
        
#         while list1 and list2:
#             curr = list2.next
#             header.next = list2
            
#             list2.next = list1
#             list1.next =None
            
#             header = list1
#             list1 = curr
            
#             if curr:
#                 list2 = curr.next
                
#         if curr:
#             header.next = curr
            
#         return temp.next
            