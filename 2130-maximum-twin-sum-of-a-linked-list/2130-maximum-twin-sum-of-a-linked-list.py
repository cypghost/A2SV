# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = head
        cur = head.next
        
        twins = [temp.val]

        index = 0
        
        while cur.next:
            temp = temp.next
            cur = cur.next.next
            
            twins.append(temp.val)
            index += 1

        temp = temp.next

        while temp:
            twins[index] += temp.val
            
            index -= 1
            temp = temp.next

        return max(twins)
        
        # Approach 1
        
#         temp = head
#         cur = head
#         count = 1
        
#         add = 0
#         itr = 0
            
#         while cur.next:
#             count += 1
#             cur = cur.next
         
#         while itr != (count // 2):
#             cur = head
#             idx = 0
            
#             while idx != count - itr - 1:
#                 cur = cur.next
#                 idx += 1
            
#             sums = temp.val + cur.val
#             add = max(sums, add)
            
#             temp = temp.next
#             itr += 1
        
#         return add
            
                