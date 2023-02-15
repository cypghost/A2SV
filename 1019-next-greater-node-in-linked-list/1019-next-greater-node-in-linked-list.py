# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        itr = []
        answer = []
        
        temp = head
        
        index = 0
        
        while temp:
            
            while itr and itr[-1][0] < temp.val:
                answer[itr[-1][1]] = temp.val
                itr.pop()
            
            itr.append((temp.val, index))
            answer.append(0)
            
            index += 1
            
            temp = temp.next
            
        return answer
                    
                
                