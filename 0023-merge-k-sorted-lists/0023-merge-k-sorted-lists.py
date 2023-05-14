# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# HEAP

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        
        min_heap = []
        
        heapq.heapify(min_heap)
        
        for index in range(n):
            if lists[index]:
                temp_val = lists[index].val
                lists[index] = lists[index].next
                heapq.heappush(min_heap,[temp_val, index])
            
        head = ListNode()
        node = head
        
        while min_heap:
            val, ind = heapq.heappop(min_heap)
            node_i = ListNode(val = val)
            node.next = node_i
            node = node.next
            
            if lists[ind]:
                temp_val = lists[ind].val
                lists[ind] = lists[ind].next
                heapq.heappush(min_heap, [temp_val,ind])
          
        return head.next

# LINKED LISTS
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
        
        
