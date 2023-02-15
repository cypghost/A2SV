# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer, stack = [], []
        
        while head:
            while stack and stack[-1][1] < head.val:
                answer[stack.pop()[0]] = head.val
                
            stack.append([len(answer), head.val])
            answer.append(0)
            
            head = head.next
            
        return answer
                    
                
                