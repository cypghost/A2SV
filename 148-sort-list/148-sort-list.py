# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(temp)

        sorted = ListNode(0)
        tail = sorted

        while left and right:
            temp = None
            if left.val <= right.val:
                temp = ListNode(left.val)
                left = left.next
            else:
                temp = ListNode(right.val)
                right = right.next

            tail.next = temp
            tail = tail.next

        if right:
            tail.next = right
        
        elif left:
            tail.next = left
  
        return sorted.next        































        # def sortedInsert(head, new_node):
        #     current = None

        #     if not head or head.val >= new_node.val:
        #         new_node.next = head
        #         head = new_node

        #     else:
        #         current = head
                
        #         while current.next and current.next.val < new_node.val:
        #             current = current.next

        #         new_node.next = current.next
        #         current.next = new_node

        #     return head

        # sorte = None
        # current = head

        # while current:
        #     next = current.next
        #     sorte = sortedInsert(sorte, current)

        #     current = next
            
        # head = sorte
        
        # return head


        