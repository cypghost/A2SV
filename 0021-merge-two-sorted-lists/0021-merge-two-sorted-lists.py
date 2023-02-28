# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:   
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if list1 == None and list2 == None:
#             return 
    
#         temp = list1
#         cur = list2
#         values = []
        
#         if list2 == None:
            
#             while temp.next:
#                 temp = temp.next
                
#             temp.next = cur
#             temp = list1
            
#             while temp:
#                 values.append(temp.val)
#                 temp = temp.next

#             values.sort()

#             temp = list1
#             values = collections.deque(values)

#             while temp:
#                 temp.val = values.popleft()
#                 temp = temp.next

#             return list1
            
#         else:
            
#             while cur.next:
#                 cur = cur.next
                
#             cur.next = temp
#             cur = list2
            
#             while cur:
#                 values.append(cur.val)
#                 cur = cur.next

#             values.sort()

#             cur = list2
#             values = collections.deque(values)

#             while cur:
#                 cur.val = values.popleft()
#                 cur = cur.next

#             return list2
            
            if not list1 and not list2:
                return 
            
            if not list1 and list2:
                return list2
            
            if list1 and not list2:
                return list1
            
            cur = list1
            curr = list2
                    
            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return cur
            
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return curr
            
            
            
        
            
                    
            
            
                
                
                
        