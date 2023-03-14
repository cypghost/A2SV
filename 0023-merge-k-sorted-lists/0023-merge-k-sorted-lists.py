# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        v = []
        for index in lists:
            x = index
            
            while x:
                v += [x.val]
                x = x.next
        
        v = sorted(v, reverse=True)
        ans = None
        
        for idx in v:
            ans = ListNode(idx, ans)
            
        return ans
        
        