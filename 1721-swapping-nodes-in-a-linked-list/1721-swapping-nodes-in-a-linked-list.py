# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return []
        
        temp = head 
        ans = []
        
        while temp:
            ans.append(temp.val)
            temp = temp.next
        
        ans[k - 1], ans[len(ans) - k] =  ans[len(ans) - k], ans[k - 1]
                  
        head2 = ListNode()
        temp = head2
        
        for index in range(len(ans)):
            head2.next = ListNode(ans[index])
            head2 = head2.next
            
        return temp.next