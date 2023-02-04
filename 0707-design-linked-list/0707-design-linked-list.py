class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
    
        temp = self.head
    
        for index in range(0, index):
            temp = temp.next
        
        return temp.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val) 

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
         if index > self.size:
            return

         temp = self.head
         new_node = ListNode(val)

         if index <= 0:
             new_node.next = temp
             self.head = new_node
            
         else:
             for _ in range(index - 1):
                 temp = temp.next
                
             new_node.next = temp.next
             temp.next = new_node

         self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0  or index >= self.size:
            return -1
    
        temp = self.head
        
        if index == 0:
            self.head = self.head.next
    
        else:
            for _ in range(0, index - 1):
                temp = temp.next
            
            temp.next = temp.next.next
        
        self.size -= 1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)