# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return head
        
        original = [head.val]
        temp = head
        count = 0
        
        
        while temp.next:
            count += 1
            temp = temp.next
            original.append(temp.val)
            
        if original == original[::-1]:
            return True
        
        else:
            return False
    
                
            
        # Approach 1
        
#         temp2 = head
        
#         temp = temp2
        
#         count1 = 1
#         count = 1
#         count2 = 1
        
#         palindrome = True
        
#         while temp != None:
#             temp = temp.next
#             count1 += 1
        
#         if count1 == 2:
#             return True
            
#         while count1 > count:
#             temp = temp2.next
            
#             while count2 >= count1 - 1:
#                 temp = temp.next
#                 count2 += 1
                
#             if temp2.val == temp.val:
#                 palindrome = True
                    
#             else:
#                 palindrome = False
                
#             temp2 = temp2.next
            
#             count1 -= 1
#             count += 1
            
#         if palindrome:
#             return True
        
#         else:
#             return False
            
        # Approach 2 
        
#         temp2 = head
        
#         temp = temp2
        
#         count1 = 1
#         count = 1
        
#         palindrome = True
        
#         while temp != None:
#             temp = temp.next
#             count1 += 1
            
#         while count1 > count:
#             temp = temp2.next
#             count2 = count
            
#             while count2 < count1 - 1:
#                 temp = temp.next
#                 count2 += 1
                
#             if temp2.val == temp.val:
#                 palindrome = True
                    
#             else:
#                 palindrome = False
                
#             temp2 = temp2.next
            
#             count1 -= 1
#             count += 1
            
#         if palindrome:
#             return True
        
#         else:
#             return False
            
                 