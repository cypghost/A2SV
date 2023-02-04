# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp2 = node
        
        while temp2.next:
            temp2.val = temp2.next.val
            temp2 = temp2.next
        
        temp2 = node
        
        while temp2.next.next:
            temp2 = temp2.next
        
        temp2.next = None
        