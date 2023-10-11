# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self.ans = []
#         self.left = 0
#         self.n = len(nestedList)
        
#     def inside(arr):
#         i = 0
#         while i < len(arr):
#             if type(arr[i]) == int:
#                 self.ans.append(self.arr[i])
            
#             else:
#                 inside(arr[i])
            
#             i += 1
    
#     def next(self) -> int:
#         if type(self.ans[self.left]) == int:
#             self.ans.append(self.nestedList[self.left])
        
#         elif type(self.ans[self.left]) == list:
#             inside(ans[self.left])
            
    
#     def hasNext(self) -> bool:
#          if self.left < self.n - 1:
#                 return True
        
#          return False
    
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ans = []
        self.left = 0
        self.n = len(nestedList)
        self.flatten(nestedList)  # Call flatten to initialize the 'ans' list.

    def flatten(self, arr):
        for item in arr:
            if item.isInteger():
                self.ans.append(item.getInteger())
            else:
                self.flatten(item.getList())

    def next(self) -> int:
        if self.hasNext():
            val = self.ans[self.left]
            self.left += 1
            return val

    def hasNext(self) -> bool:
        return self.left < len(self.ans)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())