# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = ListNode()
        ptr = temp
        ans = ListNode()
        cur = ans
        idx = 0
        node = head
        
        while node:
            if idx == k :
                reversednode = self.reverseList(temp.next)
                cur.next = reversednode
                
                while cur.next:
                    cur = cur.next
                    
                temp = ListNode()
                ptr = temp
                idx = 0
                
            
            ptr.next = ListNode(node.val,None)    
            ptr = ptr.next
            idx = idx + 1
            node = node.next
        res = self.reverseList(temp.next)
        
        if res:
            if k != idx:
                reverseagain = self.reverseList(res)
                cur.next = reverseagain
                
            else:
                cur.next = res
                
        return ans.next
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr,temp = None, head
        
        while temp:
            tmp = temp.next
            temp.next = ptr
            ptr = temp
            temp = tmp
            
        return ptr 
#         count = 1
#         temp = head
        
#         while temp:
#             count += 1
#             temp = temp.next
        
#         reversesum = 0

#         cur = head
#         prev = None
#         index = 0
        
#         while cur:
#             index += 1
            
#             temp = cur.next
#             cur.next = prev
#             prev = cur
#             cur = temp
            
#             if index % k == 0:
#                 print(prev)
            